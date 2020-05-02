import smtplib  # to connect smtp server
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

#
# mail = MIMEMultipart()
# mail['From'] = 'hukukisler@gmail.com'
# mail['To'] = 'mistafagunes@gmail.com'
# mail['Subject'] = 'Smtp mail gonderme'
#
# mesaj = '''
#
# Smtp ile mail gonderiyorum.
#
# Mustafa Gunes
#
# '''
#
# mesaj_body = MIMEText(mesaj, 'plain')
#
# mail.attach(mesaj_body)
#
# try:
#     # param 1: hangi smtp server'a baglanmak istedigimizi belirtiyoruz
#     # param 2: bu smtp nin hangi portuna baglanmak istedigimizi belirtiyoruz
#     send_mail = smtplib.SMTP('smtp.gmail.com', 587)
#
#     send_mail.ehlo()  # SMTP serverına kendimizi tanıtıyoruz.
#
#     send_mail.starttls()  # Adresimizin ve Parolamızın şifrelenmesi için gerekli
#
#     send_mail.login('hukukisler@gmail.com', 'hukuktevkil')  # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı giriyoruz.
#
#     send_mail.send(mail['From'], mail['To'], mail.as_string())  # Mailimizi gönderiyoruz.
#
#     print("Mail başarıyla gönderildi....")
#
#     send_mail.close()
#
# except smtplib.SMTPResponseException:
#     print(smtplib.SMTPResponseException)
#     sys.stderr.write('something went wrong')


mail_content = '''
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''

# The mail addresses and password

sender_address = 'mistafagunes@gmail.com'
sender_pass = '198907Mg'
receiver_address = 'hukukisler@gmail.com'

# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'  # The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
