import base64
import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formatdate

def sendmail():
    main_text = "complete scrap data from website and export to CSVbuddy "
    charset = "utf-8"
    if charset == "utf-8":
        msg = MIMEText(main_text, "plain", charset)
    elif charset == "iso-2022-jp":
        msg = MIMEText(base64.b64encode(main_text.encode(charset, "ignore")), "plain", charset)


    msg.replace_header("Content-Transfer-Encoding", "base64")
    msg["Subject"] = "!!COMPLETE EXPORT CSV!!"
    msg["From"] = "aimanhaziq0978@gmail.com"
    #msg["To"] = "danishdnial1998@gmail.com"
    msg["To"] = "aimanhaziq0978@gmail.com"
    msg["Date"] = formatdate(None,True)


    host = "smtp.gmail.com"
    nego_combo = ("ssl", 465) 

    if nego_combo[0] == "no-encrypt":
        smtpclient = smtplib.SMTP(host, nego_combo[1], timeout=10)
    elif nego_combo[0] == "starttls":
        smtpclient = smtplib.SMTP(host, nego_combo[1], timeout=10)
        smtpclient.ehlo()
        smtpclient.starttls()
        smtpclient.ehlo()
    elif nego_combo[0] == "ssl":
        context = ssl.create_default_context()
        smtpclient = smtplib.SMTP_SSL(host, nego_combo[1], timeout=10, context=context)
    smtpclient.set_debuglevel(2) 


    username = "aimanhaziq0978@gmail.com"
    password = "uiegevqstlnqwadm"
    smtpclient.login(username, password)


    smtpclient.send_message(msg)
    smtpclient.quit()

if __name__ == "__main__":
    sendmail()
