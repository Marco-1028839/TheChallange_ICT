import customtkinter as ctk
from config import *
import menu, server_con
import random





class KluizenPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        """Initializes KluizenPage frame with menu bar and grid of locker status buttons.
        
        Connects to locker API to get list of all lockers. Creates menu bar and configures 
        style. Creates scrollable frame with grid of buttons for each locker, configured
        with locker ID, colors indicating status, and click handler to show locker details.
        Buttons are arranged in grid of 5 columns per row. 
        """
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
           
        self.server_conn = server_con.kluis_api_connectie()
        output = self.server_conn.get_all_kluizen()
    


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
                        text=f"Kluis ID: {button_id}",
                        height=100,
                        width=100,
                        border_color=MENU_BACKGROUND_COLOR,
                        border_width=5,
                        fg_color=KLUIS_FULL_COLOR,
                        text_color="black",
                        command=lambda bid=button_id: self.to_kluis_status(bid)
                        )
                    panel.pack(side="left", anchor="center",pady=10, padx=10)
                frame.pack(side="top", anchor="center", pady=10, padx=10)
        self.panel.pack(side="right", fill="both", expand=True)  
        
        
        
        """
        for y in range(4):
            
            frame = ctk.CTkFrame(self.panel)
            for x in range(5):
                
                panel = ctk.CTkButton(
                    frame, 
                    text=f"{button_id}", 
                    height=100, 
                    width=100, 
                    border_color=MENU_BACKGROUND_COLOR, 
                    border_width=5,
                    fg_color=KLUIS_FULL_COLOR, 
                    text_color="black",
                    command=lambda bid=button_id: self.to_kluis_status(bid)
                    )
                panel.pack(side="left", anchor="center",pady=10, padx=10)
                
                

            frame.pack(side="top", anchor="center", pady=10, padx=10)
        """    
        
        

    
    

    def to_kluis_status(self, id):
        # Retrieves locker data from API and configures status page with details.
        # id: ID of locker to retrieve data for and display status of.
        # Gets locker data from API based on id. Configures status page labels and colors 
        # to indicate locker status. Shows status page.
        self.server_conn = server_con.kluis_api_connectie()
        output = self.server_conn.get_specific_kluis(id)
        
        status_page = self.controller.frames["Kluis_status_page"]

        
        status_page.locker_number.configure(text=f"Locker ID:   {output['id']}")
        if output['status'] == 0:
            status_page.locker_status.configure(text=f"Locker status: EMPTY", text_color="#cc0425", width=25, height=25)
        elif output['status'] == 1:
            status_page.locker_status.configure(text=f"Locker status: FULL", text_color="#008000", width=25, height=25)
        
        status_page.locker_code.configure(text=f"Locker code:   {output['code']}")
        status_page.status = output['status']

        self.controller.show_frame("Kluis_status_page")
 



class Kluis_status_page(ctk.CTkFrame):# Kluis_status_page is a custom CTkFrame subclass that displays the status and information for a specific locker. It allows changing the locker status and deleting the locker.

    def __init__(self, parent, controller):
        # Initializes Kluis_status_page frame with locker ID, status, and code. 
        # Configures menu bar and UI elements to display locker info and buttons 
        # to change status, delete, and change code. Binds button clicks to 
        # corresponding methods.
        ctk.CTkFrame.__init__(self,parent)
        self.controller = controller

        # ---- confic variables
        self.id = 0 #default value
        self.status = 0 #default value
        self.status_text = "Locker status: EMPTY" #default value

        
    
        # ---- graphics
        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)
        self.kluis_id = ctk.CTkLabel(self, text=f"")
        self.kluis_id.pack(side="right")

        # ---- main area
        self.locker_number = ctk.CTkLabel(self, text=f"{self.id}")
        self.locker_number.pack(pady=10, padx=10)
        
        self.locker_status = ctk.CTkLabel(self, text=f"{self.status_text}")
        self.locker_status.pack(pady=10, padx=10)

        self.locker_code = ctk.CTkLabel(self, text=f"Locker code: ***-***-***")
        self.locker_code.pack(pady=10, padx=10)

        self.locker_status_button = ctk.CTkButton(self,
                                                  text="Change status",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5,
                                                  command=lambda: self.change_status())
        self.locker_status_button.pack(side="left", anchor="center",pady=10, padx=10)
        self.locker_delete_button = ctk.CTkButton(self,
                                                  text="Delete",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.locker_delete_button.pack(side="left", anchor="center",pady=10, padx=10)

        self.locker_change_code_button = ctk.CTkButton(self,
                                                       text="Change code",
                                                       height=50,
                                                       width=100,
                                                       border_color=MENU_BACKGROUND_COLOR,
                                                       border_width=5,
                                                       command=lambda: self.change_code())
        self.locker_change_code_button.pack(side="left", anchor="center",pady=10, padx=10)
    
    def change_code(self):
        # Generates a random 3-part locker code, checks if it already 
        # exists, and if not, updates the locker with the new code
        code = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
        self.server_conn = server_con.kluis_api_connectie()
        output = self.server_conn.get_all_kluizen()
        for kluis in output:
            if kluis["code"] == code:
                code = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
            else:
                self.server_conn.change_code(self.id, code)
                self.locker_code.configure(text=f"Locker code:   {code}")
                break



        
    def change_status(self):
        # Changes the status of the locker between FULL and EMPTY by updating the server and UI.
        self.server_conn = server_con.kluis_api_connectie()
        if self.status == 0:
            self.server_conn.change_status(self.id, 1)
            self.status = 1
            self.status_text = "Locker status: FULL"
            self.locker_status.configure(text=f"Locker status: FULL", text_color="#008000", width=25, height=25)
        else:
            self.server_conn.change_status(self.id, 0)
            self.status = 0
            self.status_text = "Locker status: EMPTY"
            self.locker_status.configure(text=f"Locker status: EMPTY", text_color="#cc0425", width=25, height=25)
        self.locker_status.configure(text=f"{self.status_text}")






