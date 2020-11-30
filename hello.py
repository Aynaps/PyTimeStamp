from datetime import datetime,timezone,date
import keyboard
import time

t1 = datetime.now()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("ran the exe")
today = date.today()
filename = "%s.txt" % today
f = open(filename, "a")
f.write("Started stream at : " + current_time + "\n")
f.close()
while True:
    #get keyboard press
    if keyboard.read_key() == "|":
        f = open(filename, "a")
        #get diff from start to now
        diffNow = datetime.now() - now

        #write to file
        f.write("clip at : " + str(diffNow) + "\n")
        time.sleep(1)
        f.close()
