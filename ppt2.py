from tkinter import *
import random

class pptFunctions():
    def choicePC(self):
        self.choice_PC = random.randint(1, 3)

class allPages(pptFunctions):
    def __init__(self):
        self.page_All = Tk()
        self.page_All.geometry('600x700')
        self.page_All.config(background='gray')
        self.page_All.resizable(0, 0)
        self.page_All.title('Pedra, papel e tesoura')


        self.button_First_Page()

        self.page_All.mainloop()
    
    def button_First_Page(self):

        self.play_First_Page_Button = Button(
            self.page_All, 
            text='P L A Y',
            command=self.game_Page,
            width=20,
        )
        self.play_First_Page_Button.place(x=220, y=600)

    def game_Page(self):

        self.play_First_Page_Button.destroy()

        self.button_Game_Page()

    def button_Game_Page(self):

        self.rock_Button = Button(
            self.page_All, 
            text='P E D R A', 
            command=quit,
            width=18,
            height=7
        )
        self.rock_Button.place(x=20, y=30)

        self.paper_Button = Button(
            self.page_All, 
            text='P A P E L', 
            command=quit,
            width=18,
            height=7
        )
        self.paper_Button.place(x=20, y=230)

        self.cramp_Button = Button(
            self.page_All, 
            text='T E S O U R A', 
            command=quit,
            width=18,
            height=7
        )
        self.cramp_Button.place(x=20, y=430)

    def label_Game_Page(self):
        pass






allPages()
