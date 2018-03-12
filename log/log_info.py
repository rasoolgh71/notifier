import datetime

def log_info():
    file = open('info.log', 'a')
    message = " " + "user\t"+ "\tclick on link to page book  "
    time = datetime.datetime.now()
    log = time.strftime("%Y-%m-%d %H:%M:%S\t:") + message
    file.write(log)
    file.write("\n")
    file.close()
