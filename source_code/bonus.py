import tkinter as tk

class Timer:
    def __init__(self, root, time_left, timer_label):
        self.root = root
        self.time_left = time_left
        self.timer_label = timer_label
        self.timer = None

    def start_timer(self):
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Temps restant: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer = self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def cancel_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)