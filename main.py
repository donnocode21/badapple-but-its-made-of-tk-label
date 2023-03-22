from tkinter import *
try: from PIL.Image import open
except: from Image import open
from cv2 import VideoCapture, imencode, resize
from io import BytesIO
import time

root = Tk()
root.geometry("300x300")
root.title("Bad Apple!!")

index = 0
index_rows = 0
FPS = 30
FRAME_DISPLAY = "Frame 0"
content = ["", "", "", "", "", "", "", "", ""]
vidcap = VideoCapture('./video.mp4')
success, image = vidcap.read()

def I2T(File):
	global content
	im = open(File)
	(w, h) = im.size
	mim = im.convert("1")
	data = list(mim.getdata())
	counter = 0
	row = 0
	field = True
	for pixel in data:
		if field:
			if pixel > 127: content[row] = content[row] + "⬜"
			else: content[row] = content[row] + "⬛"
		counter = counter + 1
		if counter >= w:
			counter = 0
			if field: row += 1
			field = not field

def start():
	global index
	global success
	global index_rows
	global image
	global vidcap
	global FPS
	global FRAME_DISPLAY

	while success:
		time.sleep(1 / FPS)
		index += 1
		I2T(BytesIO(imencode(".jpg", resize(image, (18, 9), interpolation = 3))[1]))
		for index_rows in range(1,10):
			changeLabel(index_rows, content[index_rows - 1]) # Missing Subtract of One.
			content[index_rows - 1] = "" #Clear a index of content
		FRAME_DISPLAY = "Frame " + str(index)
		f.config(text=FRAME_DISPLAY)
		success, image = vidcap.read()

def changeLabel(__id__, newlabel):
    if __id__ == 1:
        l1.config(text=newlabel)
    elif __id__ == 2:
        l2.config(text=newlabel)
    elif __id__ == 3:
        l3.config(text=newlabel)
    elif __id__ == 4:
        l4.config(text=newlabel)
    elif __id__ == 5:
        l5.config(text=newlabel)
    elif __id__ == 6:
        l6.config(text=newlabel)
    elif __id__ == 7:
        l7.config(text=newlabel)
    elif __id__ == 8:
        l8.config(text=newlabel)
    elif __id__ == 9:
        l8.config(text=newlabel)
    else:
        print("NO VARIABLE!")

l1 = Label(text = "content row 1")
l2 = Label(text = "content row 2")
l3 = Label(text = "content row 3")
l4 = Label(text = "content row 4")
l5 = Label(text = "content row 5")
l6 = Label(text = "content row 6")
l7 = Label(text = "content row 7")
l8 = Label(text = "content row 8")
l9 = Label(text = "content row 9")
f = Label(text = "Frame (number)")
start_btn = Button(root,
                   text = "Start",
                   command = start)

l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()
l8.pack()
l9.pack()
f.pack()
start_btn.pack()

mainloop()
