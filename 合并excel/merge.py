import pandas as pd
import os

def 合并指定列的excel(文件路径列表, 输出文件路径, 合并列名列表):
    """
    从多个excel文件中读取列名为'a'和'b'的列，合并后输出到一个新的excel文件。
    :param 文件路径列表: 包含所有excel文件路径的列表
    :param 输出文件路径: 合并后输出的excel文件路径
    """
    合并后的数据 = []
    for 路径 in 文件路径列表:
        if os.path.exists(路径):
            try:
                df = pd.read_excel(路径, usecols=合并列名列表)
                合并后的数据.append(df)
            except Exception as e:
                print(f"读取文件 {路径} 时出错: {e}")
        else:
            print(f"文件不存在: {路径}")
    if 合并后的数据:
        总表 = pd.concat(合并后的数据, ignore_index=True)
        总表.to_excel(输出文件路径, index=False)
        print(f"合并完成，已保存到 {输出文件路径}")
    else:
        print("没有可合并的数据。")

# 示例用法
if __name__ == "__main__":
    # 这里填写需要合并的excel文件路径列表
    文件列表 = [
        "C:/Users/lijiang/Downloads/对公发票池导出20250814112208/对公发票池导出20250814112208_0001.xlsx",
        "C:/Users/lijiang/Downloads/对公发票池导出20250814112208/对公发票池导出20250814112208_0002.xlsx",
        "C:/Users/lijiang/Downloads/对公发票池导出20250814112208/对公发票池导出20250814112208_0003.xlsx"
    ]
    输出路径 = "./合并excel/合并结果.xlsx"
    合并指定列的excel(文件列表, 输出路径, ['发票号码'])
