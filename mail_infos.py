import re

# 读取 mail_infp.log 文件内容
with open('mail_infp.log', 'r', encoding='utf-8') as f:
    content = f.read()

# 还原转义字符
content = content.replace('\\/', '/').replace('\\\\', '\\')

# 使用正则表达式查找所有的 URL
urls = re.findall(r'https?://[^\s\'"<>]+', content)

# 打印所有找到的 URL
for url in urls:
    print(url)
    
    
    
    