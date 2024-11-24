import psutil,pygame,playsound,subprocess
pygame.init()
y = 0
win = pygame.display.set_mode((1330,710))
pygame.display.set_caption("System EYE")
pygame.mouse.set_visible(1)
font = pygame.font.SysFont('Calibri ',20)
afont = pygame.font.SysFont('Bell MT',50)
entry1 = afont.render("O",True,(255,140,0))
entry2 = afont.render("s",True,(0,255,255))
entry3 = afont.render("a",True,(145,50,200))
entry4 = afont.render("m",True,(10,140,5))
entry5 = afont.render("a",True,(255,255,0))
entry = afont.render("'s Tech.",True,(255,0,0))
bs = pygame.mixer.Sound('C:\Python Data Storage\Data centre\Beep.mp3')
#intro
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    win.fill((0,0,0))
    if y > 0:
        if y < 720:
            win.blit(entry2,(645,333))
            pygame.display.update()
            pygame.time.delay(1)
            win.fill((0,0,0))
            pygame.draw.rect(win,((255,0,0)),(0,0,2000,y),0)
            pygame.display.update()
            win.fill((0,0,255))
            pygame.display.update()
            win.fill((0,0,0))
            pygame.display.update()
            win.blit(entry1,(620,335))
            pygame.display.update()
            pygame.time.delay(1)
        if y > 720:
            if (y - 720) < 1500:
                y + 15
                win.blit(entry4,(683,333))
                win.blit(entry2,(645,333))
                pygame.display.update()
                pygame.time.delay(1)
                win.fill((0,0,255))
                pygame.display.update()
                win.fill((0,0,0))
                pygame.display.update()
                pygame.draw.rect(win,((0,255,0)),(0,0,y - 720 ,2000),0)
                pygame.display.update()
                win.fill((0,0,0))
                win.blit(entry3,(665,333))
                win.blit(entry1,(620,335))
                pygame.display.update()
                pygame.time.delay(1)

            else:
                win.fill((50,50,50))
                pygame.display.update()
                win.blit(entry1,(620,335))
                pygame.time.delay(100)
                pygame.display.update()
                win.blit(entry2,(645,333))
                pygame.time.delay(100)
                pygame.display.update()
                win.blit(entry3,(665,333))
                pygame.time.delay(100)
                pygame.display.update()
                win.blit(entry4,(683,333))
                pygame.time.delay(100)
                pygame.display.update()
                win.blit(entry5,(712,333))
                pygame.time.delay(200)
                pygame.display.update()
                pygame.time.delay(250)
                win.blit(entry,(730,333))
                pygame.display.update()
                pygame.time.delay(1000)
                break
                
            
        
    y += 25
    pygame.display.update()
    limit = 0
    fps = 0
    cfps = 0
    olddate = 0
    plug = False
    timeleft = 0
    percent = 0
    saver = False
    T1 = 0
    T2 = 0
    inter = False
    select = False
    read = []
    charge = 0
    carry = int(0)
    workey = int(0)
    run = False
    shut_time = int(0)
    control = int(20)
    batch = int(0)
    file = open("C:\Python Data Storage\Data centre\Battery time.txt","r")
    ring = int(0)
    box = [False,False,False]
    done = False
    per = 90
    h = 0
    m = 0
    need = 0
    listen = ""
    speak = False
    mpass = False
    data = False
    rule = False
    typ = ""
    buff = 0
    wait = 0
    text_1 = font.render("Time Select",True,(0,255,0))
    dshow = font.render("Done",True,(0,255,0))
    shut_time = int(file.readline())
    if shut_time == 0:
        shut_time = 23
    else:
        shut_time -= 1
    file.close()
