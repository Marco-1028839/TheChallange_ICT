import customtkinter as ctk
from config import *
from menu import *

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        ctk.CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller


        self.menu_bar = Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill= "y")
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)

        self.center_field = Center_field(self)
        self.center_field.pack(side="right", fill="both", expand=True, padx=10,pady=10)

        


class Center_field(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.user_name = "Marco"


        self.test_label = ctk.CTkLabel(self, text=f"Welkom {self.user_name}")
        self.test_label.pack()



        
        