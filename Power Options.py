#POWER options
import os
import time
import ctypes

#lock
def lock():
    ctypes.windll.user32.LockWorkStation()
#log off
def log_off():
    ctypes.windll.user32.ExitWindowsEx(0, 1)
#shutdown
def shutdown():
    os.system("shutdown /s /t 0")
# restart
def restart():
    os.system("shutdown /r /t 0")
#sleep
def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

x=int(input('''1-lock
2-log off
3-shutdown
4-restart
5-sleep\n'''))
if x==1:
    try:
        y=int(input('time(seconds):'))
        for z in range(y)[::-1]:
            time.sleep(1)
            print(x)
        lock()
    except:
        print("Not a number")
elif x==2:
    try:
        y=int(input('time(seconds):'))
        for z in range(y)[::-1]:
            time.sleep(1)
            print(x)
        log_off()
    except:
        print("Not a number")
elif x==3:
    try:
        y=int(input('time(seconds):'))
        for z in range(y)[::-1]:
            time.sleep(1)
            print(x)
        shutdown()
    except:
        print("Not a number")
elif x==4:
    try:
        y=int(input('time(seconds):'))
        for z in range(y)[::-1]:
            time.sleep(1)
            print(x)
        sleep()
    except:
        print("Not a number")
else:
    quit()
