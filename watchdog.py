import datetime
import time
import os
from termcolor import colored
import colorama

while True:
    last_line = None
    time_now = datetime.datetime.now ()

    for line in open("config.log", "r"):
        last_line = line
		
    print ('')
    print (time_now.strftime('Sys last time: ' + "%H:%M:%S"))
    print ('log last time: ' + last_line)
    tm_log = last_line[3:5]
    tm_now = time_now.strftime("%M")
    print ('time log: ' + tm_log)
    print ('time now: ' + tm_now)
    check = int(tm_now) - int(tm_log)
    print ('difference: ' + str(check))
    print ('')
	
    if check >= 2:
        print('!!! РАСХОЖДЕНИЕ ПО ВРЕМЕНИ !!!')
        print('--- ВЕРОЯТНО ЗАВИСАНИЕ ПРОЦЕССА ---')
		
        os.system ("taskkill /f /im  bot.exe")
        print('--- ПРОЦЕСС ОСТАНОВЛЕН ---')
        #os.system(r'C:/Users/trogwar/Desktop/dist_0.1.3.2/bot.exe')
        #print('ПРОЦЕСС ЗАПУЩЕН')
    else:
        print('--- ПРОЦЕСС АКТИВЕН ---')
    time.sleep (30)
