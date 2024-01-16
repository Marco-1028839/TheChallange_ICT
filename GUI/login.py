import customtkinter
from PIL import Image

from config import *

class LoginPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller

        self.test_name = "user"
        self.test_passwd = "pass"

        self.left_section = customtkinter.CTkFrame(self, )
        self.right_section = customtkinter.CTkLabel(self, text="Welkom bij de Voedselkluis" ,image=customtkinter.CTkImage(Image.open(LOGIN_BACKGROUND_IMAGE_01), Image.open(LOGIN_BACKGROUND_IMAGE_01), size=(SCREEN_SIZE[0],SCREEN_SIZE[1])))

     
        

        self.login_section = customtkinter.CTkFrame(self.left_section)

        self.label_name = customtkinter.CTkLabel(self.login_section, text="Email",)
        self.label_name.grid(row=0, column=0, padx=20, pady=10)
        self.entry_name = customtkinter.CTkEntry(self.login_section)
        self.entry_name.grid(row=1, column=0, padx=20, pady=10)

        self.label_password = customtkinter.CTkLabel(self.login_section, text="Password")
        self.label_password.grid(row=3, column=0, padx=20, pady=10)
        self.entry_password = customtkinter.CTkEntry(self.login_section, show="*")
        self.entry_password.grid(row=4, column=0, padx=20, pady=10)

        self.button_login = customtkinter.CTkButton(self.login_section, text="Login",
                                                    command=lambda: self.controller.show_frame("HomePage") if self.login() else "")
        self.button_login.grid(row=5, column=0, padx=20, pady=10)


        self.login_section.pack(side="left", expand=True, pady=30, padx=30)

        self.left_section.pack(side="left", expand=True, fill="both", pady=10,padx=10)
        self.right_section.pack(side="right", expand=True, fill="both", pady=10, padx=10)

    def login(self):
        if self.test_name == self.entry_name.get() and self.test_passwd == self.entry_password.get():
            return True
