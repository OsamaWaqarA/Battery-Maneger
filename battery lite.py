import psutil, pygame, playsound

while True:
    pygame.time.delay(50000)
    if psutil.sensors_battery().percent < 25 and psutil.sensors_battery().power_plugged == False:
        playsound.playsound('C:\\Users\wabal\Python Data Storage\Data centre\Beep.mp3')
        playsound.playsound("C:\\Users\wabal\Python Data Storage\Data centre\Battery low.mp3")
    if psutil.sensors_battery().percent > 85 and psutil.sensors_battery().power_plugged == True:
        playsound.playsound('C:\\Users\wabal\Python Data Storage\Data centre\Beep.mp3')
        playsound.playsound("C:\\Users\wabal\Python Data Storage\Data centre\80 per.mp3")
