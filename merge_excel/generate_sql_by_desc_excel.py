import pandas as pd

# 读取Excel文件
excel_path = r"C:\Users\lijiang\Desktop\merged_result3.xlsx"
df = pd.read_excel(excel_path, dtype=str)

# 遍历每一行，格式化SQL并输出
for idx, row in df.iterrows():
    table_name = row['table_name']
    col_name = row['列名']
    value = row['字段名（日）']
    id_value = row['id']
    sql = "replace into %s (id, language, %s) values (%s, 'ja', '%s');" % (table_name, col_name, id_value, value)
    if pd.isna(value) or value == 'nan' or value == '':
        sql = '#' + sql
    print(sql)
