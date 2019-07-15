import json
#import Tkinter
from Tkinter import *

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
fenster.title("Nur ein Fenster")
fenster.mainloop()


print("End")