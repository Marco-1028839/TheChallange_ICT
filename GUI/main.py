import customtkinter
from config import *
import login, home, kluizen, emails, server_con, personen

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(f"{size[0]}x{size[1]}")
        self.title(title)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        

        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)  # configure grid system
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.logingpage = login.LoginPage
        self.homepage =  home.HomePage
        self.kluizenpage = kluizen.KluizenPage
        self.emailspage = emails.EmailsPage
        self.emailsreaderpage = emails.Email_reader_page
        self.kluizen_status_page = kluizen.Kluis_status_page
        self.personenpage = personen.PersonPage
        self.persononinfopage = personen.Person_info_page

        

        for frame in (self.logingpage, self.homepage, self.kluizenpage, self.emailspage, self.emailsreaderpage, self.kluizen_status_page, self.personenpage, self.persononinfopage):
            page_name = frame.__name__
            frame = frame(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")
        
        #self.kluizenpage.to_kluis_status = self.kluizen_status_page

       

        self.show_frame("LoginPage")



    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == '__main__':
    app = App(SCREEN_SIZE,  SCREEN_TITLE)
    app._set_appearance_mode("light")
    app.mainloop()
    
    