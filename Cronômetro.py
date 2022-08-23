from tkinter import *

corbg = "#242323"

main = Tk()
main.title("CRONÔMETRO")
main.geometry("500x230+700+300")
main.config(bg = corbg)
main.resizable(width = False, height = False)


tempo = "00:00:00"
count = -3
cond = False

def time():
    global tempo
    global count

    if cond == True:
        if count <= -1:
            inicio = "Começando em " + str(count)[-1:]
            crono["text"] = inicio
            crono["font"] = "Courier 36 bold"
        else:
            crono["font"] = "Courier 70 bold"
            hr, min, sec = map(int, tempo.split(":"))
            sec = count
            
            if sec == 59:
                count = -1
                min += 1
            
            if min == 59:
                min = 0
                hr += 1

            sec = str(0) + str(sec)
            min = str(0) + str(min)
            hr = str(0) + str(hr)

            crono["text"] = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])
            tempo = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])
            
        crono.after(1000, time)
        count += 1
        inic["state"] = "disabled"

def start():
    global cond
    cond = True
    time()

def pause():
    global cond
    cond = False
    inic["state"] = "active"
    time()

def resett():
    global tempo, count
    count = 0
    crono["text"] = "00:00:00"
    
    
crono = Label(main, text= tempo, font=("Courier 70 bold"), bg=corbg, fg="#c21b2c")
crono.place(x=25,y=20)


inic = Button(main, text="Iniciar", command = start, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
inic.place(x=25, y= 160)

pausa = Button(main, text="Pausar", command = pause, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
pausa.place(x=207, y= 160)

reset = Button(main, text="Resetar", command = resett, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
reset.place(x=370, y= 160)




main.mainloop()