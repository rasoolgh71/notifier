import string
#from .models import Used
from django.utils.crypto import get_random_string
from django.shortcuts import HttpResponse
from celery import task, shared_task
import subprocess
import smtplib
import time
from datetime import datetime
import os


def send_email():
    gmail_user = 'rasoolghanna@gmail.com'
    gmail_password = ''
    send_from = gmail_user
    to = ['javani125@gmail.com']
    # to = input("please enter email to send:")
    subject = "loggigng"
    body = "the loggigng not change modify"
    email_text = """\
               From: %s\n
               To: %s
               Subject: %s

              %s
               """ % (send_from, (to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(send_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')

def check_log():
    get_file = ('/home/parspooyesh-kashan/djangocode/notifier/info.log') #get path file
    file_mod_time = (os.path.getmtime(get_file))  #file mode time
    #print("file_mod_time:", file_mod_time)
    time_now=datetime.now()
    mktime_now = round(time.mktime(time_now.timetuple()))
    diff = round((mktime_now - file_mod_time)/60)
    print("diff:", diff)
    if(diff>5 and diff<10):
        send_email()

    elif(diff>10):
        send_email()
    else:
        pass


@shared_task(name="repeat_cheakfive")
def repeat_cheak_fiveminuts():
    check_log()
    return '{} repeat  in five minutes!'

@shared_task(name="repeat_cheaksixty")
def repeat_cheak_sixtyminuts():
    check_log()
    return '{} repeat  in sexty minutes!'