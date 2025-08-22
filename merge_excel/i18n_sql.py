import pandas as pd

def generate_i18n_sql(excel_path):
    """
    根据Excel文件生成国际化SQL语句
    
    参数:
    excel_path: Excel文件路径
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(excel_path, dtype=str)
        
        # 定义支持的报表名列表
        supported_reports = [
            '发票汇总报表',
            '发票查验轮询状态变更报表',
            '发票异常状态报表'
        ]
        
        # 打开文件准备写入
        with open('res.sql', 'w', encoding='utf-8') as f:
            # 遍历每一行
            for idx, row in df.iterrows():
                # 检查报表名是否在支持的列表中
                if row['报表名'] in supported_reports:
                    column_id = row['column_id']
                    
                    # 处理空值
                    en_name = '' if pd.isna(row['字段名（英）']) else row['字段名（英）']
                    en_desc = '' if pd.isna(row['字段说明（英）']) else row['字段说明（英）']
                    en_logic = '' if pd.isna(row['取值逻辑（英）']) else row['取值逻辑（英）']
                    ja_name = '' if pd.isna(row['字段名（日）']) else row['字段名（日）']
                    ja_desc = '' if pd.isna(row['字段说明（日）']) else row['字段说明（日）']
                    ja_logic = '' if pd.isna(row['取值逻辑（日）']) else row['取值逻辑（日）']
                    
                    # 生成英文SQL
                    en_sql = f"""replace into atl_report_column_i18n(id, language, column_display_name, column_desc, value_logic_desc)
values ({column_id},'en',"{en_name}","{en_desc}","{en_logic}");"""
                    
                    # 生成日文SQL
                    ja_sql = f"""replace into atl_report_column_i18n(id, language, column_display_name, column_desc, value_logic_desc)
values ({column_id},'ja',"{ja_name}","{ja_desc}","{ja_logic}");"""
                    
                    # 写入SQL语句到文件
                    f.write(en_sql + '\n')
                    f.write(ja_sql + '\n\n')  # 添加空行分隔
                    
        print("SQL语句已成功写入到 res.sql 文件")
                
    except Exception as e:
        print(f"生成SQL过程中出现错误: {str(e)}")

if __name__ == "__main__":
    # 示例使用
    excel_path = r"C:\Users\lijiang\Downloads\报表数据导出6.3（修改标红版）.xlsx"
    generate_i18n_sql(excel_path)
