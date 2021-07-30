from datetime import datetime
import threading
import random
import time





def choice_maker():

    now = datetime.now()

    second = str(now.strftime("%S"))
    minute = str(now.strftime("%M"))
    hour = str(now.strftime("%H"))
    print(second)


    if int(minute) % 2 == 0:
        time.sleep(random.randint(60, 540))
        file_object = open("log.txt", "a")
        log_object = open("time_of_log.txt", "a")
        file_object.write("       even          ")
        log_object.write(str(datetime.now()))
        file_object.close()
        log_object.close()
    else:
        time.sleep(random.randint(60, 540))
        file_object = open("log.txt", "a")
        file_object.write("       odd         ")
        log_object = open("time_of_log.txt", "a")
        log_object.write(str(datetime.now()))
        file_object.close()
        log_object.close()

    choice_maker()

choice_maker()
