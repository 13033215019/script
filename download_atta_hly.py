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

from requests.auth import HTTPBasicAuth

def get_open_api_token_for_a1():
    """
    获取a1环境的OpenAPI token，使用Basic Auth方式
    """
    url = 'https://console.huilianyi.com/oauth/token?_key=hkZ0wRxfCpE43aua'
    # 这里请替换为实际的用户名和密码
    username = 'b010ded8-ff3e-493a-8099-133aa93b2f93'
    password = 'NjM0NzdjNjgtNjAzNC00YTE3LTg5YTItNmNmNTgzMWQxODhk'
    headers = {
        'x-forwarded-prefix': 'gateway'
    }
    data = {
        'grant_type': 'client_credentials',
        'scope': 'write'
    }
    response = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth(username, password))
    response_json = response.json()
    access_token = response_json.get('access_token')
    print('OPEN API TOKEN', response_json)
    return access_token


    
def download_attachment_return_json(token, host, attachmentOID, local_path):
    # 设置请求的URL
    url = f'{host}/api/attachments/{attachmentOID}'
    
    # 设置请求头
    headers = {
        'x-forwarded-prefix': 'gateway',
        'Authorization': f'Bearer {token}'
    }
    
    # 发送GET请求
    response = requests.get(url, headers=headers)
    return response.json()

def get_file_extension(filename):
    """获取文件的后缀名（带点），例如 '.txt'、'.py'"""
    return os.path.splitext(filename)[1]

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
    download_file(download_url, attachmentOID + '_' + get_file_extension(response_json.get('fileName')), local_path)
    
def download_file(download_url, file_name, local_path):
    # 创建本地文件夹
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    file_path = os.path.join(local_path, file_name)
    # 如果文件已存在则直接跳过下载
    if os.path.exists(file_path):
        print(f'文件已存在，跳过下载: {file_path}')
        return
    file_response = requests.get(download_url)
    with open(file_path, 'wb') as file:
        file.write(file_response.content)
    print(f'文件已下载到: {file_path}')

def download_attachment_batch_open_api(token, host, attachmentOIDs, local_path):
    # 创建本地文件夹
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    
    # 设置请求的URL
    url = f'{host}/api/open/attachment/batch?_key=hkZ0wRxfCpE43aua'
    
    # 设置请求头
    headers = {
        'x-forwarded-prefix': 'gateway',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    # 按照步长为20拆分 attachmentOIDs
    batch_size = 20
    oid_batches = [attachmentOIDs[i:i + batch_size] for i in range(0, len(attachmentOIDs), batch_size)]
    
    processed_count = 0  # 记录已处理的附件数量

    for oid_batch in oid_batches:
        response = None
        try:
            # 发送POST请求
            response = requests.post(url, headers=headers, json=oid_batch)
            if response.status_code == 200:
                for item in response.json():
                    download_file(item.get('downloadUrl'), item.get('attachmentOID') + '.png', local_path)
                    processed_count += 1
                    if processed_count % 100 == 0:
                        time.sleep(1)
            else:
                print(f'批量下载请求失败，状态码: {response.status_code}')
                print(response.json())
        except Exception as e:
            print(f'批量下载附件时发生异常: {e}')
            time.sleep(10)
            response = requests.post(url, headers=headers, json=oid_batch)
            if response.status_code == 200:
                for item in response.json():
                    download_file(item.get('downloadUrl'), item.get('attachmentOID') + '.png', local_path)
                    processed_count += 1
                    if processed_count % 100 == 0:
                        time.sleep(1)
            else:
                print(f'批量下载请求失败，状态码: {response.status_code}')
                print(response.json())
    

url_map = {
    "a1": "http://api.huilianyi.com",
    "uat": "https://apiuat.huilianyi.com",
    "stage": "https://apistage.huilianyi.com"
}

def download_all_attachments(env, oids, path):
    host = url_map[env]
    token = getToken(host)
    for oid in oids:
        try:
            download_attachment(token, host, oid, path)
        except Exception as e:
            print(f'下载附件 {oid} 时发生异常: {e}')
            time.sleep(10)
            download_attachment(token, host, oid, path)

def download_all_attachments_open_api(env, oids, path):
    host = url_map[env]
    if env == 'a1':
        token = get_open_api_token_for_a1()
    else:
        raise Exception('环境不支持')
    download_attachment_batch_open_api(token, host, oids, path)

if __name__ == "__main__":
    print(get_open_api_token_for_a1())


