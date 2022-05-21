import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login('split777hisense@gmail.com', 'Split777hisense159')
server.sendmail('split777hisense@gmail.com', 'dsannikov@gmail.com', 'Mail sent from Python')
print('Mail sent')

# ===============================================================
# <form action=”mailto:contact@yourdomain.com”
# method=”POST”
# enctype=”multipart/form-data”
# name=”EmailForm”>
# Name:<br>
# <input type=”text” size=”19″ name=”ContactName”><br><br>
# Message:<br> <textarea name=”ContactCommentt” rows=”6″ cols=”20″>
# </textarea><br><br> <input type=”submit” value=”Submit”> </form>