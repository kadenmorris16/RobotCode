import tkinter as tk
import subprocess
from robotProgrammingParser import RobotProgrammingParser

class RobotProgrammingGUI:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.actions = []
        
        # Create timeline slots
        self.num_slots = 9
        self.timeline_slots = [None] * self.num_slots
        self.slot_size = self.canvas.winfo_screenwidth() // (self.num_slots * 1.2)
        self.create_timeline_slots()

        # Create instruction icons
        self.icons = {
            "Drive": "🛞",
            "Turn": "🧭",
            "Head Tilt": "🙄",
            "Head Turn": "👀",
            "Waist Turn": "🔄",
            "Listen": "👂",
            "Talk": "🗣",
            "Gesture": "👋"
        }

        # Create play and trash buttons
        self.create_buttons()

        # Create icons
        self.create_icons()

    def create_timeline_slots(self):
        total_width = self.num_slots * self.slot_size  # Total width of the timeline
        canvas_width = self.canvas.winfo_screenwidth()
        canvas_height = self.canvas.winfo_screenheight()
        initial_x = (canvas_width - total_width) // 2  # Calculate initial x-coordinate for the first slot
        for i in range(self.num_slots):
            x = initial_x + i * self.slot_size
            y = canvas_height // 2 - self.slot_size // 2
            self.canvas.create_rectangle(x, y, x + self.slot_size, y + self.slot_size, outline="black", fill="lightblue")

    def create_icons(self):
        total_width = 8 * (self.slot_size // 2  + 50)
        canvas_width = self.canvas.winfo_screenwidth()
        canvas_height = self.canvas.winfo_screenheight()
        initial_x = (canvas_width - total_width) / 2  # Calculate initial x-coordinate for the first slot
        x, y = initial_x, canvas_height // 4 - (self.slot_size // 4)
        for name, icon in self.icons.items():
            label = tk.Label(self.root, text=icon, font=("Arial", int(self.slot_size // 2)), bg='lightgray', bd=2, relief=tk.RAISED)
            label.name = name
            label.bind("<ButtonPress-1>", self.on_icon_click)
            label.place(x=x, y=y)
            x += (self.slot_size // 2  + 50)

    def create_buttons(self):
        canvas_width = self.canvas.winfo_screenwidth()
        canvas_height = self.canvas.winfo_screenheight()

        # Play button
        play_button = tk.Label(self.root, text="🟢", font=("Arial", int(self.slot_size // 2)), bg='lightgray', bd=2, relief=tk.RAISED)
        play_button.bind("<ButtonPress-1>", lambda event: self.play_timeline())
        play_button.place(x = canvas_width*(3/5) - self.slot_size // 2, y = canvas_height*(3/4) - self.slot_size // 2)

        # Trash button
        trash_button = tk.Label(self.root, text="🗑️", font=("Arial", int(self.slot_size // 2)), bg='lightgray', bd=2, relief=tk.RAISED)
        trash_button.bind("<ButtonPress-1>", lambda event: self.restart())
        trash_button.place(x = canvas_width*(2/5) - self.slot_size // 2, y = canvas_height*(3/4) - self.slot_size // 2)

    def on_icon_click(self, event):
        icon_name = event.widget.name
        self.add_icon_to_timeline(icon_name)

    def add_icon_to_timeline(self, icon_name):
        canvas_width = self.canvas.winfo_screenwidth()
        canvas_height = self.canvas.winfo_screenheight()

        if None in self.timeline_slots:
            self.open_popup_window(icon_name)
            total_width = self.num_slots * self.slot_size
            initial_x = (canvas_width - total_width) // 2
            slot_index = self.timeline_slots.index(None)
            x, y = initial_x + slot_index * self.slot_size, canvas_height // 2 - self.slot_size // 2
            self.timeline_slots[slot_index] = icon_name
            self.canvas.create_text(x + self.slot_size/2, y + self.slot_size/2, text=self.icons[icon_name], font=("Arial", int(self.slot_size // 2)))
        else:
            message_x = canvas_width // 2
            message_y = canvas_height * (2/3)
            self.canvas.create_text(message_x, message_y, text="Timeline is full", font=("Arial", int(self.slot_size // 4)), fill="black")


    def open_popup_window(self, icon_name):
        popup_width = self.canvas.winfo_screenwidth()
        popup_height = self.canvas.winfo_screenheight()
        x_coordinate = popup_width // 2
        y_coordinate = popup_height // 2

        popup_window = tk.Toplevel(self.root)
        popup_window.title("Adjust " + icon_name + " Details")
        popup_window.geometry("%dx%d+%d+%d" % (popup_width, popup_height, x_coordinate, y_coordinate))


        font_size = int(popup_width // 30)

        if icon_name == "Drive":
            # forward/backward option
            forward_backward_frame = tk.Frame(popup_window)
            forward_backward_frame.pack(pady=(font_size/2,font_size/2))

            forward_backward_label = tk.Label(forward_backward_frame, text="Direction:", font=("Arial", font_size))
            forward_backward_label.grid(row=0, column=0, padx=(10, 20))

            forward_backward_options = ["Forward", "Backward"]
            popup_window.forward_backward_variable = tk.StringVar()
            popup_window.forward_backward_variable.set(forward_backward_options[0])
            for i, option in enumerate(forward_backward_options):
                button = tk.Radiobutton(forward_backward_frame, text=option, variable=popup_window.forward_backward_variable, value=option, font=("Arial", int(font_size/2)), indicatoron=False)
                button.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            # slider for speed (1-30)
            speed_frame = tk.Frame(popup_window)
            speed_frame.pack(pady=(font_size/2,font_size/2))

            speed_label = tk.Label(speed_frame, text="Speed:", font=("Arial", font_size))
            speed_label.grid(row=0, column=0, padx=(10, 20))

            popup_window.speed_slider = tk.Scale(speed_frame, from_=1, to=30, orient=tk.HORIZONTAL, length=popup_width/2, font=("Arial", font_size))
            popup_window.speed_slider.grid(row=0, column=1)

            # slider for distance (0-5 meters)
            distance_frame = tk.Frame(popup_window)
            distance_frame.pack(pady=(font_size/2,font_size/2))

            distance_label = tk.Label(distance_frame, text="Distance (m):", font=("Arial", font_size))
            distance_label.grid(row=0, column=0, padx=(10, 20))

            popup_window.distance_slider = tk.Scale(distance_frame, from_=0, to=5, orient=tk.HORIZONTAL, length=popup_width/2, resolution=0.1, font=("Arial", font_size))
            popup_window.distance_slider.grid(row=0, column=1)

        elif icon_name == "Turn":
            # left/right option
            left_right_frame = tk.Frame(popup_window)
            left_right_frame.pack(pady=(font_size/2, font_size/2))

            left_right_label = tk.Label(left_right_frame, text="Direction:", font=("Arial", font_size))
            left_right_label.grid(row=0, column=0, padx=(10, 20))

            left_right_options = ["Left", "Right"]
            popup_window.left_right_variable = tk.StringVar()
            popup_window.left_right_variable.set(left_right_options[0])
            for i, option in enumerate(left_right_options):
                button = tk.Radiobutton(left_right_frame, text=option, variable=popup_window.left_right_variable, value=option, font=("Arial", int(font_size/2)), indicatoron=False)
                button.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            # slider for time (0-5 seconds)
            time_frame = tk.Frame(popup_window)
            time_frame.pack(pady=(font_size/2, font_size/2))

            time_label = tk.Label(time_frame, text="Time (s):", font=("Arial", font_size))
            time_label.grid(row=0, column=0, padx=(10, 20))

            popup_window.time_slider = tk.Scale(time_frame, from_=0, to=5, orient=tk.HORIZONTAL, length=popup_width/2, resolution=0.1, font=("Arial", font_size))
            popup_window.time_slider.grid(row=0, column=1)

        elif icon_name == "Head Tilt":
            # up/down option
            up_down_frame = tk.Frame(popup_window)
            up_down_frame.pack(pady=(font_size/2, font_size/2))

            up_down_label = tk.Label(up_down_frame, text="Direction:", font=("Arial", font_size))
            up_down_label.grid(row=0, column=0, padx=(10, 20))

            up_down_options = ["Up", "Down"]
            popup_window.up_down_variable = tk.StringVar()
            popup_window.up_down_variable.set(up_down_options[0])
            for i, option in enumerate(up_down_options):
                button = tk.Radiobutton(up_down_frame, text=option, variable=popup_window.up_down_variable, value=option, font=("Arial", int(font_size/2)), indicatoron=False)
                button.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

        elif icon_name == "Head Turn":
            # left/right option
            left_right_frame = tk.Frame(popup_window)
            left_right_frame.pack(pady=(font_size/2, font_size/2))

            left_right_label = tk.Label(left_right_frame, text="Direction:", font=("Arial", font_size))
            left_right_label.grid(row=0, column=0, padx=(10, 20))

            left_right_options = ["Left", "Right"]
            popup_window.left_right_variable = tk.StringVar()
            popup_window.left_right_variable.set(left_right_options[0])
            for i, option in enumerate(left_right_options):
                button = tk.Radiobutton(left_right_frame, text=option, variable=popup_window.left_right_variable, value=option, font=("Arial", int(font_size/2)), indicatoron=False)
                button.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

        elif icon_name == "Waist Turn":
            # left/right option
            left_right_frame = tk.Frame(popup_window)
            left_right_frame.pack(pady=(font_size/2, font_size/2))

            left_right_label = tk.Label(left_right_frame, text="Direction:", font=("Arial", font_size))
            left_right_label.grid(row=0, column=0, padx=(10, 20))

            left_right_options = ["Left", "Right"]
            popup_window.left_right_variable = tk.StringVar()
            popup_window.left_right_variable.set(left_right_options[0])
            for i, option in enumerate(left_right_options):
                button = tk.Radiobutton(left_right_frame, text=option, variable=popup_window.left_right_variable, value=option, font=("Arial", int(font_size/2)), indicatoron=False)
                button.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

        elif icon_name == "Listen":
            # display text that says "I will listen, then repeat what was said"
            listen_frame = tk.Frame(popup_window)
            listen_frame.pack(fill=tk.X, pady=(font_size, font_size), anchor="n")

            listen_label = tk.Label(listen_frame, text="I will listen, then repeat what was said.", font=("Arial", font_size), wraplength=popup_width)
            listen_label.pack(expand=True)

        elif icon_name == "Talk":
            # Select one of the following:
            #   "Hi, I am Tango the Robot."
            #   "Get out of my way!"
            #   "Welcome to Montana State University"
            #   Custom entry field (keyboard pops up on the touchscreen on click)
            talk_frame = tk.Frame(popup_window)
            talk_frame.pack(pady=(font_size/2, font_size/2))

            talk_label = tk.Label(talk_frame, text="Message:", font=("Arial", font_size))
            talk_label.grid(row=0, column=0, columnspan=2, padx=(10, 20), sticky="nsew")  # Add columnspan and sticky parameter for centering

            talk_options = ["Hi, I am Tango the Robot.", "Get out of my way!", "Welcome to Montana State University", "Somebody charge me!"]
            popup_window.talk_variable = tk.StringVar()
            popup_window.talk_variable.set(talk_options[0])
            for i, option in enumerate(talk_options):
                button = tk.Radiobutton(talk_frame, text=option, variable=popup_window.talk_variable, value=option, font=("Arial", int(font_size/2)), indicatoron=False)
                button.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            custom_entry_label = tk.Label(popup_window, text="Custom message:", font=("Arial", font_size))
            custom_entry_label.pack()

            popup_window.custom_entry = tk.Entry(popup_window, font=("Arial", int(font_size/2)), width=int(font_size))
            popup_window.custom_entry.pack()
            #popup_window.custom_entry.bind("<Button-1>", self.open_keyboard)

        else: # Gesture
            # Select one of the following:
            #   point right
            #   point left
            #   hands up
            #   wave
            gesture_frame = tk.Frame(popup_window)
            gesture_frame.pack(pady=(font_size/2, font_size/2))

            gesture_label = tk.Label(gesture_frame, text="Gesture:", font=("Arial", font_size))
            gesture_label.grid(row=0, column=0, padx=(10, 20), sticky="w")

            gesture_options = ["Point Right", "Point Left", "Hands Up", "Wave"]
            popup_window.gesture_variable = tk.StringVar()
            popup_window.gesture_variable.set(gesture_options[0])
            for i, option in enumerate(gesture_options):
                button = tk.Radiobutton(gesture_frame, text=option, variable=popup_window.gesture_variable, value=option, font=("Arial", int(font_size/2)), indicatoron=False)
                button.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

        # Apply button
        apply_button = tk.Button(popup_window, text="☑️", command=lambda: self.apply_adjustments(icon_name, popup_window), font=("Arial", font_size), padx=10, pady=5, borderwidth=2, relief=tk.RAISED, background="lightgray")
        apply_button.pack(pady=(font_size,font_size))

    def open_keyboard(self, event):
        subprocess.Popen(['matchbox-keyboard', '--fontptsize', self.slot_size])

    def apply_adjustments(self, icon_name, popup_window):
        string = ""

        if icon_name == "Drive":
            string += "Drive "
            string += str(popup_window.forward_backward_variable.get()) + " "
            string += str(popup_window.speed_slider.get()) + " "
            string += str(popup_window.distance_slider.get())

        elif icon_name == "Turn":
            string += "Turn "
            string += str(popup_window.left_right_variable.get()) + " "
            string += str(popup_window.time_slider.get())

        elif icon_name == "Head Tilt":
            string += "HeadTilt "
            string += str(popup_window.up_down_variable.get())

        elif icon_name == "Head Turn":
            string += "HeadTurn "
            string += str(popup_window.left_right_variable.get())

        elif icon_name == "Waist Turn":
            string += "WaistTurn "
            string += str(popup_window.left_right_variable.get())

        elif icon_name == "Listen":
            string += "Listen"

        elif icon_name == "Talk":
            string += "Talk "
            if(str(popup_window.custom_entry.get()).strip() == ""):
                string += str(popup_window.talk_variable.get())
            else:
                string += str(popup_window.custom_entry.get())

        else: # Gesture
            string += "Gesture "
            if(str(popup_window.gesture_variable.get()) == "Point Right"):
                string += "pointRight"
            elif(str(popup_window.gesture_variable.get()) == "Point Left"):
                string += "pointLeft"
            elif(str(popup_window.gesture_variable.get()) == "Hands Up"):
                string += "handsUp"
            else:
                string += "wave"
        
        self.actions.append(string)
        print(string)

        popup_window.destroy()

    def play_timeline(self):
        RobotProgrammingParser(self.actions, self.root)
        print("Parsing Actions")
        self.restart()

    def restart(self):
        self.timeline_slots = [None] * self.num_slots
        self.canvas.delete("all")
        self.actions.clear()
        print("CLEARED")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        self.create_timeline_slots()
        self.create_buttons()
        self.create_icons()




def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    canvas = tk.Canvas(root, bg="#dcdcdc")
    canvas.pack(fill=tk.BOTH, expand=True)
    RobotProgrammingGUI(root, canvas)
    root.mainloop()

if __name__ == "__main__":
    main()
