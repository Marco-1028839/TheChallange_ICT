import customtkinter as tkc

class EmailsPage(tkc.CTkFrame):
    def __init__(self, parent, controller):
        tkc.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.greeting_label = tkc.CTkLabel(self, text="Emails per groep")
        self.greeting_label.pack(pady=10, padx=10)

        self.kluis_button = tkc.CTkButton(self, text="Home", command=lambda: controller.show_frame("HomePage"))
        self.kluis_button.pack(pady=10, padx=10)
