from tkinter import *
import random
scrplayer = 0
def pedra():
    if ran == 1:
        scrplayer = scrplayer + 0
    elif ran == 2:
        scrplayer = scrplayer - 1
    else:
        scrplayer = scrplayer + 1

def papel():
    if ran == 1:
        scrplayer = scrplayer + 1
    elif ran == 2:
        scrplayer = scrplayer + 0
    else:
        scrplayer = scrplayer - 1

def tesoura():
    if ran == 1:
        scrplayer = scrplayer - 1
    elif ran == 2:
        scrplayer = scrplayer + 1
    else:
        scrplayer = scrplayer + 0

def ppt():
    jan.destroy()
    jan2 = Tk()
    jan2.geometry('720x620')
    jan2.title('pedra papel tesoura')

    botaopedra = Button(jan2, text='pedra', command=pedra)
    while scrplayer < 5:
        ran = random.randint(1, 3)
        botaopedra.pack




    jan2.mainloop()

jan = Tk()
jan.geometry('300x400')
jan.title('pedr papel e tesoura')
botao = Button(jan, text='play', command=ppt)
botao.place(x=130,
            y=250)
jan.mainloop()