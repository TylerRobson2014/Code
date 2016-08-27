from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import sys
from string import ascii_uppercase
import json
import Image

def draw_sharp(a):
	m = max(a)
	for i in xrange(len(a)):
		if i % 20:
			if a[i] > 0: k = 1
			if a[i] == 0: k = 0
			print k,
		else:
			print ""



def definput(s,index):
	print "/home/steve/Downloads/training/upper/"+s+"/"+str(index)+".gif"
	foo = Image.open("/home/steve/Downloads/training/upper/"+s+"/"+str(index)+".gif")
	data = foo.getdata()
	return data

def inputlayer_sharp(array):
	node = []
	for i in xrange(len(array)):
		if array[i] > 0: kk = 1
		if array[i] == 0: kk = 0
		node.append(kk)
	node.append(1)
	return node

def inputlayer_blur(array):
	node = []
	m = max(array)
	for i in xrange(len(array)):
		kk = array[i]/m
		node.append(kk)
	node.append(1)
	return node



def hiddenlayer():
	global numberHidden,numberInput
	h = [0 for x in xrange(numberHidden+1)]
	h[numberHidden] = 1
	wih = [[random.uniform(-0.5,0.5) for x in xrange(numberInput+1)] for y in xrange(numberHidden+1)]
			
	return h,wih
	
def outputlayer():
	global numberHidden,numberOutput
	o = [0 for x in xrange(numberOutput)]
	who = [[random.uniform(-0.5,0.5) for x in xrange(numberHidden+1)] for y in xrange(numberOutput)]

	return o,who

def netinput(nodes,weight,j,MinWeight):
	# pass input nodes, weights between input and next layer and node j
	# need to do this for each j of next layer
	netin = 0
	for i in xrange(len(nodes)):
		if abs(weight[j][i]) < MinWeight: weight[j][i] = 0.0  
		netin +=  weight[j][i] * nodes[i]
	return netin
	
def activation(netin):
	activ = 1/(1 + math.exp(-1*netin))
	return activ

def activation1(netin):
	activ = math.exp(netin)
	return activ

def trainNet(Required_output):
	
	global HLW,OLW,inode
	global hiddenL,outL,Error
	global numberHidden,numberInput,numberOutput

	MinWeight = 0.0

	Running = True
	while Running:
		
		#print OLW[6][7]
		#print HLW
		#raw_input()
		
		# **** Hidden Layer ****

		# Get net input of each hidden node
		net_input_H = []
		for j in xrange(len(hiddenL)):
			net_input_H.append(netinput(inode,HLW,j,MinWeight))
		#Get the activation of each hidden node
		activation_H = []	
		for j in xrange(len(hiddenL)):
			aa = activation(net_input_H[j])
			activation_H.append(aa)

		#print activation_H
			
		# **** Output Layer ****

		# Get net input of each hidden node
		net_input_O = []
		for j in xrange(len(outL)):
			net_input_O.append(netinput(activation_H,OLW,j,MinWeight))
		#Get the activation of each hidden node
		activation_O = []	
		for j in xrange(len(outL)):
			activation_O.append(activation(net_input_O[j]))
			
		#**** Check result ****
		testo = []
		for kk in activation_O:
			r = int(round(kk,1))
			testo.append(r)
			
		#print "Check results"
		#print testo
		#print activation_O
		#print Required_output
		
		error_function = 0
		
		for t in xrange(len(Required_output)):
			error_function += 0.5 * (Required_output[t] - activation_O[t])**2
		
		print error_function
		if not(round(error_function,4) < Error):

			errorGradO = [0 for x in xrange(numberOutput)]
			deltaWO = [[0 for x in xrange(numberHidden+1)] for x in xrange(numberOutput)]

			errorGradH = [0 for x in xrange(numberHidden+1)]
			deltaWH = [[0 for x in xrange(numberInput+1)] for x in xrange(numberHidden+1)]



			for j in xrange(numberOutput):
				for i in xrange(numberHidden+1):
					errorGradO[j] = activation_O[j] * (1 - activation_O[j]) * (Required_output[j] - activation_O[j])
					deltaWO[j][i] = 0.3 * activation_H[i] * errorGradO[j]			
					OLW[j][i] = OLW[j][i] + deltaWO[j][i]

			for j in xrange(numberHidden+1):
				for k in xrange(numberOutput):
					errorGradH[j] += activation_H[j] * (1 - activation_H[j]) * (errorGradO[k]*OLW[k][j])
				for i in xrange(numberInput+1):
					deltaWH[j][i] = 0.3 * inode[i] * errorGradH[j]	
					HLW[j][i] = HLW[j][i] + deltaWH[j][i]
		
		else:
			Running = False

