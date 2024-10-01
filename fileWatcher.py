import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadOnChange(FileSystemEventHandler):
    def __init__(self, command):
        super().__init__()
        self.command = command
        self.process = None
        self.start_process()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            self.restart_process()

    def start_process(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen(self.command, shell=True)

    def restart_process(self):
        print("Changes detected, restarting the application...")
        self.start_process()

if __name__ == "__main__":
    path = "."  # Directory to monitor (current directory)
    command = "python main.py"  # Command to start the Tkinter app

    event_handler = ReloadOnChange(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
