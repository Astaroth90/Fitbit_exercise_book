import json

testplan = {
	"name": "Brust",
	"ex1": { "name":"test1","sets":"5","repeat":"12","weight":"20" } ,
	"ex2": { "name":"test2","sets":"5","repeat":"8","weight":"50" } ,
	"ex3": { "name":"test3","sets":"5","repeat":"10","weight":"25" } ,
}

with open('plan.json','w') as outfile
plan.dumps(testplan, outfile)
