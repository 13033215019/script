import pandas as pd

# 读取Excel文件
excel_path = r"C:\Users\lijiang\Downloads\发票补充成本中心.xlsx"
df = pd.read_excel(excel_path, dtype=str)

# 创建输出文件
output_file = "output.sql"
with open(output_file, 'w', encoding='utf-8') as f:
    # 遍历每一行，格式化SQL并输出到文件
    for idx, row in df.iterrows():
        receipt_code = row['发票号码']
        cost_center_code = row['costCenterCode']
        cost_center_item_code = row['costCenterItemCode']
        
        sql = f"""insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = '{cost_center_code}' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = '{cost_center_item_code}' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = '{cost_center_code}' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '{receipt_code}';"""
        
        f.write(sql + '\n')
