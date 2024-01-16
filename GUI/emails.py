import customtkinter as ctk
from config import *
import menu, server_con





class EmailsPage(ctk.CTkFrame):
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
            idy -= 1
        
        self.panel.pack(side="right", fill="both", expand=True)
        
    

    def to_Email(self, id):

        self.server_conn = server_con.kluis_api_connectie()
        output = self.server_conn.get_specific_kluis(id)

        status_page = self.controller.frames["Email_reader_page"]

        status_page.email_id.configure(text=f"Email ID:   {id}")


        self.controller.show_frame("Email_reader_page")
 



class Email_reader_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        self.controller = controller

        # ---- confic variables
        self.id = 0 #default value
        self.status = False
        self.reciever = "John Doe"

        self.email_content = """
        Er en om vlijtige op verleden gestoken uiterste. 
        Smeltovens op mijnschool afwachting de ze wantrouwen nu uiteenvalt. 
        Overgaat centimes vlijtige zal plaatsen geworden bak zij. 
        Liep koel aan zij wat acre even tien iets. 
        In werkelijk ad aanraking liverpool in nu bereiding. 
        Tunnel handen al te cijfer ik brusch succes na.

        Toch hier in wiel maar wijk ze bate. 
        Werkman inkomen aan metalen dus zin gevoerd. 
        Worm om vast koel en meer bord. Ver die wild zout kant. 
        Op of ruimte enkele gezegd. Is afkomst taiping brokken donkere geleend de. 
        Middelpunt dan initiatief die het ptolomaeus verscholen wij.

        Allen spijt ik hevea ad de bonte. 
        Bedraagt zin grootste eromheen een uitgeput vijftien vreemden der tot. 
        Bedreven vlijtige ad af is tweemaal of gelijken schaffen. Moderne wel zou drijven ontzegd amboina. 
        Wel uit wij engelsche ook aardschok bestreken. 
        En ontrukten overvloed antwerpen al aankoopen bijgeloof besparing op. 
        Gewijzigd goa ontrukten vertoonen wat stoompomp wassching behandeld. 
        Ontsnappen tot verdwijnen lot verbazende tinwinning nauwelijks verlichten. 
        Slotte er in groote mijnen daarin.

        En om afkomst op bekkens javanen gronden er bersawa. 
        Dier daar ik in eens zelf vorm. Sommige systeem op de toegang geheven. 
        Alleen pahang ter breede boomen dat nam heb. 
        Dal wij bezetten strooien snelsten veteraan moeilijk van eveneens tot. 
        Verlichten dergelijke vruchtbaar en de woekeraars na.
        Groot geldt ook eenig men. Steek wegen na ik alles en grond de.

        Kosten zoo mee sunger heb are varens. 
        Arbeiden baksteen gesloten rug zoo mijnbouw zes contract heerlijk bij. 
        Verlaten systemen millioen op er er cultures uitgeput.
        Schijnt moderne hoeveel af de al tunnels inkomen. 
        Ingericht of al de stichting britschen uitgaande en. 
        Mijnschool zit dus herkenbaar verzamelen onvermoeid. 
        Ellen in en allen massa na zeker. 
        Herhaling zuidgrens te al opgevoerd nu mineralen er. 
        Aanmerking werkwijzen mogendheid herkenbaar mei agentschap een ontsnappen.
        """
        
    
        # ---- graphics
        self.menu_bar = menu.Menu_bar(self.controller, parent=self, width=300)
        self.menu_bar.pack(side="left", fill="both")  
        self.menu_bar.configure(fg_color=MENU_BACKGROUND_COLOR)
        self.kluis_id = ctk.CTkLabel(self, text=f"")
        self.kluis_id.pack(side="right")

        # ---- main area
        self.email_id = ctk.CTkLabel(self, text=f"{self.id}")
        self.email_id.pack(pady=10, padx=10)

        self.email_title = ctk.CTkLabel(self, text=f"Title: Some Email Title")
        self.email_id.pack(pady=10, padx=10)
        
        self.email_reciever = ctk.CTkLabel(self, text=f"{self.reciever}")
        self.email_reciever.pack(pady=10, padx=10)

        self.email_text = ctk.CTkLabel(self, text=self.email_content, justify="left")
        self.email_text.pack(pady=10, padx=10)

        
        self.locker_delete_button = ctk.CTkButton(self,
                                                  text="Delete",
                                                  height=50,
                                                  width=100,
                                                  border_color=MENU_BACKGROUND_COLOR,
                                                  border_width=5)
        self.locker_delete_button.pack(side="left", anchor="center",pady=10, padx=10)
        








