from tkinter import *
import webbrowser

def video():
    webbrowser.open('https://youtu.be/k_ESAqyimR4')

def newjan():
    jan.destroy()
    jan2 = Tk()

    jan2.geometry('1405x789')
    img2 = PhotoImage(master=jan2, )
    label1 = Label(jan2,
                  image=img2)

    label1.pack()
    botao3 = Button(jan2, text='play', command=video)
    botao3.place(x=650,
                 y=650)

    jan2.mainloop()


jan = Tk()
jan.geometry('350x600')

botao1 = Button(jan, text='sair', command=quit)
botao2 = Button(jan, text='teste', command=newjan)

botao1.place(x=150,
             y=400,
             width=60,
             height=30)
botao2.place(x=50,
             y=100)