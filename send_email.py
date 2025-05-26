import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(to_email, subject, content):
    # 邮箱服务器配置
    mail_host = "smtp.qq.com"
    mail_port = 465  # QQ邮箱使用SSL，端口号为465

    # 发件人邮箱账号
    mail_user = "2293785363@qq.com"
    # 发件人邮箱授权码，非QQ邮箱密码
    mail_pass = "zbufdijwimesdjdi"

    try:
        # 创建邮件内容
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = Header(mail_user)
        msg['To'] = Header(to_email)
        msg['Subject'] = Header(subject)

        # 使用SMTP_SSL连接邮箱服务器
        with smtplib.SMTP_SSL(mail_host, mail_port) as smtp:
            smtp.login(mail_user, mail_pass)
            smtp.sendmail(mail_user, to_email, msg.as_string())
        
        print("邮件发送成功")
    except Exception as e:
        return
        
# 使用示例
if __name__ == "__main__":
    send_email("2293785363@qq.com", "测试邮件", "这是一封测试邮件内容")