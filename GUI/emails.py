import customtkinter as ctk
from config import *
import menu, server_con





class EmailsPage(ctk.CTkFrame):
    global list_of_kluis_ids
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.server_conn = server_con.email_api_connectie()
        output = self.server_conn.get_all_emails()
        print(len(output))
        



        #self.kluizen_status_page = None

        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)

        self.panel = ctk.CTkFrame(self)

        last_index = 0
        while True:
            if last_index >= len(output):
                break
            else:
                frame = ctk.CTkFrame(self.panel)
                for _ in range(5):
                    button_id = output[last_index]['id']
                    last_index += 1
                    panel = ctk.CTkButton(
                        frame,
                        text=f"Email ID: {button_id}",
                        height=50,
                        width=100,
                        border_color=MENU_BACKGROUND_COLOR,
                        border_width=5,
                        fg_color=KLUIS_FULL_COLOR,
                        text_color="black",
                        command=lambda bid=button_id: self.to_Email(bid)
                        )
                    panel.pack(side="left", anchor="center",pady=10, padx=10)
                frame.pack(side="top", anchor="center", pady=10, padx=10)
        
        
        self.panel.pack(side="right", fill="both", expand=True)
        
    

    def to_Email(self, id):
        self.server_conn = server_con.email_api_connectie()
        output = self.server_conn.get_specific_email(id)

        status_page = self.controller.frames["Email_reader_page"]


        status_page.email_id.configure(text=f"Email ID:   {output['id']}")
        status_page.email_reciever.configure(text=f"Reciever:   {output['reciever']}")
        status_page.email_title.configure(text=f"Title:   {output['title']}")
        status_page.email_text.configure(text=f"Test:\n{output['body']}")
        status_page.email_date.configure(text=f"Date:   {output['date']}")


        self.controller.show_frame("Email_reader_page")
 



class Email_reader_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        self.controller = controller

        # ---- confic variables
        self.id = 0 #default value
        self.status = False
        self.reciever = "John Doe"


        # ---- menu bar
        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)
        self.kluis_id = ctk.CTkLabel(self, text=f"")
        self.kluis_id.pack(side="right")

        # ---- main area
        self.email_id = ctk.CTkLabel(self, text=f"{self.id}")
        self.email_id.pack(pady=10, padx=10)

        self.email_title = ctk.CTkLabel(self, text=f"Title: Some Email Title")
        self.email_title.pack(pady=10, padx=10)
        
        self.email_reciever = ctk.CTkLabel(self, text=f"{self.reciever}")
        self.email_reciever.pack(pady=10, padx=10)

        self.email_text = ctk.CTkLabel(self, text="", justify="left")
        self.email_text.pack(pady=10, padx=10)

        self.email_date = ctk.CTkLabel(self, text="Date: 2020-01-01")
        self.email_date.pack(pady=10, padx=10)

        
        self.locker_delete_button = ctk.CTkButton(self,
                                                  text="Delete",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.locker_delete_button.pack(side="left", anchor="center",pady=10, padx=10)
        








