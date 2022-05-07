from tkinter import *

class pageAll():
    def __init__(self):
        self.page_All = Tk()
        self.page_All.geometry('600x700')
        self.page_All.config(background='gray')
        self.page_All.resizable(0, 0)

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
            command=quit
        )
        self.rock_Button.pack()



class pptFunctions():
    pass


pageAll()
