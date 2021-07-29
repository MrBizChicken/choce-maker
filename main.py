from datetime import datetime







def choice_maker():
    now = datetime.now()
    second = str(now.strftime("%S"))
    print(second)
    if int(second) == int(second) + 9 * int(second):



        if int(second) // 2 == 0:
            file_object = open("log.txt", "a")
            file_object.write("       even          ")
            file_object.close()
        else:
            file_object = open("log.txt", "a")
            file_object.write("       odd         ")
            file_object.close()

while True:
    choice_maker()
