import requests
import os
import time

def getToken(host):
    url = f'{host}/oauth/token'

    # 设置请求头
    headers = {
        'x-forwarded-prefix': 'gateway',
        'Authorization': 'Basic and0LWF3MXdiZ3Z0enc1MDpOVE0xTmpKaFltRXRObUZqT0MwME1UQm1MV0poWkRFdE1tTTJNamd6T0dRMU5UTTM='
    }

    # 设置请求表单数据
    data = {
        'grant_type': 'client_credentials',
        'scope': 'write'
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data)

    # 打印响应内容
    response_json = response.json()
    access_token = response_json.get('access_token')
    return access_token

def download_attachment(token, host, attachmentOID, local_path):
    # 设置请求的URL
    url = f'{host}/api/attachments/{attachmentOID}'
    
    # 设置请求头
    headers = {
        'x-forwarded-prefix': 'gateway',
        'Authorization': f'Bearer {token}'
    }
    
    # 发送GET请求
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    # 获取下载链接
    download_url = response_json.get('downloadUrl')
    
    # 创建本地文件夹
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    
    # 下载文件
    file_name = attachmentOID + '_' + response_json.get('fileName')
    file_path = os.path.join(local_path, file_name)
    file_response = requests.get(download_url)
    
    with open(file_path, 'wb') as file:
        file.write(file_response.content)
    
    print(f'文件已下载到: {file_path}')



url_map = {
    "a1": "http://api.huilianyi.com",
    "uat": "https://apiuat.huilianyi.com"
}

print('输入环境')
env = input()
host = url_map[env]
# 设置请求的URL
token = getToken(host)
path = r'C:\Users\lijiang\Documents\发票\xml'


# 读取文件中的每一行
with open(rf'{path}\atta.txt', 'r') as file:
    oids = file.readlines()

# 去除每行的换行符
oids = [oid.strip() for oid in oids]

# 下载每个附件
for oid in oids:
    try:
        download_attachment(token, host, oid, rf'{path}')
    except Exception as e:
        print(f'下载附件 {oid} 时发生异常: {e}')
        time.sleep(10)
        download_attachment(token, host, oid, rf'{path}')
