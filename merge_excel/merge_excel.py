import pandas as pd
def merge_excel_files(file1_path, file2_path, output_path):
    """
    合并两个Excel文件，基于'中文'列进行匹配，只保留每个中文对应的第一行匹配结果
    
    参数:
    file1_path: 第一个Excel文件路径
    file2_path: 第二个Excel文件路径
    output_path: 输出Excel文件路径
    """
    try:
        # 读取两个Excel文件
        df1 = pd.read_excel(file1_path, dtype=str)  # 将所有列读取为字符串类型
        df2 = pd.read_excel(file2_path, dtype=str)  # 将所有列读取为字符串类型
        # 基于'中文'列进行合并，然后根据四列（table_name, id, 列名, 中文）一起去重，只保留第一行
        merged_df = pd.merge(df1, df2, on='employee_id', how='left')
        # 保存合并后的结果，所有列都作为文本类型保存
        merged_df.to_excel(output_path, index=False)
        print(f"文件已成功合并并保存至: {output_path}")
        
    except Exception as e:
        print(f"合并过程中出现错误: {str(e)}")

if __name__ == "__main__":
    # 示例使用
    file1_path = r"C:\Users\lijiang\Downloads\2025-07-07-10-06-40_EXPORT_CSV_20101900_829_0.xlsx"
    file2_path = r"C:\Users\lijiang\Downloads\执行结果1 (7).xlsx"
    output_path = r"C:\Users\lijiang\Desktop\merged_result_20250708105728001.xlsx"
    
    merge_excel_files(file1_path, file2_path, output_path)
