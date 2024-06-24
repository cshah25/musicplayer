from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound

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
    root = Tk()
    root.geometry('3000x1500')
    root.minsize(500, 500)
    root.title('Music Player')

    my_menu=Menu(root)
    root.config(menu=my_menu)
    add_song_menu=Menu(my_menu)
    my_menu.add_cascade(label="Menu",menu=add_song_menu)
    add_song_menu.add_command(label="Add songs",command=addsongs)
    add_song_menu.add_command(label="Delete song",command=deletesongs)

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


if __name__ == "__main__":
    main()