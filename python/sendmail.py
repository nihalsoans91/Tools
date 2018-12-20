def sendmail(msg1, subject=""):
    import time
    import datetime
    import smtplib
    from tqdm import tqdm
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("<login email>", "<password here>")
    msgsubject = "Notification - <experiment> [" + str(subject) + " ]"
    msg = "**** Notification - <experiment> *****\nNotification Sent at : "
    msg += str(datetime.datetime.now()) + "\n"
    msg += msg1
    message = 'Subject: {}\n\n{}'.format(msgsubject, msg)
    print("Sending Notification")
    server.sendmail("< From Email>", "<To Email>", message)
    for i in tqdm(range(100)):
        time.sleep(0.005)
        pass
    print("Notification Sent")
    server.quit()
