from datetime import datetime
import threading





def choice_maker():
    now = datetime.now()
    second = str(now.strftime("%S"))
    print(second)
    if int(second) // 2 == 0:
        threading.Timer(9.0, choice_maker).start()
        file_object = open("log.txt", "a")
        file_object.write("       even          ")
        file_object.close()
    else:
        threading.Timer(9.0, choice_maker).start()
        file_object = open("log.txt", "a")
        file_object.write("       odd         ")
        file_object.close()

while True:
    choice_maker()
