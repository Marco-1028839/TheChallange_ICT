import customtkinter as ctk
from config import *
import menu, server_con





class PersonPage(ctk.CTkFrame):
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
                    text=f"person ID: {button_id}", 
                    height=50, 
                    width=100, 
                    border_color=MENU_BACKGROUND_COLOR, 
                    border_width=5,
                    fg_color=KLUIS_FULL_COLOR, 
                    text_color="black",
                    command=lambda bid=button_id: self.to_person_info(bid)
                    )
                panel.pack(side="left", anchor="center",pady=10, padx=10)
                
                

            frame.pack(side="top", anchor="center", pady=10, padx=10)
            idy -= 1
        
        self.panel.pack(side="right", fill="both", expand=True)
        
    

    def to_person_info(self, id):

        self.server_conn = server_con.kluis_api_connectie()
        output = self.server_conn.get_specific_kluis(id)

        status_page = self.controller.frames["Person_info_page"]

        status_page.person_id.configure(text=f"Person ID:   {id}")


        self.controller.show_frame("Person_info_page")
 



class Person_info_page(ctk.CTkFrame):# Person_info_page class inherits from ctk.CTkFrame
# Displays detailed information for a specific person
# Includes menu bar, labels to display person ID, name, and other details
# Has button to delete the person

    def __init__(self, parent, controller):
        # Initializes Person_info_page frame with parent and controller.  
        # Sets up UI elements like menu bar, labels, and buttons.
        # Displays person ID, name, and other details.
        # Button allows deleting the person.
        ctk.CTkFrame.__init__(self,parent)
        self.controller = controller

        # ---- confic variables
        self.reciever = "John Doe"

        
    
        # ---- graphics
        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)
        self.kluis_id = ctk.CTkLabel(self, text=f"")
        self.kluis_id.pack(side="right")

        # ---- main area
        self.person_id = ctk.CTkLabel(self, text=f"")
        self.person_id.pack(pady=10, padx=10)

        self.name = ctk.CTkLabel(self, text=f"Name: John Doe \nGeboren: 01-01-1990\nleeftijd: 32 jaar")
        self.name.pack(pady=10, padx=10)

        self.location = ctk.CTkLabel(self, text=f"Locatie: Den Haag\nGebied: wijk X")
        self.location.pack(pady=10, padx=10)
        
        self.email = ctk.CTkLabel(self, text=f"Email: john@doe.com")
        self.email.pack(pady=10, padx=10)


        
        self.locker_delete_button = ctk.CTkButton(self,
                                                  text="Delete Persoon",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.locker_delete_button.pack(side="left", anchor="center",pady=10, padx=10)

        self.locker_delete_button = ctk.CTkButton(self,
                                                  text="Change email",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.locker_delete_button.pack(side="left", anchor="center",pady=10, padx=10)

        self.locker_delete_button = ctk.CTkButton(self,
                                                  text="Change name",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.locker_delete_button.pack(side="left", anchor="center",pady=10, padx=10)

        self.locker_delete_button = ctk.CTkButton(self,
                                                  text="change location",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.locker_delete_button.pack(side="left", anchor="center",pady=10, padx=10)
        








