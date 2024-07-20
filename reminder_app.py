import tkinter as tk
from tkinter import messagebox
import time
import threading
from datetime import datetime, timedelta

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder Application")
        
        self.reminders = []
        
        self.label = tk.Label(root, text="Enter reminder:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        self.time_label = tk.Label(root, text="Enter time (in seconds):")
        self.time_label.pack(pady=10)
        
        self.time_entry = tk.Entry(root, width=50)
        self.time_entry.pack(pady=10)
        
        self.button = tk.Button(root, text="Set Reminder", command=self.set_reminder)
        self.button.pack(pady=20)
        
        self.log_label = tk.Label(root, text="Reminder Log:")
        self.log_label.pack(pady=10)
        
        self.log_text = tk.Text(root, width=50, height=10)
        self.log_text.pack(pady=10)
        self.log_text.config(state=tk.DISABLED)
        
    def set_reminder(self):
        reminder_text = self.entry.get()
        try:
            reminder_time = int(self.time_entry.get())
            reminder_time_absolute = datetime.now() + timedelta(seconds=reminder_time)
            reminder_data = {
                "text": reminder_text,
                "time": reminder_time,
                "time_absolute": reminder_time_absolute
            }
            self.reminders.append(reminder_data)
            threading.Thread(target=self.reminder_thread, args=(reminder_data,)).start()
            self.log(f"Reminder set for {reminder_time} seconds: {reminder_text}")
            messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time} seconds.")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid time in seconds")
    
    def reminder_thread(self, reminder_data):
        time.sleep(reminder_data["time"])
        self.show_popup(reminder_data["text"])
        self.log(f"Reminder triggered: {reminder_data['text']}")
    
    def show_popup(self, reminder_text):
        popup = tk.Toplevel()
        popup.title("Reminder")
        popup.geometry("300x100")
        
        label = tk.Label(popup, text=reminder_text, wraplength=250)
        label.pack(pady=10)
        
        button = tk.Button(popup, text="OK", command=popup.destroy)
        button.pack(pady=10)

    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
        self.log_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
