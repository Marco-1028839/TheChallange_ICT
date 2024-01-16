from typing import Optional, Tuple, Union
import customtkinter as ctk
class Menu_bar(ctk.CTkFrame):
    def __init__(self, controller ,parent: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None ,**kwargs):
        super().__init__(parent, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.login_button = ctk.CTkButton(self, text="Logout", command=lambda: controller.show_frame("LoginPage"))
        self.login_button.pack(pady=10, padx=10, side="bottom")

        self.kluis_button = ctk.CTkButton(self, text="Kluizen", command=lambda: controller.show_frame("KluizenPage"))
        self.kluis_button.pack(pady=10, padx=10)

        self.kluis_button = ctk.CTkButton(self, text="Email", command=lambda: controller.show_frame("EmailsPage"))
        self.kluis_button.pack(pady=10, padx=10)