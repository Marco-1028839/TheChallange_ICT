import customtkinter as ctk
from config import *
import menu, server_con





class PersonPage(ctk.CTkFrame):
    global list_of_kluis_ids
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.server_conn = server_con.personen_api_connectie()
        output = self.server_conn.get_all_persons()
        print(len(output))



        #self.kluizen_status_page = None

        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)

        self.panel = ctk.CTkFrame(self)
        
        last_index = 0
        range_end = 5
        length = len(output)
        while True:
            if last_index >= len(output):
                break
            else:
                frame = ctk.CTkFrame(self.panel)
                
                print(f"length: {length}")
                
                if length < range_end:
                    range_end = length
                print(f"range_end: {range_end}")
                for _ in range(range_end):
                    button_id = output[last_index]['id']
                    last_index += 1
                    panel = ctk.CTkButton(
                        frame,
                        text=f"Person ID: {button_id}",
                        height=100,
                        width=100,
                        border_color=MENU_BACKGROUND_COLOR,
                        border_width=5,
                        fg_color=KLUIS_FULL_COLOR,
                        text_color="black",
                        command=lambda bid=button_id: self.to_person_info(bid)
                        )
                    panel.pack(side="left", anchor="center",pady=10, padx=10)
                frame.pack(side="top", anchor="center", pady=10, padx=10)
                length -= range_end
                print(f"length: {length}")
        
        self.panel.pack(side="right", fill="both", expand=True)
        
    

    def to_person_info(self, id):
        # Displays detailed information for a specific person
        self.server_conn = server_con.personen_api_connectie()
        output = self.server_conn.get_specific_person(id)


        status_page = self.controller.frames["Person_info_page"]

        status_page.person_id.configure(text=f"Person ID:   {output['id']}")
        status_page.name.configure(text=f"Name:   {output['username']}")
        status_page.email.configure(text=f"Email:   {output['email']}")
        status_page.telefoon.configure(text=f"Telefoon:   {output['telefoon']}")


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
        

        
    
        # ---- graphics
        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)
        self.kluis_id = ctk.CTkLabel(self, text=f"")
        self.kluis_id.pack(side="right")

        # ---- main area
        self.person_id = ctk.CTkLabel(self, text=f"")
        self.person_id.pack(pady=10, padx=10)

        self.name = ctk.CTkLabel(self, text=f"Gebruikers naam: <NAME>")
        self.name.pack(pady=10, padx=10)
        
        self.email = ctk.CTkLabel(self, text=f"Email: john@doe.com")
        self.email.pack(pady=10, padx=10)
        
        self.telefoon = ctk.CTkLabel(self, text=f"Telefoon: 06-12345678")
        self.telefoon.pack(pady=10, padx=10)


        
        self.person_delete_button = ctk.CTkButton(self,
                                                  text="Delete Persoon",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.person_delete_button.pack(side="left", anchor="center",pady=10, padx=10)

        self.change_email_button = ctk.CTkButton(self,
                                                  text="Change email",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.change_email_button.pack(side="left", anchor="center",pady=10, padx=10)

        self.chanege_name_button = ctk.CTkButton(self,
                                                  text="Change name",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.chanege_name_button.pack(side="left", anchor="center",pady=10, padx=10)

        self.change_telefoon_number = ctk.CTkButton(self,
                                                  text="Change telefoon number",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.change_telefoon_number.pack(side="left", anchor="center",pady=10, padx=10)

        
    








