import smtplib
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Micrpophone() as source:
        print('listening.....')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)

except:
    pass

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('sender_email_address','sender_password')
    server.sendmail('sender_email_address',
                    'receiver_email_address',
                    'Hi bro how r u man.')