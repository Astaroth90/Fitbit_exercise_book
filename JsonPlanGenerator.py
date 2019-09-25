import json
#import Tkinter
from tkinter import *

def button_quit_action(): fenster.quit()
#def addButton_action()
	
def button_create_action():
	print("create")
	
print("Start")
testplan = {}
testplan['name'] = []
testplan['exercise'] = []
testplan['name'].append('Brust')
testplan['exercise'].append({
	"name":"test1",
	"sets":"5",
	"repeat":"12"
	,"weight":"20"
})
testplan['exercise'].append({
	"name":"test2",
	"sets":"5",
	"repeat":"8",
	"weight":"50" 
})
testplan['exercise'].append({
	"name":"test3",
	"sets":"5",
	"repeat":"10",
	"weight":"25" 
}) 
print("TestPlan")
print(testplan)

plan = json.dumps(testplan)
print(plan)
file = open('plan.txt', 'w')	

file.write(plan)

file.close()

fenster = Tk()
fenster.title("Create your own Plan")

create_button = Button(fenster, text="Create", command= button_create_action)

exit_button = Button(fenster, text="Close", command=button_quit_action)

start_label = Label(fenster, text="Plan")
title_label = Label(fenster,text="Name")
repeat_label = Label(fenster,text="Repeat")
sets_label = Label(fenster,text="Sets")
weight_label = Label(fenster,text="Weight")
list_label = Label(fenster,text="hier steht \n\
eine Liste aller \n\
Ubungen")

name_entry = Entry(fenster, bd=5, width=40)
repeat_entry = Entry(fenster, bd=5, width= 40)
sets_entry = Entry(fenster, bd=5, width=40)
weight_entry = Entry(fenster,bd=5, width=40)

start_label.grid(row=0, column=1)
title_label.grid(row=1, column=1)
name_entry.grid(row=1, column=2,columnspan=2)
list_label.grid(row=1,column=0, rowspan=4)
sets_label.grid(row=2,column=1)
sets_entry.grid(row=2,column=2,columnspan=2)
repeat_label.grid(row=3,column=1)
repeat_entry.grid(row=3,column=2,columnspan=2)
weight_label.grid(row=4,column=1)
weight_entry.grid(row=4,column=2,columnspan=2)

exit_button.grid(row=5, column=1)


fenster.mainloop()


print("End")