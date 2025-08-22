import os
import sys
import zipfile
import openpyxl


def 检测文件类型(文件路径: str) -> str:
    """
    粗略检测文件类型：xlsx(zip)、xls(ole)、文本/HTML/PDF/未知
    返回: 'xlsx_zip' | 'xls_ole' | 'text' | 'html' | 'pdf' | 'unknown'
    """
    try:
        with open(文件路径, 'rb') as f:
            头 = f.read(8)
        if 头.startswith(b'PK\x03\x04'):
            return 'xlsx_zip'
        if 头.startswith(b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'):
            return 'xls_ole'
        if 头.startswith(b'%PDF'):
            return 'pdf'
        if b'<html' in 头.lower() or b'<!doctype html' in 头.lower():
            return 'html'
        try:
            with open(文件路径, 'rb') as f:
                样本 = f.read(4096)
            # 若可解码为UTF-8且出现逗号/制表符等，猜测为文本/CSV/TSV
            样本.decode('utf-8')
            if any(sep in 样本 for sep in [b',', b'\t', b'|', b';']):
                return 'text'
            return 'unknown'
        except Exception:
            return 'unknown'
    except Exception:
        return 'unknown'


def 用ExcelCOM强力修复(文件路径: str, 输出路径: str) -> tuple[bool, str | None]:
    """
    通过 Excel COM 的 CorruptLoad 修复/提取数据。
    需本机安装 Excel，且安装 pywin32。
    优先使用修复模式(1)，失败则尝试提取数据模式(2)。
    """
    try:
        import win32com.client as win32  # type: ignore
        from win32com.client import constants  # type: ignore
    except Exception as e:
        print(f"强力修复不可用（未安装 pywin32 或无 Excel）：{e}")
        return False, None

    # FileFormat: 51 = xlOpenXMLWorkbook (*.xlsx)
    xlOpenXMLWorkbook = 51

    xl = None
    wb = None
    try:
        xl = win32.DispatchEx("Excel.Application")
        xl.Visible = False
        xl.DisplayAlerts = False

        # 尝试修复模式
        for 模式 in (1, 2):  # 1=xlRepairFile, 2=xlExtractData
            try:
                wb = xl.Workbooks.Open(
                    Filename=os.path.abspath(文件路径),
                    UpdateLinks=False,
                    ReadOnly=True,
                    CorruptLoad=模式,
                )
                # 保存为 xlsx
                目录 = os.path.dirname(os.path.abspath(输出路径))
                if 目录 and not os.path.exists(目录):
                    os.makedirs(目录, exist_ok=True)
                wb.SaveAs(os.path.abspath(输出路径), FileFormat=xlOpenXMLWorkbook)
                return True, 输出路径
            except Exception as e:
                print(f"Excel COM 模式 {模式} 修复尝试失败：{e}")
            finally:
                if wb is not None:
                    try:
                        wb.Close(SaveChanges=False)
                    except Exception:
                        pass
                    wb = None
        return False, None
    finally:
        if xl is not None:
            try:
                xl.Quit()
            except Exception:
                pass


def 用OpenPyXL尝试修复(文件路径: str, 输出路径: str) -> tuple[bool, str | None]:
    try:
        wb = openpyxl.load_workbook(文件路径, data_only=True)
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for cell in row:
                    try:
                        _ = cell.value
                    except Exception:
                        cell.value = None
        wb.save(输出路径)
        return True, 输出路径
    except Exception as e:
        print(f"openpyxl 修复失败: {e}")
        return False, None


def 修复excel文件(文件路径: str, 输出路径: str | None = None) -> tuple[bool, str | None]:
    """
    先检测文件类型：
    - 若疑似 xlsx(zip) 或 xls(ole)，优先用 Excel COM 强力修复；
    - 若 COM 不可用或失败，再尝试 openpyxl（仅适用于 xlsx 且结构尚可）；
    - 若是文本/HTML/PDF，提示无法作为 Excel 直接修复。
    """
    if 输出路径 is None:
        基名, 扩展名 = os.path.splitext(文件路径)
        输出路径 = 基名 + '_fixed.xlsx'

    类别 = 检测文件类型(文件路径)
    print(f"检测到文件类型: {类别}")

    if 类别 in ('xlsx_zip', 'xls_ole', 'unknown'):
        成功, 路径 = 用ExcelCOM强力修复(文件路径, 输出路径)
        if 成功:
            return True, 路径
        # COM 失败后，若看起来是 xlsx(zip)，再尝试 openpyxl
        if 类别 == 'xlsx_zip':
            return 用OpenPyXL尝试修复(文件路径, 输出路径)
        return False, None

    if 类别 in ('text', 'html', 'pdf'):
        print("该文件看起来不是原生 Excel 文件，无法作为 Excel 直接修复。")
        return False, None

    # 兜底
    return False, None


if __name__ == "__main__":
    原始路径 = r"C:\Users\lijiang\Sync\ocr_test\res.xlsx"
    目标路径 = r"C:\Users\lijiang\Sync\ocr_test\fixed_res.xlsx"
    成功, 修复后路径 = 修复excel文件(原始路径, 目标路径)
    if 成功:
        print(f"修复成功，文件已保存至: {修复后路径}")
    else:
        print("修复失败。")
