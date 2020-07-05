from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size=0

#for updating download %
def progress(chunk=None,file_handle=None,remaining=None):
    file_downloaded=(file_size-remaining)
    per=(file_downloaded/file_size)*100
    dBtn.config(text="{:00.0f} % downloaded".format(per))

def startdownload():
    global file_size
    try:
        url = urlField.get()
        #changing btn text
        dBtn.config(text='Please Wait...')
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return

        ob = YouTube(url,on_progress_callback=progress)
        strm = ob.streams.first()
        file_size=strm.filesize
        vTitle.config(text=ob.title)
        vTitle.pack(side=TOP)
        strm.download(path_to_save_video)

        print("done")
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Download Finised","Download successful")
        vTitle.pack_forget()
    except Exception as e:
        print(e)
        print("Something went wrong")

def StartDownloadThread():
    thread=Thread(target=startdownload)
    thread.start()


#Gui building
main=Tk()
main.title("My Youtube Downloader")
main.iconbitmap('download.ico')
main.geometry("500x600")

#heading box

urlField=Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)

#DOWNLOAD BTN
dBtn=Button(main,text="start download",font=("verdana",18),relief="ridge",command=StartDownloadThread)
dBtn.pack(side=TOP,pady=10)

#video title
vTitle=Label(main,text="Video Title")
main.mainloop()