import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("swathik.8586@gmail.com", "swathik.123")
msg = "hi!"
server.sendmail("swathik.8586@gmail.com", "vidhyabidrakote2@gmail.com", msg)
print("success")
server.quit()
