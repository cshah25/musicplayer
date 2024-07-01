import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
from mutagen.mp3 import MP3
import threading
import pygame
import time
import os

def play():
    pass

def pause():
    pass

def stop():
    pass

def next():
    pass

def prev():
    pass

def openFile():
    try:
        file = filedialog.askopenfile(initialdir='~/Music',title='Select Songs', filetypes=[("Music files",".mp3 .wav")])
        return file
    except Exception as e:
        print(e)
        return False

def addsongs():
    file = openFile()

    if (file == False): 
        return False

def deletesongs():
    pass

def main():
    # Main Window
    window = tk.Tk()
    window.title("Music Player CS")
    window.geometry("600x500")

    # Lable
    lbl_title = tk.Label

if __name__ == "__main__":
    main()