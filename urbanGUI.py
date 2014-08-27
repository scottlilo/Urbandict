import urbandict
from Tkinter import *
index = 0
word = '  '
LoopEnd = False

def urbandefine():
	word = userword.get()
	data = urbandict.define(word)
	word = data[index]['word']
	definition =  data[index]['def']
	example = data[index]['example']	
	labelText.set(definition) 
	widgetLabelResult.pack()


def changeLabel():
	name = "Thanks for the click " + yourName.get()
	labelText.set(name)
	yourName.delete(0, END)
	yourName.insert(0, "My name is Derek")






app = Tk()
app.title("GUI Example")
app.geometry('450x450+200+200')
app.configure(background = 'black')


labelGreeting = StringVar(None)
labelGreeting.set("Enter a Word")
widgetgreet = Label(app, textvariable=labelGreeting, height=2,bg="red")
widgetgreet.pack()

userword = StringVar(None)
widgetwordprompt = Entry(app, textvariable=userword,bg="grey")
widgetwordprompt.pack()

labelText = StringVar(None)
labelText.set("Your definition will go here.")
widgetLabelResult = Label(app, textvariable=labelText, height=20, width = 200, bg="red")
widgetLabelResult.pack()

widgetbutton1 = Button(app, text="Look up Definition", width=20,command=urbandefine,bg="red")
widgetbutton1.pack(side='bottom',padx=15,pady=15)

app.mainloop()
