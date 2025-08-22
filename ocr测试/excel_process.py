import time
import pandas as pd
import os
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from download_atta_hly import download_attachment, getToken, url_map, download_all_attachments_open_api


def download_attachments_from_excel(excel_path, env, oid_column, save_path):
    # 读取excel
    df = pd.read_csv(excel_path)
    # 获取token
    host = url_map[env]
    token = getToken(host)
    # 收集所有oid
    oids = []
    for idx, row in df.iterrows():
        attachment_oid = str(row[oid_column]).strip()
        if attachment_oid:  # 排除空值
            oids.append(attachment_oid)

    download_all_attachments_open_api(env, oids, save_path)
    

if __name__ == "__main__":
    # 示例用法
    excel_path = r'C:\Users\lijiang\Downloads\2025-07-23-18-28-02_EXPORT_CSV_20397630_209\2025-07-23-18-28-02_EXPORT_CSV_20397630_287_0.csv'
    env = 'a1'
    oid_column = 'slicing_attachment_oid'
    save_path = r'C:\Users\lijiang\Downloads\ocr_res_2\res_excel'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    download_attachments_from_excel(excel_path, env, oid_column, save_path)
