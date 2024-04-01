import os
import math
from tkinter import *
from tkinter import ttk

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
            "path": root + "/" + name,
            "size": fileSize
            }
            fileList.append(fileDict)
    fileBoxCounterDef = 0
    for x in fileList:
        if(int(x["size"]) > int(minSizedShown)):
            
            fileBoxCounterDef += 1

            sizeVar = convert_size(int(x["size"]))
            filesBox.insert('', 'end', text="1", values=(x["name"], sizeVar, x["path"]))

def onDoubleclick(evt):
    print("Double Click")

def getPath():
    headPath = pathInput.get()

    addFilesToList(headPath)



headPath = ""

fileList = []

#Minimum and maximum sizes for files that are shown, will be used with the scale but doesn't work atm
minSizedShown = 0;
biggestSize = 0;

tkroot = Tk()
tkroot.title('Folder Manager')
tkroot.geometry("1000x600")

pathInput = Entry(tkroot)

pathSubmitButton = Button(tkroot, text="Get Path", command=getPath)

pathInput.pack()
pathSubmitButton.pack()

#filesBox = Listbox(tkroot, name="filesBox", width=35)
filesBox = ttk.Treeview(tkroot, column=("c1", "c2", "c3"), show='headings', height=20)

filesBox.column("# 1", anchor=CENTER)
filesBox.heading("# 1", text="Name")
filesBox.column("# 2", anchor=CENTER)
filesBox.heading("# 2", text="Size")
filesBox.column("# 3", anchor=CENTER)
filesBox.heading("# 3", text="Path")



#run onselect function when an item in the list has been selected
#https://stackoverflow.com/questions/6554805/getting-a-callback-when-a-tkinter-listbox-selection-is-changed
#filesBox.bind('<<ListboxSelect>>', onselect)

filesBox.bind('<ButtonRelease-1>', onselect)
#Double click will be used to open the folder where the file is located
filesBox.bind('<Double-1>', onDoubleclick)

#Labels and information panel for selected file
fileNameLabelText = StringVar()

fileInformationCanvas = Canvas(tkroot, height="250", width="250")
fileInformationCanvas.pack()

fileNameLabel = Label(fileInformationCanvas, textvariable=fileNameLabelText)
fileNameLabelText.set("File Size")
fileNameLabel.pack()


#setFileInformationGui

#Slider for minimun file size
#Doesn't work, gets the biggest value in bits
fileSizeSlider = Scale(tkroot, from_=0, to=biggestSize, orient=HORIZONTAL)

filesBox.pack()
fileSizeSlider.pack()

tkroot.mainloop()






