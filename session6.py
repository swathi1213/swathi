import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("vidhyabidrakote2@gmail.com", "chiru243")
msg ="hi!"
server.sendmail("vidhyabidrakote2@gmail.com", "swathik.8586@gmail.com", msg)
print("success")
server.quit()
