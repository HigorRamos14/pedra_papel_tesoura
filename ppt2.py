from tkinter import *
import random

class pptFunctions():

    def choice_PC(self):
        
        self.random_Choice_PC = random.randint(1, 3)

class allPages(pptFunctions):

    def __init__(self):

        self.score_Pc = 0
        self.score_client = 0

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
        self.label_Game_Page()

    def button_Game_Page(self):

        self.rock_Button = Button(
            self.page_All, 
            text='P E D R A', 
            command=self.user_Rock,
            width=18,
            height=7
        )
        self.paper_Button = Button(
            self.page_All, 
            text='P A P E L', 
            command=self.user_Paper,
            width=18,
            height=7
        )
        self.cramp_Button = Button(
            self.page_All, 
            text='T E S O U R A', 
            command=self.user_Cramp,
            width=18,
            height=7
        )
        
        self.rock_Button.place(x=20, y=30)
        self.paper_Button.place(x=20, y=230)
        self.cramp_Button.place(x=20, y=430)

    def label_Game_Page(self):

        self.choice_PC_label = Label(
            self.page_All,
            text='',
            width=18,
            height=7,
            background='gray'
            )
        self.score_Label = Label(
            text='YOU {} X {} PC'.format(self.score_client, self.score_Pc),
            background='gray'
            )

        self.score_Label.place(x=210, y=580)
        self.choice_PC_label.place(x=410, y=230)

    def user_Rock(self):
    
        self.choice_PC()
        if self.random_Choice_PC == 1:

            self.choice_PC_label.destroy()
            
            self.choice_PC_label = Label(
                self.page_All,
                text='PEDRA',
                width=18,
                height=7,
            )

            self.choice_PC_label.place(x=410, y=230)
        
        elif self.random_Choice_PC == 2:

            self.score_Pc = self.score_Pc + 1

            self.choice_PC_label.destroy()
            self.score_Label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='PAPEL',
                width=18,
                height=7,
            )
            self.score_Label = Label(
            text='YOU {} X {} PC'.format(self.score_client, self.score_Pc),
            background='gray'
            )

            self.score_Label.place(x=210, y=580)
            self.choice_PC_label.place(x=410, y=230)

        else:

            self.score_client = self.score_client + 1
            
            self.choice_PC_label.destroy()
            self.score_Label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='TESOURA',
                width=18,
                height=7,
            )
            self.score_Label = Label(
                text='YOU {} X {} PC'.format(self.score_client, self.score_Pc),
                background='gray'
            )
            
            self.score_Label.place(x=210, y=580)
            self.choice_PC_label.place(x=410, y=230)

    def user_Paper(self):
    
        self.choice_PC()
        if self.random_Choice_PC == 1:

            self.score_client = self.score_client + 1

            self.choice_PC_label.destroy()
            self.score_Label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='PEDRA',
                width=18,
                height=7,
            )
            self.score_Label = Label(
                text='YOU {} X {} PC'.format(self.score_client, self.score_Pc),
                background='gray'
            )

            self.score_Label.place(x=210, y=580)
            self.choice_PC_label.place(x=410, y=230)
        
        elif self.random_Choice_PC == 2:

            self.choice_PC_label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='PAPEL',
                width=18,
                height=7,
            )
            self.choice_PC_label.place(x=410, y=230)
           
        else:

            self.score_Pc = self.score_Pc + 1

            self.choice_PC_label.destroy()
            self.score_Label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='TESOURA',
                width=18,
                height=7,
            )
            self.score_Label = Label(
            text='YOU {} X {} PC'.format(self.score_client, self.score_Pc),
            background='gray'
            )

            self.choice_PC_label.place(x=410, y=230)
            self.score_Label.place(x=210, y=580)
    
    def user_Cramp(self):
    
        self.choice_PC()
        if self.random_Choice_PC == 1:

            self.score_Pc = self.score_Pc + 1

            self.choice_PC_label.destroy()
            self.score_Label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='PEDRA',
                width=18,
                height=7,
            )
            self.score_Label = Label(
                text='YOU {} X {} PC'.format(self.score_client, self.score_Pc),
                background='gray'
            )

            self.score_Label.place(x=210, y=580)
            self.choice_PC_label.place(x=410, y=230)

        elif self.random_Choice_PC == 2:

            self.score_client = self.score_client + 1

            self.choice_PC_label.destroy()
            self.score_Label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='PAPEL',
                width=18,
                height=7,
            )
            self.score_Label = Label(
                text='YOU {} X {} PC'.format(self.score_client, self.score_Pc),
                background='gray'
            )

            self.score_Label.place(x=210, y=580)
            self.choice_PC_label.place(x=410, y=230)

        else:

            self.choice_PC_label.destroy()

            self.choice_PC_label = Label(
                self.page_All,
                text='TESOURA',
                width=18,
                height=7,
            )

            self.choice_PC_label.place(x=410, y=230)

allPages()
