import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Graph Theory - Connectivity Checker")

        self.create_widgets()

    def create_widgets(self):
        pass


if __name__ == "__main__":
    window = App()
    window._state_before_windows_set_titlebar_color = "zoomed"
    window.mainloop()
