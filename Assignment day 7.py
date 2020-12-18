from tkinter import *
from pytube import YouTube
a= Tk()
a.geometry('480x320')
a.resizable(0,0)
a.title("YOUTUBE VIDEO DOWNLOADER")
Label(a,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
Label(a, text = 'Paste the video link:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(a, width = 70,textvariable = link).place(x = 32, y = 90)
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(a, text = 'Sucessfully Downloaded',font  = 'arial 10').place(x= 180 , y = 210)  
Button(a,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 5, command = Downloader).place(x=180 ,y = 150)
a.mainloop()