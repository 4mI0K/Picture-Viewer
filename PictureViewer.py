from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Prozorcic")

# Images
img = ImageTk.PhotoImage(Image.open("web.png"))
img1 = ImageTk.PhotoImage(Image.open("webp.png"))
img2 = ImageTk.PhotoImage(Image.open("pro.png"))
img3 = ImageTk.PhotoImage(Image.open("coding.png"))
img4 = ImageTk.PhotoImage(Image.open("data.png"))


img_lst = [img, img1, img2, img3, img4]

label = Label(image=img)
label.grid(row=0, column=0, columnspan=3)


# Button Functions
def forward(img_num):
	global label
	global right
	global left
	label.grid_forget()
	label = Label(image=img_lst[img_num-1])
	right = Button(root, text=">>", command=lambda: forward(img_num+1))
	left = Button(root, text="<<", command=lambda: back(img_num-1))
	
	if img_num == 5:
		right = Button(root, text=">>", state=DISABLED)

	label.grid(row=0, column=0, columnspan=3)
	left.grid(row=1, column=0)
	right.grid(row=1, column=2)

def back(img_num):
	global label
	global right
	global left
	label.grid_forget()
	label = Label(image=img_lst[img_num-1])
	right = Button(root, text=">>", command=lambda: forward(img_num+1))
	left = Button(root, text="<<", command=lambda: back(img_num-1))

	if img_num == 1:
		left = Button(root, text="<<", state=DISABLED)

	label.grid(row=0, column=0, columnspan=3)
	left.grid(row=1, column=0)
	right.grid(row=1, column=2)

# Buttons
exit_button = Button(root, text="Exit Program", command=root.quit)
right = Button(root, text=">>", command=lambda: forward(2))
left = Button(root, text="<<", command=back, state=DISABLED)

exit_button.grid(row=1, column=1)
left.grid(row=1, column=0)
right.grid(row=1, column=2)

root.mainloop()
