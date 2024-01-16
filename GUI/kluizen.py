from typing import Optional, Tuple, Union
import customtkinter as ctk
from config import *
import menu, server_con

currend_kluis_id = 0

class KluizenPage(ctk.CTkFrame):
    global list_of_kluis_ids
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        #self.kluizen_status_page = None




        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)

        self.panel = ctk.CTkFrame(self)
        idx = 0
        idy = 1
        for y in range(4):
            idy+=1
            frame = ctk.CTkFrame(self.panel)
            for x in range(5):
                button_id = idx - 1 + idy  # Calculate the button ID once for each button
                idx+=1
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
            idy -= 1
        
        self.panel.pack(side="right", fill="both", expand=True)
        
    

    def to_kluis_status(self, id):
        global currend_kluis_id
        currend_kluis_id = id
        status_page = self.controller.frames["Kluis_status_page"]
        status_page.greeting_label.configure(text=f"{id}")
        self.controller.show_frame("Kluis_status_page")
 



class Kluis_status_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        self.controller = controller

        # ---- confic variables
        

        # ---- get info about the kluis class
        self.id = currend_kluis_id

        # ---- graphics
        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)
        self.kluis_id = ctk.CTkLabel(self, text=f"")
        self.kluis_id.pack(side="right")

        # ---- main area
        self.greeting_label = ctk.CTkLabel(self, text=f"{self.id}")
        self.greeting_label.pack(pady=10, padx=10)
        self.get_kluis_info()


    def get_kluis_info(self):
        """Get information from the server and display it on the page"""
        pass








