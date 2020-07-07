from hashlib import sha256 as SHA256
from hashlib import sha512 as SHA512
from tkinter import Button as Button
from tkinter import Label as Label
from tkinter import Frame as Page
from tkinter import Text as TextBox
from tkinter import Tk as App

Font = lambda x : ('Courier', x) #lambda expression to select Courier font size

class TextToSHA(App): #class for main app
	def __init__(self):
		super().__init__() #constructor of super class
		self.maxsize(1080, 1920) #setting max size

		HEIGHT = int(self.winfo_screenheight() * 0.93)
		WIDTH = int(self.winfo_screenheight() * 0.5625)
		Sizes = str(WIDTH) + 'x' + str(HEIGHT)
		X = int((self.winfo_screenwidth() - WIDTH) / 2)
		#Y = int((self.winfo_screenheight() - HEIGHT) / 2)
		Pos = '+' + str(X) + '+0'
		self.geometry(Sizes + Pos)
		
		self.Main = Convert(self)
		
		self.PlaceWidgets()
		
		
	def PlaceWidgets(self):
		self.Main.place(relx =0, rely = 0, relwidth = 1, relheight =1)

	def ClipBoard(self, Input):
		self.clipboard_clear()
		self.clipboard_append(Input)
		self.update()

class Convert(Page):
	def __init__(self, Parent = None):
		self.Parent = Parent
		super().__init__(Parent)
		self.bg = '#4f4f4f'
		self.fg = '#ffffff'
		self.config(bg = self.bg)
		
		self.TopLabel = Label(self)
		self.TopLabel.config(bg = self.bg)
		self.TopLabel.config(fg = self.fg)
		TopLabelText = 'Hash your text to SHA'
		self.TopLabel.config(text = TopLabelText)
		self.TopLabel.config(font = Font(14))
		
		self.TextInput = TextBox(self)
		self.TextInput.config(bg = '#8f8f8f')
		self.TextInput.config(fg = self.fg)
		self.TextInput.config(font = Font(12))
		
		self.ToSHA256 = Button(self)
		self.ToSHA256.config(bg = '#8f8f8f')
		self.ToSHA256.config(fg = self.fg)
		self.ToSHA256.config(text = 'To SHA 256')
		self.ToSHA256.config(font = Font(12))
		self.ToSHA256.config(command = lambda : self.SHA256())
		
		self.ToSHA512 = Button(self)
		self.ToSHA512.config(bg = '#8f8f8f')
		self.ToSHA512.config(bg = '#8f8f8f')
		self.ToSHA512.config(text = 'To SHA512')
		self.ToSHA512.config(font = Font(12))
		self.ToSHA512.config(command = lambda : self.SHA512())
		
		self.TextOutput = TextBox(self)
		self.TextOutput.config(bg = '#8f8f8f')
		self.TextOutput.config(fg = self.fg)
		self.TextOutput.config(font = Font(12))
		self.TextOutput.config(state = 'disabled')
		
		self.Copy = Button(self)
		self.Copy.config(bg = '#8f8f8f')
		self.Copy.config(fg = self.fg)
		self.Copy.config(font = Font(12))
		self.Copy.config(text = 'Copy it')
		self.Copy.config(command = lambda : self.Parent.ClipBoard(self.TextOutput.get('1.0', 'end')))
		
		self.PlaceWidgets()
		
	def PlaceWidgets(self):
		self.TopLabel.place(anchor = 'n', relx = 0.5, relwidth = 1, relheight = 0.08)
		self.TextInput.place(anchor = 'n', relx = 0.5, rely = 0.08, relwidth = 0.95, relheight = 0.35)
		self.ToSHA256.place(anchor = 'n', relx = 0.25, rely = 0.45, relwidth = 0.4, relheight = 0.05)
		self.ToSHA512.place(anchor = 'n', relx = 0.75, rely = 0.45, relwidth = 0.4, relheight = 0.05)
		self.TextOutput.place(anchor = 'n', relx = 0.5, rely = 0.52, relwidth = 0.95, relheight = 0.35)
		self.Copy.place(anchor = 'n', relx = 0.5, rely = 0.89, relwidth = 0.95, relheight = 0.05)
			
	def SHA256(self):
		self.TextOutput.config(state = 'normal')
		self.TextOutput.delete('1.0',  'end')
		Input = self.TextInput.get('1.0',  'end')
		Input = Input.encode()
		Hash = SHA256(Input).hexdigest().upper()
		self.TextOutput.insert('1.0', Hash)
		self.TextOutput.config(state = 'disabled')
		
	def SHA512(self):
		self.TextOutput.config(state = 'normal')
		self.TextOutput.delete('1.0',  'end')
		Input = self.TextInput.get('1.0', 'end')
		Input = Input.encode()
		Hash = SHA512(Input).hexdigest().upper()
		self.TextOutput.insert('1.0', Hash)
		self.TextOutput.config(state = 'disabled')
		
if __name__ == '__main__':
	App = TextToSHA()
	App.mainloop()