# script
# 发票处理脚本

## 功能说明
本仓库包含多个用于处理发票的Python脚本，主要用于发票识别、验证和下载等功能。

## 主要脚本
- `download_atta_hly.py`: 用于下载发票附件
- `map_excel/check_order_map.py`: 发票验证错误码映射
- `map_excel/ocr_order_map.py`: 发票OCR识别结果处理

## 使用说明

### 下载发票附件
1. 运行 `download_atta_hly.py`
2. 输入环境（a1或uat）
3. 脚本会自动下载指定目录下的附件

### 发票验证
`check_order_map.py` 包含了各种发票验证错误码及其对应的错误说明，可用于发票验证失败时的错误处理。

### OCR识别处理
`ocr_order_map.py` 用于处理发票OCR识别结果：
1. 读取CSV文件中的OCR识别结果
2. 解析JSON格式的识别数据
3. 提取发票号码和发票代码
4. 生成处理后的CSV文件

## 注意事项
- 请确保有正确的API访问权限
- 下载附件时需要正确的token认证
- OCR识别结果需要符合指定的JSON格式
