from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'kopjack@163.com'
    receivers = ['fanhw1@lenovo.com', 'fanhwid@gmail.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('罗浩', 'utf-8')
    message['Subject'] = Header('国庆中秋放假安排', 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'wfpwus')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成！')


if __name__ == "__main__":
    main()
