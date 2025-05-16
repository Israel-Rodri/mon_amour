import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        # Create a canvas
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Link the scrollbar to the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

    def add_widget(self, widget):
        widget.pack(in_=self.scrollable_frame)

# Create the main application window
root = tk.Tk()
root.title("Scrollable Frame Example")

# Create an instance of the ScrollableFrame
scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(fill="both", expand=True)

# Add some widgets to the scrollable frame
for i in range(30):
    label = tk.Label(scrollable_frame.scrollable_frame, text=f"Label {i+1}")
    scrollable_frame.add_widget(label)

# Start the Tkinter main loop
root.mainloop()