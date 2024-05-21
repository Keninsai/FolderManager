import os
import math
from tkinter import *
from tkinter import ttk
import platform
import tkinter.messagebox

def get_dir_size_old(path='.'):
    total = 0
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size_old(full_path)
    return total

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def getFileSize(file):
    fileSize = os.path.getsize(file)
    return(fileSize)

#OnSelect in file listbox
def onselect(evt):
    
    curItem = filesBox.focus()

#
#    #Change information labels in the GUI
    fileNameLabelText.set(filesBox.item(curItem)["values"][1])

def addFilesToList(choPath):
    fileList.clear()
    filesBox.delete(*filesBox.get_children())
    for root, dirs, files in os.walk(choPath):
        for name in files:
            fileSize = getFileSize(root + "/" + name)
            
            fileDict = {
            "name": name,
            "path": root,
            "size": fileSize,
            "fullPath": root + "/" + name
            }
            fileList.append(fileDict)
    fileBoxCounterDef = 0
    for x in fileList:
        if(int(x["size"]) > int(minSizedShown)):
            
            fileBoxCounterDef += 1

            sizeVar = convert_size(int(x["size"]))
            filesBox.insert('', 'end', text="1", values=(x["name"], sizeVar, x["path"]))

def onDoubleclick(evt):

    curItem = filesBox.focus()

    if(usersOS == "Linux"):
        foldername = os.path.realpath(filesBox.item(curItem)["values"][2])
        os.system('xdg-open "%s"' % foldername)
    
    else:
        print("Function not supported in " + usersOS)
        ttk.messagebox.showerror(title="Function not supported", message="Function not supported on " + usersOS)


def getPath():
    headPath = pathInput.get()

    addFilesToList(headPath)


#This is used for the system to use the right funciton
usersOS = platform.system()

headPath = ""

fileList = []

#Minimum and maximum sizes for files that are shown, will be used with the scale but doesn't work atm
minSizedShown = 0;
biggestSize = 0;

tkroot = Tk()
tkroot.title('Folder Manager')
tkroot.geometry("750x600")

#Use all the window space and center stuff
tkroot.grid_columnconfigure((0, 1, 2), weight=1)

#entryCanvas = Canvas(tkroot, height="250", width="250")
entryCanvas = Canvas(tkroot)
entryCanvas.grid(row=20, column=1, sticky='w')

pathInput = Entry(entryCanvas)
pathSubmitButton = Button(entryCanvas, text="Get Path", command=getPath)

pathInput.grid(row=1, column=1, padx=5, pady=5, sticky='w')
pathSubmitButton.grid(row=1, column=2, padx=5, pady=5, sticky='w')


filesCanvas = Canvas(tkroot,)
filesCanvas.grid(row=15, column=1)

#filesBox = Listbox(tkroot, name="filesBox", width=35)
filesBox = ttk.Treeview(filesCanvas, column=("c1", "c2", "c3"), show='headings', height=20)

filesBox.column("# 1", anchor=CENTER)
filesBox.heading("# 1", text="Name")
filesBox.column("# 2", anchor=CENTER)
filesBox.heading("# 2", text="Size")
filesBox.column("# 3", anchor=CENTER)
filesBox.heading("# 3", text="Path")

#Slider for minimun file size
#Doesn't work, gets the biggest value in bits
fileSizeSlider = Scale(filesCanvas, from_=0, to=biggestSize, orient=HORIZONTAL)

filesBox.grid(row=1, column=1)
fileSizeSlider.grid(row=2, column=1)


#run onselect function when an item in the list has been selected
#https://stackoverflow.com/questions/6554805/getting-a-callback-when-a-tkinter-listbox-selection-is-changed
#filesBox.bind('<<ListboxSelect>>', onselect)

filesBox.bind('<ButtonRelease-1>', onselect)
#Double click will be used to open the folder where the file is located
filesBox.bind('<Double-1>', onDoubleclick)

#Labels and information panel for selected file
fileNameLabelText = StringVar()
fileNameinfoLabelText = StringVar()

fileInformationCanvas = Canvas(tkroot, height="250", width="250")
fileInformationCanvas.grid(row=13, column=1)


fileNameinfoLabel = Label(fileInformationCanvas, textvariable=fileNameinfoLabelText)
fileNameinfoLabelText.set("Size: ")
fileNameinfoLabel.grid(row=10, column=1, sticky='w')

fileNameLabel = Label(fileInformationCanvas, textvariable=fileNameLabelText)
fileNameLabelText.set("0 b")
fileNameLabel.grid(row=10, column=2, sticky='w')

print(platform.platform())
print(platform.system())

#setFileInformationGui


tkroot.mainloop()






