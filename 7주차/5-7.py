import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
print(smtp.login("youjinv@g.skku.edu","**********"))
smtp.send.message()
smtp.quit()