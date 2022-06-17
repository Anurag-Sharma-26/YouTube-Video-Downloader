from tkinter import *
from pytube import YouTube

# create display window
window = Tk()
window.geometry('800x400')
window.resizable(0, 0)
window.title("Youtube video downloader")
Label(window, text="Youtube Video Downloader",
      font='arial 26 bold').pack()

# Link Input
link = StringVar()

Label(window, text='Paste Link here:',
      font='arial 16 bold').place(x=70, y=90)
link_enter = Entry(window, width=100, textvariable=link
                   ).place(x=40, y=120)


# download function
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download("D:\\videos\\")
    Label(window, text='DOWNLOADED', font='arial 16'
          ).place(x=280, y=250)


Button(window, text='DOWNLOAD', font='arial 16', bg='pale violet red',
       padx=2, command=downloader).place(x=280, y=200)

window.mainloop()
