import threading
import tkinter as tk
import pyautogui
import time

class MouseMover:
    def __init__(self, interval):
        self.interval = interval
        self.thread = None
        self.running = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.move_mouse)
        self.thread.start()

    def stop(self):
        self.running = False

    def move_mouse(self):
        while self.running:
            pyautogui.moveRel(10, 10)
            pyautogui.moveRel(10, 10)
            time.sleep(self.interval)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.mover = None
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.master, text="Iniciar", command=self.start_mover)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Parar", command=self.stop_mover, state="disabled")
        self.stop_button.pack()

    def start_mover(self):
        self.mover = MouseMover(interval=20)
        self.mover.start()
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

    def stop_mover(self):
        if self.mover is not None:
            self.mover.stop()
            self.mover = None
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
