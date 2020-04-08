import smtplib
from email.mime.text import MIMEText

mailto_list = ["shirleyaizeng@sina.com"]
mail_host = "smtp.sina.com"
mail_user = "shirleyaizeng@sina.com"
mail_pass = "stkm99cp9"

msg = MIMEText('提交作业')
msg['Subject'] = '提交CS作业时间'
msg['From'] = mail_user
msg['To'] = ";".join(mailto_list)


try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user,mail_pass)
    s.sendmail(mail_user, mailto_list, msg.as_string())
    s.close()
    print("成功")
    
except Exception as e:
    print(str(e))
    print("发送失败")
