from random import randint

day = 0
switch = [1]*1000
smurf = [0]*101
todaysSmurf = 0
totalNumberSmurfs = 4
numberDays = 4

def selectSmurf():
	numberSmurfs = totalNumberSmurfs
	chosenSmurf = randint(1,numberSmurfs)
	return chosenSmurf

def updateMemory(chosenSmurf):
	smurf[chosenSmurf] = 1
	
def setLightSwitch(day,chosenSmurf):
	if smurf[chosenSmurf] == 0:
		if switch[day-1] == (-1)**(day-1):
			switch[day] = (-1)**day

	if smurf[chosenSmurf] == 1:
		if day <= numberDays:
			switch[day] = (-1)*((-1)**day)
		if day > numberDays:
			if switch[day-1] == (-1)**(day-1):
				switch[day] = ((-1)**day)*(-1)
			else:
				switch[day] = (-1)**day
			
def decide(switch,day,chosenSmurf):
	if day >= numberDays and smurf[chosenSmurf] == 0:
		if switch[day-1] == (-1)**(day-1):
			return 1
		else:
			return 0
	else:
		return 0

while (not(decide(switch,day,todaysSmurf))):
	day = day + 1
	print "day",day
	todaysSmurf = selectSmurf()
	print "smurf",todaysSmurf
	setLightSwitch(day,todaysSmurf)
	print "old light", switch[day-1]
	print "todays light",switch[day]
	print "decission", decide(switch,day,todaysSmurf)
	if decide(switch,day,todaysSmurf):
		updateMemory(todaysSmurf)
		print "FINISHED"
		print day
		print smurf
	else:
		updateMemory(todaysSmurf)
		print raw_input()

		