win = pygame.display.set_mode((600,100))
while True:
    ring += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playsound.playsound("C:\Python Data Storage\Data centre\mean.mp3")
            #pygame.quit()
        if event.type == pygame.KEYDOWN and speak == False:
            if event.unicode != "":
                typ = typ + event.unicode
            if event.unicode == "c":
                typ = ""
        if event.type == pygame.KEYDOWN and speak == True:
            if event.key == pygame.K_RETURN:
                if box[0] == True and int(listen) <= 24:
                    h = int(listen)
                if box[1] == True and int(listen) <= 59:
                    m = int(listen)
                if box[2] == True and int(listen) >= 25 and int(listen) <= 100:
                    per = int(listen)

                box[0] = False
                box[1] = False
                box[2] = False
                speak = False
                listen = str("")
                pygame.mouse.set_visible(1)
            if  "0" in event.unicode or "1" in event.unicode or  "2" in event.unicode or "3" in event.unicode or "4" in event.unicode or "5" in event.unicode or "6" in event.unicode or "7" in event.unicode or "8" in event.unicode or "9" in event.unicode:
                if len(listen) == 1 and listen == "0":
                    listen = event.unicode
                elif len(listen) < 2:
                    listen += event.unicode
            if event.key == pygame.K_BACKSPACE :
                listen = listen[0:-1]
                if len(listen) == 0:
                    listen = "0"
    if len(typ) > 5:
        typ = ""
    if rule == False:
        if typ == "false":
            rule = True
            buff = 0
            wait = 0
            typ = ""
        win.fill((10,0,0))
    else:
        if typ == "ture":
            rule = False
            typ = ""
        if time != buff:
            buff = time
            wait += 1
        if wait >= 120:
            rule = False
        win.fill((255,0,0))
        saver = False
    
    cpu = psutil.cpu_percent()
    try :  
        battery = psutil.sensors_battery()
        timeleft = int(battery.secsleft/60)
        percent = int(battery.percent)
        if battery.power_plugged == False:
            plug = False
        else:
            plug = True
    except AttributeError:
        plug = True
        timeleft = 123456

    pygame.time.delay(limit)
    pygame.time.delay(100)
    
    click1,click2,click3 = pygame.mouse.get_pressed()
    if click1 == True:
        pos = pygame.mouse.get_pos()
        line = str(pos)
        coma = int(line.find(","))
        fbracket = int(line.find("("))
        lbracket = int(line.find(")"))
        x = int(line[fbracket + 1:coma])
        y = int(line[coma+2:lbracket])
        pygame.time.delay(100)
        if x >= 10 and x <= 110 and y >= 50 and y <= 75:
            box [0] = True
            listen = str(h)
        elif x >= 260 and x <= 360 and y >= 50 and y <= 75:
            box[1] = True
            listen = str(m)
        elif x >= 460 and x <= 560 and y >= 50 and y <= 75:
            box[2] = True
            listen = str(per)
        elif x >= 150 and x <= 200 and y>= 50 and y <= 75:
            done = True
            

    if timeleft == 0:
        show = font.render("Battery percent = " + str(percent) + " battery timeleft = " + "INFINITY " + " CPU percent = " +str(cpu),True,(255,255,255))
    elif timeleft == 123456:
        show = font.render("Last Know Battery percent = " + str(percent) + " No Battery " +  "CPU percent = "  +str(cpu),True,(0,255,0))
    else:
        show = font.render("Battery percent = " + str(percent) + " battery timeleft = " + str(timeleft) + " CPU percent = " +str(cpu),True,(255,255,255))

    file = open("C:\Python Data Storage\Data centre\present.txt","w")
    file.write(str("Yes"))
    file.close()
        
    if done == False:
        if select == False:
            pygame.draw.rect(win,((255,255,255)),(260,50,100,25),1)
            win.blit(text_1,((260,50)))
            if box[1] == True:
                box[0] = False
                box[1] = False
                box[2] = False
                select = True
        else:
            lshow = font.render(str(listen),True,((255,0,0)))
            hshow = font.render(str(h),True,((255,255,255)))
            mshow = font.render(str(m),True,((255,255,255)))
            pershow = font.render(str(per),True,((255,255,255)))
            pygame.draw.rect(win,((255,255,255)),(10,50,100,25),1)
            pygame.draw.rect(win,((255,255,255)),(260,50,100,25),1)
            pygame.draw.rect(win,((255,255,255)),(460,50,100,25),1)
            pygame.draw.rect(win,((255,255,255)),(150,50,50,25),1)
            win.blit(dshow,((150,50)))
            if box[0] == True:
                win.blit(lshow,((10,50)))
                speak = True
            else:
                win.blit(hshow,((10,50)))
            if box[1] == True:
                win.blit(lshow,((260,50)))
                speak = True
            else:
                win.blit(mshow,((260,50)))
            if box[2] == True:
                win.blit(lshow,((460,50)))
                speak = True
            else:
                win.blit(pershow,((460,50)))
    else:
        if h >= date and h <= (date+1) and mpass == False:
            if m <= time or h == date:
                mpass = True
                #if per > 70 and m >= 10:
                 #   m -= 10
                #elif per > 70 and m < 10 and h != 0:
                 #   h -= 1
                  #  m += 50
                #if per < 70 and m >= 5:
                 #   m -= 5
                #elif per < 70 and m < 5 and h != 0:
                 #   h -= 1
                  #  m += 55
        if mpass == True:
            if per == percent and h == date and (m - time) <= 15:
                playsound.playsound("C:\Python Data Storage\Data centre\Target com.mp3")
                mpass = False
                select = False
                done = False
                run = []
                charge = 0
                m = 0
                h = 0
            if h == date and m == time and per != percent:
                playsound.playsound("C:\Python Data Storage\Data centre\Fail.mp3")
                mpass = False
                select = False
                done = False
                run = []
                charge = 0
                m = 0
                h = 0
            if per > percent:
                need = per - percent
                if charge == 0:
                    read = []
                    run = True
                    file = open("C:\Python Data Storage\Data centre\charge7525.txt","r")
                    while run:
                        read.append(file.readline())
                        if "EOF" in read or "EOF\n" in read:
                            run = False
                    file.close()
                    for i in range (0,len(read)):
                        if "\n" in read[i]:
                            read[i] = read[i][0:len(read[i])-1]
                    charge = 0
                    for i in range (0,(len(read)-1)):
                        charge += int(read[i])
                    charge = charge/(len(read)-2)
                    charge = charge / 60#change to min from second
                    charge = int(charge/50)#time per percent!
                if h == date:
                    if (need*charge) >= m - time and plug == False:
                        playsound.playsound("C:\Python Data Storage\Data centre\Battery low.mp3")
                        
                else:
                    if (need*charge) >= (m - time)+60 and plug == False:
                        playsound.playsound("C:\Python Data Storage\Data centre\Battery low.mp3")

            if per < percent:
                need = percent - per
                if h == date and timeleft <= 500:
                    if int(need*(timeleft/(percent))) >= m - time and plug == True:
                        playsound.playsound("C:\Python Data Storage\Data centre\80 per.mp3")
                    
    win.blit(show,((10,10)))
    pygame.display.update()
    
    import time
    time = time.ctime()
    T1 = int(time[17:19])#sec
    date = int(time[11:13])#hours
    time = int(time[14:16])#mintues
    if T2 != T1 :
        if inter == True and plug == True:
            carry += 1
        if inter == False and plug == False and carry != 0:
            file = open("C:\Python Data Storage\Data centre\charge7525.txt","r")
            run = True
            read = []
            while run:
                read.append(file.readline())
                if "EOF" in read or "EOF\n" in read:
                    run = False
            file.close()
            read[len(read)-1] = str(carry)
            carry = int(carry)
            read.append("EOF")
            file = open("C:\Python Data Storage\Data centre\charge7525.txt","w")
            for i in range (0,len(read)):
                if "\n" in read[i]:
                    read[i] = read[i][0:len(read[i])-1]
                file.write(str(read[i]))
                file.write("\n")
            read = []
            carry = int(0)
            file.close()
        elif inter == True and plug == False and carry != 0:
            inter = False
            carry = 0


            
        if data == True and plug == False:
            workey += 1
        if data == False and plug == True and workey != 0:
            file = open("C:\Python Data Storage\Data centre\window fail.txt","r")
            run = True
            read = []
            while run:
                read.append(file.readline())
                if "EOF" in read or "EOF\n" in read:
                    run = False
            file.close()
            read[len(read)-1] = str(workey)
            workey = int(workey)
            read.append("EOF")
            file = open("C:\Python Data Storage\Data centre\window fail.txt","w")
            for i in range (0,len(read)):
                if "\n" in read[i]:
                    read[i] = read[i][0:len(read[i])-1]
                file.write(str(read[i]))
                file.write("\n")
            read = []
            workey = int(0)
            file.close()
        elif data == True and plug == True and workey != 0:
            workey = 0
            data = False

        fps = cfps
        T2 = T1
        cfps = 0
    else:
        cfps += 1
    if fps > 2:
        limit += 1
    if fps < 2:
        limit -= 1
        
    
    if olddate != date and (date >= 21 or (date >= 0 and date <= 2)):
        olddate = date
        file = open("C:\Python Data Storage\Data centre\Battery time.txt","w")
        file.write(str(date))
        file.close()

    if percent <= 15 and plug == False:
        control = 0
        batch = 0
        limit = 0
        playsound.playsound("C:\Python Data Storage\Data centre\low 15.mp3")
    else:
        control = 20
        
    if (saver == False or cpu > 60 )and ring >= control:
        ring = 0
        if percent <= 25 and plug == False:
            if batch <= 10:
                bs.play()
                pygame.time.delay(1600)
                playsound.playsound("C:\Python Data Storage\Data centre\Battery low.mp3")
            elif batch >= 15:
                batch = 0
            batch += 1
            inter = True
            data = False
        elif percent >= 75 and plug == True and percent < 95 and mpass == False:
            if batch <= 5:
                bs.play()
                pygame.time.delay(1600)
                playsound.playsound("C:\Python Data Storage\Data centre\80 per.mp3")
            elif batch >= 20:
                batch = 0
            batch += 1
            inter = False
            data = True
        elif percent >= 95 and plug == True and mpass == False:
            playsound.playsound("C:\Python Data Storage\Data centre\Battery full.mp3")
        else:
            batch = 0

            
    if (saver == True and cpu < 60) and ring >= control:
        ring = 0
        if percent <= 45 and plug == False:
            if batch <= 5:
                bs.play()
                pygame.time.delay(1600)
                playsound.playsound("C:\Python Data Storage\Data centre\Battery low.mp3")
            elif batch >= 15:
                batch = 0
            batch += 1
        elif percent >= 55 and plug == True and percent < 95:
            if batch <= 5:
                bs.play()
                pygame.time.delay(1600)
                playsound.playsound("C:\Python Data Storage\Data centre\80 per.mp3")
            elif batch >= 20:
                batch = 0
            batch += 1
        elif percent >= 95 and plug == True:
            playsound.playsound("C:\Python Data Storage\Data centre\Battery full.mp3")
        else:
            batch = 0
            
    if (date >= 21 or (date >= 0 and date <= 2)):
        if shut_time < 21:
            if date == 0 or date == 1 or date == 2:
                if date >= shut_time:
                    saver = True
        else:
            if date >= shut_time:
                saver = True
            if shut_time >= 21:
                if date == 0 or date == 1 or date == 2:
                    saver = True
    else:
        saver = False

