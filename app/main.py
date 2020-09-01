import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk
import cv2

from services.convolution import getConv, resizeOutput


class GUI(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.master = master
		self.filename = ''
		self.viewInput()

	def viewInput(self):
		self.label_browse = tk.Label(self.master, text = '')
		self.label_browse.grid(row=0, column=0, padx=5, pady=5)

		self.button_browse = tk.Button(self.master, text='Browse An Image', command=self.fileDialog)
		self.button_browse.grid(row=0, column=1, padx=5, pady=5)

		self.kernel = tk.StringVar()
		self.input_kernel = tk.Entry(self.master, textvariable=self.kernel)
		self.input_kernel.grid(row=1, column=0, padx=5, pady=5)

		self.button_process = tk.Button(self.master, text='Process', command=self.process)
		self.button_process.grid(row=1, column=1, padx=5, pady=5)

	def fileDialog(self):
		self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
		(("jpeg files","*.jpg"),("all files","*.*")) )
		self.label_browse.configure(text = self.filename)

		cv_img = cv2.imread(self.filename)
		self.cv_img = cv2.resize(cv_img, (400, 400), interpolation=cv2.INTER_AREA)

		self.canvas = tk.Canvas(self.master, width=400, height=400)
		self.canvas.grid(row=2, column=0, rowspan=2, columnspan=2)
		self.photo = ImageTk.PhotoImage(image = Image.fromarray(self.cv_img))
		self.canvas.create_image(0, 0, image=self.photo, anchor='nw')

	def process(self):
		if self.filename and self.input_kernel.get():
			if int(self.input_kernel.get()):
				self.viewConv()
				self.viewInfo()
			else:
				messagebox.showinfo(title='Info', message='Kernel must be a number')
		else:
			messagebox.showinfo(title='Info', message='Image and kernel size must be filled')

	def viewInfo(self):
		self.label_info = tk.Label(self.master, text = '')
		info = 'Visualization of convolution process from 3 channels to 9 channels with kernel size '+self.input_kernel.get()+'x'+self.input_kernel.get()
		self.label_info.configure(text=info)
		self.label_info.grid(row=0, column=3, columnspan=3, rowspan=2)

	def viewConv(self):
		kernel = self.input_kernel.get()
		self.data_conv = getConv(self.cv_img, 9, int(kernel))

		conv1 = resizeOutput(self.data_conv, 0)
		self.photo_conv1 = ImageTk.PhotoImage(image = Image.fromarray(conv1))
		self.canvas1 = tk.Canvas(self.master, width=200, height=200)
		self.canvas1.grid(row=2, column=2)
		self.canvas1.create_image(0, 0, image=self.photo_conv1, anchor='nw')

		conv2 = resizeOutput(self.data_conv, 1)
		self.photo_conv2 = ImageTk.PhotoImage(image = Image.fromarray(conv2))
		self.canvas2 = tk.Canvas(self.master, width=200, height=200)
		self.canvas2.grid(row=2, column=3)
		self.canvas2.create_image(0, 0, image=self.photo_conv2, anchor='nw')

		conv3 = resizeOutput(self.data_conv, 2)
		self.photo_conv3 = ImageTk.PhotoImage(image = Image.fromarray(conv3))
		self.canvas3 = tk.Canvas(self.master, width=200, height=200)
		self.canvas3.grid(row=2, column=4)
		self.canvas3.create_image(0, 0, image=self.photo_conv3, anchor='nw')

		conv4 = resizeOutput(self.data_conv, 3)
		self.photo_conv4 = ImageTk.PhotoImage(image = Image.fromarray(conv4))
		self.canvas4 = tk.Canvas(self.master, width=200, height=200)
		self.canvas4.grid(row=3, column=2)
		self.canvas4.create_image(0, 0, image=self.photo_conv4, anchor='nw')

		conv5 = resizeOutput(self.data_conv, 4)
		self.photo_conv5 = ImageTk.PhotoImage(image = Image.fromarray(conv5))
		self.canvas5 = tk.Canvas(self.master, width=200, height=200)
		self.canvas5.grid(row=3, column=3)
		self.canvas5.create_image(0, 0, image=self.photo_conv5, anchor='nw')

		conv6 = resizeOutput(self.data_conv, 5)
		self.photo_conv6 = ImageTk.PhotoImage(image = Image.fromarray(conv6))
		self.canvas6 = tk.Canvas(self.master, width=200, height=200)
		self.canvas6.grid(row=3, column=4)
		self.canvas6.create_image(0, 0, image=self.photo_conv6, anchor='nw')

		conv7 = resizeOutput(self.data_conv, 6)
		self.photo_conv7 = ImageTk.PhotoImage(image = Image.fromarray(conv7))
		self.canvas7 = tk.Canvas(self.master, width=200, height=200)
		self.canvas7.grid(row=4, column=2)
		self.canvas7.create_image(0, 0, image=self.photo_conv7, anchor='nw')

		conv8 = resizeOutput(self.data_conv, 7)
		self.photo_conv8 = ImageTk.PhotoImage(image = Image.fromarray(conv8))
		self.canvas8 = tk.Canvas(self.master, width=200, height=200)
		self.canvas8.grid(row=4, column=3)
		self.canvas8.create_image(0, 0, image=self.photo_conv8, anchor='nw')

		conv9 = resizeOutput(self.data_conv, 8)
		self.photo_conv9 = ImageTk.PhotoImage(image = Image.fromarray(conv9))
		self.canvas9 = tk.Canvas(self.master, width=200, height=200)
		self.canvas9.grid(row=4, column=4)
		self.canvas9.create_image(0, 0, image=self.photo_conv9, anchor='nw')


if __name__ == '__main__':
	root = tk.Tk()
	root.title('Convolution Visualization App')
	master = GUI(root)
	root.mainloop()