def testNet(targetLetter):
	
	global HLW,OLW,inode
	global hiddenL,outL
	global correct, Tcorrect, Ccorrect
	
	MinWeight = 0.0001#0.15
	
	# **** Hidden Layer ****

	# Get net input of each hidden node
	net_input_H = []
	for j in xrange(len(hiddenL)):
		net_input_H.append(netinput(inode,HLW,j,MinWeight))
	#Get the activation of each hidden node
	activation_H = []	
	for j in xrange(len(hiddenL)):
		aa = activation(net_input_H[j])

		activation_H.append(aa)
		
	# **** Output Layer ****

	# Get net input of each hidden node
	net_input_O = []
	for j in xrange(len(outL)):
		net_input_O.append(netinput(activation_H,OLW,j,MinWeight))
	#Get the activation of each hidden node
	activation_O = []	
	for j in xrange(len(outL)):
		activation_O.append(activation(net_input_O[j]))
		
	#**** Check result ****
	net_output = []
	
	m = max(activation_O)
#	for kk in activation_O:
#		if kk/m >= 0.9: r = 1
#		if kk/m < 0.9: r = 0
	r = []
	t = []
	total_sum = sum(activation_O)
	for kk in activation_O:
		r = int(round(kk,0))
		t = (round(kk,3))
		if t > 0.5:
			t = 1
		else:
			t = 0
		#testo.append(r)

		net_output.append(t)
		
	print "Check results"
	print "Result we want:"
	print targetLetter
	print "Result we have:"
	print net_output
	raw_input()
	
	if net_output == targetLetter:
		correct += 1
		Tcorrect += 1
		Ccorrect += 1
	
	#print Required_output
		
def saveWeights(weightsH,weightsO):
	target = open("weightsH.txt","w")
	json.dump(weightsH, target)
	target.close()
	target = open("weightsO.txt","w")
	json.dump(weightsO, target)
	target.close()				

def conv(letter):
	return ord(letter)-64

numberHidden = 260
numberInput = 400
numberOutput = 26
Error = 0.001

# Prime the hidden layer & weights
(hiddenL,HLW) = hiddenlayer()
# Prime the output layer & weights
(outL,OLW) = outputlayer()

L = {"A":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}#A
L["B"]=[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#B
L["C"]=[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#C
L["D"]=[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#D
L["E"]=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#E
L["F"]=[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#F
L["G"]=[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#G
L["H"]=[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#H
L["I"]=[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#I
L["J"]=[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#J
L["K"]=[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#K
L["L"]=[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#L
L["M"]=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]#M
L["N"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]#N
L["O"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]#O
L["P"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]#P
L["Q"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]#Q
L["R"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]#R
L["S"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]#S
L["T"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]#T
L["U"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]#U
L["V"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]#V
L["W"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]#W
L["X"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]#X
L["Y"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]#Y
L["Z"]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]#Z

Li = []
for i in ascii_uppercase:
	Li.append(i)
random_Li = random.sample(Li,len(Li))

option = raw_input("Train net (1), run the net (2) or check weights (3)?")
if option == "1":
	
	TrainPerformanceFile = open("TrainPerformance.txt","w")
	
	for trainCount in xrange(5):
		for j in xrange(5):
			#for i in xrange(1):
			for i in xrange(len(random_Li)):
				inputarray = definput(random_Li[i],j)
				# Feed in the input
				inode = inputlayer_sharp(inputarray)
				print random_Li[i],j
				trainNet(L[random_Li[i]])

	saveWeights(HLW,OLW)
	TrainPerformanceFile.close()
		
elif option == "2":
	
	HiddenWeightsFile = open("weightsH.txt")
	HLW = json.load(HiddenWeightsFile)
	HiddenWeightsFile.close()
	OutputWeightsFile = open("weightsO.txt")
	OLW = json.load(OutputWeightsFile)
	OutputWeightsFile.close()
	
	RunPerformanceFile = open("RunPerformance.txt","w")
	
	# Test the net
	print "************"
	print "Test the net"
	print "************"
	count = 0
	Tcorrect = 0
	Ccorect = 0
	Ctotal = 0
	Ttotal = 0
	a = []
	for i in ascii_uppercase:
		print i
		Ctotal = 0
		Ccorrect = 0
		for j in xrange(50,60):
			correct = 0
			inputarray = definput(i,j)
			inode = inputlayer_sharp(inputarray)
			#print inputarray
			testNet(L[i])
			Ttotal += 1
			Ctotal += 1
			a.append([conv(i),j,correct])

		print "****************"
		print "Correct : ",i, (Ccorrect/Ctotal)*100,"%"
		print "****************"		


	print "****************"
	print "Correct : ", (Tcorrect/Ttotal)*100,"%"
	print "****************"
	
	json.dump(a, RunPerformanceFile)
	RunPerformanceFile.close()
	
elif option == "3":

	HiddenWeightsFile = open("weightsH.txt")
	HLW = json.load(HiddenWeightsFile)
	HiddenWeightsFile.close()
	OutputWeightsFile = open("weightsO.txt")
	OLW = json.load(OutputWeightsFile)
	OutputWeightsFile.close()
	
	plt.plot(HLW)
	plt.ylabel('Hidden Weights')
	plt.show()

	plt.plot(OLW)
	plt.ylabel('Output Weights')
	plt.show()

else:
	print "You didnt select one of the options"
