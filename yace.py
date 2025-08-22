import smtplib
import threading
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import os

# 配置参数（需根据实际邮箱修改）
SMTP_SERVER = "smtp.163.com"   # 阿里云企业邮箱服务器
SMTP_PORT = 25                     # SMTP端口
SENDER_EMAIL = "lj2293785363@163.com"  # 发件人邮箱
SENDER_PASSWORD = "PKV5dkJY9ptKfHcE"      # 发件人密码
RECEIVER_EMAILS = [                 # 收件人列表
    "ljceshi3@fp.huilianyi.com",
    "test12220000000@fp.huilianyi.com", 
    "test15773250001@fp.huilianyi.com",
    "test14082978888@fp.huilianyi.com",
    "test12220000002@fp.huilianyi.com",
    "test12220000001@fp.huilianyi.com",
    "test12220000003@fp.huilianyi.com",
    "testnull@fp.huilianyi.com",
    "test17603052199@fp.huilianyi.com",
    "test14003180002@fp.huilianyi.com",
    "test15773253003@fp.huilianyi.com",
    "test17640483748@fp.huilianyi.com",
    "ljtest@fp.huilianyi.com"
]
MAIL_CONTENT = "这是一封压测邮件"
TOTAL_MESSAGES = 10          # 总发送邮件数
CONCURRENCY_LEVELS = [10,50,100]      # 三个并发级别
ATTACHMENT_PATH = r"C:\Users\lijiang\Downloads\Snipaste_2025-06-17_16-41-30.png"

timestamp = time.strftime("%Y%m%d_%H%M%S")
message_count = 0
message_count_lock = threading.Lock()
current_level = 0

class EmailSender(threading.Thread):
    def __init__(self, thread_id):
        super().__init__()
        self.thread_id = thread_id
        self.success_count = 0
        self.failure_count = 0

    def run(self):
        messages_per_thread = TOTAL_MESSAGES // CONCURRENCY_LEVELS[current_level]
        for _ in range(messages_per_thread):
            try:
                with message_count_lock:
                    global message_count
                    message_count += 1
                    current_count = message_count
                subject = f"{timestamp}_{current_count}"
                
                # 随机选择一个收件人
                receiver = random.choice(RECEIVER_EMAILS)
                
                # 创建带附件的邮件
                msg = MIMEMultipart()
                msg['From'] = Header(SENDER_EMAIL)
                msg['To'] = Header(receiver)
                msg['Subject'] = Header(subject, 'utf-8')

                # 添加正文
                text_part = MIMEText(MAIL_CONTENT, 'plain', 'utf-8')
                msg.attach(text_part)

                # 添加附件
                with open(ATTACHMENT_PATH, 'rb') as f:
                    attachment = MIMEApplication(f.read())
                    attachment.add_header('Content-Disposition', 'attachment', 
                                       filename=os.path.basename(ATTACHMENT_PATH))
                    msg.attach(attachment)

                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()  # 启用TLS加密
                    server.login(SENDER_EMAIL, SENDER_PASSWORD)
                    server.sendmail(SENDER_EMAIL, [receiver], msg.as_string())
                    # time.sleep(2)  # 等待2秒
                self.success_count += 1
            except Exception as e:
                print(f"线程{self.thread_id}发送失败: {str(e)}")
                self.failure_count += 1

def run_load_test(concurrency):
    threads = []
    for i in range(concurrency):
        thread = EmailSender(i)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_success = sum(t.success_count for t in threads)
    total_failure = sum(t.failure_count for t in threads)
    return total_success, total_failure

if __name__ == "__main__":
    index  = 0
    for level in [CONCURRENCY_LEVELS[0]]:
        current_level = index
        index += 1
        print(f"\n开始压测 - 并发级别: {level}")
        print(f"发送总数: {TOTAL_MESSAGES}")
        start_time = time.time()
        success, failure = run_load_test(level)
        duration = time.time() - start_time
        
        print(f"总耗时: {duration:.2f}秒")
        print(f"成功发送: {success}封")
        print(f"失败发送: {failure}封")
        print(f"成功率: {success/(success+failure)*100:.2f}%")
