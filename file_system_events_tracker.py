import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/zahme_85berv3"

class fileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hi, {event.src_path} has been created")
    def on_deleted(self, event):
        print(f"Oops, someone deleted {event.src_path}")
    def on_modified(self, event):
        print(f"Hi there, {event.src_path} has been modified")
    def on_moved(self, event):
        print(f"Someone moved {event.src_path} to {event.dest_path}")

eventHandler = fileEventHandler()
observer = Observer()

observer.schedule(eventHandler, from_dir, recursive = True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print('Stopped')
    observer.stop()