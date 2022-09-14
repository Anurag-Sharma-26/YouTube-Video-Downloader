from tkinter import *
from pytube import YouTube


# Download Function
def downloader():
    url = YouTube(str(link.get()))
    location1 = str(location.get())
    video = url.streams.get_highest_resolution()
    video.download(location1)
    Label(display, text=('DOWNLOADED in ' + location1), font='arial 16').place(x=305, y=300)


# Creation of Display Window
display = Tk()
display.geometry('800x400')
display.resizable(0, 0)
display.title("Youtube Video Downloader")
Label(display, text="Youtube Video Downloader", font='arial 26 bold').pack()

# Download Link
link = StringVar()
Label(display, text='Enter the Video Link here:', font='arial 16 bold').place(x=41, y=80)
link_enter = Entry(display, width=100, textvariable=link).place(x=40, y=110)

# Download Location
location = StringVar()
Label(display, text='Enter the Download Location here:', font='arial 16 bold').place(x=41, y=150)
location_enter = Entry(display, width=100, textvariable=location).place(x=40, y=180)

# Download Button
Button(display, text='DOWNLOAD', font='arial 16', bg='pale violet red', padx=2, command=downloader).place(x=320, y=250)

display.mainloop()
