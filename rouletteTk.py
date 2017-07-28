from Tkinter import *
import tkFont
from PIL import ImageTk, Image

import picamera

def exitProgram():
	print("Exit button pressed")
	win.quit()


def enter_num(event):
	myFont = tkFont.Font(family="Helvetica",size=80,weight="bold")
	camera.capture("wheel2.jpg")
	img2 = ImageTk.PhotoImage(Image.open("wheel2.jpg"))
	panel.configure(image=img2)
	panel.image=img2
	stats = win.create_text(650,100, text="stats",font=dayanaFont, fill="blue")
	if num2display:	
		#stats = win.create_text(650, 200, text=win.itemcget(num2display[0],"text"),font=myFont, fill="orange")
		#win.delete(statnum)
		win.itemconfig(statnum,text=str(len(num2display)))
		#statnum=win.create_text(650,200, text=str(len(num2display)),font=dayanaFont, fill="blue")
	numentered = v.get()
	if v.get() != "":
		# Make new text to show on screen and append to num2display list        
		num2display.append(win.create_text(alignNum(v.get()), 50, text=v.get(), font=myFont, fill=numColor(numentered)))
		# Display the new number and move the others down
		for index, rollvalue in enumerate(num2display):
			#check if the rollvalue is going to be half-off the screen
			# If so, just roll it entirely off the screen
			if win.coords(rollvalue)[1] > 1200:
				win.move(rollvalue,0,200)
			else:
				win.move(rollvalue,0,100)
			v.set("")
			win.update
	else:
		win.update

def numPadConvert(num2convert):
	if num2convert == "KP_Insert":
		return "0"
	if num2convert == "KP_End":
		return "1"
	if num2convert == "KP_Down":
		return "2"
	if num2convert == "KP_Next":
		return "3"
	if num2convert == "KP_Left":
		return "4"
	if num2convert == "KP_Begin":
		return "5"
	if num2convert == "KP_Right":
		return "6"
	if num2convert == "KP_Home":
		return "7"
	if num2convert == "KP_Up":
		return "8"
	if num2convert == "KP_Prior":
		return "9"
	else:
		 return num2convert


# For a number, determine what color it should be displayed as
def numColor(numStr):
	if numStr in ("1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"):
		return "red"
	if numStr in ("0","00"):
		return "green"
	else:
		return "black"

# For a number, determine what alignment (left or right) it should have
def alignNum(numStr):
	if numColor(numStr) in ("green","black"):
		return 150
	else:
		return 275


num2display=[]
master = Tk()
master.geometry('900x1440')
master.title("Roulette Spin Tracker v1.0")
tkrgb = "#%02x%02x%02x" % (255, 255, 230)
win = Canvas(master, width=900, height=1440, bg=tkrgb)
dayanaFont = tkFont.Font(family="Times",size=80,weight="bold")
statnum = win.create_text(650,200, text="",font=dayanaFont, fill="blue")
v = StringVar()
camera=picamera.PiCamera()
camera.resolution = (640, 480)
camera.iso=800
camera.exposure_mode = 'sports'
camera.capture("wheel.jpg")
entry_box = Entry(master, textvariable=v, width=5)
entry_box.place(rely=0.0, relx=0.0, x=0,y=0, anchor=NW)
entry_box.focus_set()
entry_box.bind('<Return>',enter_num)
wheelpic = ImageTk.PhotoImage(Image.open("wheel.jpg"))
panel = Label(master, image = wheelpic, height=480, width=450)
panel.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
win.pack()
        
	

mainloop()
