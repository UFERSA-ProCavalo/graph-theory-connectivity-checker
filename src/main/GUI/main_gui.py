import customtkinter as ctk

# Import your BFS and DFS implementations

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("BFS and DFS Visualizer")

        self.create_widgets()

    def create_widgets(self):
        # Add your widget creation code here
        pass


# Initialize and run the GUI
if __name__ == "__main__":
    app = App()
    app._state_before_windows_set_titlebar_color = "zoomed"
    app.mainloop()