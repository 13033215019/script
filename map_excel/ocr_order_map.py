import pandas as pd
import json

# 读取CSV文件
df = pd.read_csv('map_excel/发票识别.csv')

# 创建一个新的列表来存储处理后的数据
new_rows = []

# 遍历每一行
for index, row in df.iterrows():
    try:
        print(f"处理第 {index} 行:")
        print(f"列名: {list(row.index)}")
        print(f"数据: {row.to_dict()}")
        print("-" * 50)
        
        # 检查识别结果是否为"识别成功"
        if row['反馈结果'] == '识别成功':
            # 解析JSON字符串       
            ocr_result = json.loads(row['ocr结果'])
            identify_results = ocr_result['response']['data']['identify_results']
            
            # 如果identify_results是列表，遍历每个发票
            if isinstance(identify_results, list):
                for invoice in identify_results:
                    new_row = row.copy()
                    new_row['发票号码'] = invoice['details'].get('number')
                    new_row['发票代码'] = invoice['details'].get('code')
                    new_rows.append(new_row)
            else:
                # 如果只有一个发票
                new_row = row.copy()
                new_row['发票号码'] = identify_results['details'].get('number')
                new_row['发票代码'] = identify_results['details'].get('code')
                new_rows.append(new_row)
        else:
            new_rows.append(row.copy())
            
    except json.JSONDecodeError as e:
        raise Exception(f"JSON解析错误: {str(e)}")
    except KeyError as e:
        raise Exception(f"找不到必要的列: {str(e)}")

# 创建新的DataFrame
new_df = pd.DataFrame(new_rows)

# 保存结果
new_df.to_csv('map_excel/发票识别_处理结果.csv', index=False, encoding='utf-8-sig')
print("处理完成！结果已保存到 '发票识别_处理结果.csv'")