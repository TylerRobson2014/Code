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

def draw(a):
	for i in xrange(8):
		for j in xrange(8):
			print a[i][j],
		print ""

def definput_old(s):
	a = [[0 for y in xrange(8)] for x in xrange(8)]
	if s == "A":
		a[1][3] = 1
		a[1][4] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][3] = 1
		a[4][4] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][5] = 1
	if s == "B":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "C":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "D":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "E":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "F":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[6][2] = 1
	if s == "G":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "H":
		a[1][2] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][5] = 1
	if s == "I":
		a[1][2] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[6][2] = 1
	if s == "J":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][5] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "K":
		a[1][2] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[6][2] = 1
		a[3][3] = 1
		a[2][4] = 1
		a[1][5] = 1
		a[4][4] = 1
		a[5][5] = 1
		a[6][6] = 1		
	if s == "L":
		a[1][2] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "M":
		a[1][1] = 1
		a[2][1] = 1
		a[3][1] = 1
		a[4][1] = 1
		a[5][1] = 1
		a[6][1] = 1
		a[1][6] = 1
		a[2][6] = 1
		a[3][6] = 1
		a[4][6] = 1
		a[5][6] = 1
		a[6][6] = 1
		a[1][3] = 1
		a[1][5] = 1
		a[2][4] = 1
	if s == "N":
		a[1][1] = 1
		a[2][1] = 1
		a[3][1] = 1
		a[4][1] = 1
		a[5][1] = 1
		a[6][1] = 1
		a[1][6] = 1
		a[2][6] = 1
		a[3][6] = 1
		a[4][6] = 1
		a[5][6] = 1
		a[6][6] = 1
		a[3][3] = 1
		a[4][4] = 1
		a[5][5] = 1
	if s == "O":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "P":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[6][2] = 1
	if s == "Q":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
		a[6][6] = 1
		a[6][7] = 1
	if s == "R":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][5] = 1
	if s == "S":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][5] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "T":
		a[1][2] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "U":
		a[1][2] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][2] = 1
		a[5][5] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	if s == "V":
		a[1][2] = 1
		a[1][5] = 1
		a[2][2] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[4][2] = 1
		a[4][5] = 1
		a[5][3] = 1
		a[5][4] = 1
		a[6][3] = 1
		a[6][4] = 1
	if s == "W":
		a[1][1] = 1
		a[2][1] = 1
		a[3][1] = 1
		a[4][1] = 1
		a[5][1] = 1
		a[6][1] = 1
		a[5][2] = 1
		a[4][3] = 1
		a[5][4] = 1
		a[6][5] = 1
		a[5][5] = 1
		a[4][5] = 1
		a[3][5] = 1
		a[2][5] = 1
		a[1][5] = 1
	if s == "X":
		a[1][1] = 1
		a[2][2] = 1
		a[3][3] = 1
		a[4][4] = 1
		a[5][5] = 1
		a[6][6] = 1
		a[6][1] = 1
		a[5][2] = 1
		a[4][3] = 1
		a[3][4] = 1
		a[2][5] = 1
		a[1][6] = 1
	if s == "Y":
		a[1][2] = 1
		a[2][3] = 1
		a[3][4] = 1
		a[1][5] = 1
		a[2][5] = 1
		a[1][6] = 1
		a[4][4] = 1
		a[5][4] = 1
		a[6][4] = 1
	if s == "Z":
		a[1][2] = 1
		a[1][3] = 1
		a[1][4] = 1
		a[1][5] = 1
		a[2][5] = 1
		a[3][2] = 1
		a[3][3] = 1
		a[3][4] = 1
		a[3][5] = 1
		a[4][2] = 1
		a[5][2] = 1
		a[6][2] = 1
		a[6][3] = 1
		a[6][4] = 1
		a[6][5] = 1
	return a
	

def inputlayer(array):
	node = []
	for i in xrange(8):
		for j in xrange(8):
			node.append(array[i][j])
	node.append(1)
	return node

def hiddenlayer():
	h = [0 for x in xrange(97)]
	h[96] = 1
	wih = [[random.uniform(-0.5,0.5) for x in xrange(65)] for y in xrange(97)]
			
	return h,wih
	
def outputlayer():
	o = [0 for x in xrange(8)]
	who = [[random.uniform(-0.5,0.5) for x in xrange(97)] for y in xrange(8)]

	return o,who

def netinput(nodes,weight,j):
	# pass input nodes, weights between input and next layer and node j
	# need to do this for each j of next layer
	netin = 0
	for i in xrange(len(nodes)):
		netin +=  weight[j][i] * nodes[i]
	return netin
	
def activation(netin):
	activ = 1/(1 + math.exp(-1*netin))
	return activ

def trainNet(Required_output):
	
	global HLW,OLW,inode
	global hiddenL,outL

	Running = True
	while Running:
		
		#print OLW[6][7]
		#print HLW
		#raw_input()
		
		# **** Hidden Layer ****

		# Get net input of each hidden node
		net_input_H = []
		for j in xrange(len(hiddenL)):
			net_input_H.append(netinput(inode,HLW,j))
		#Get the activation of each hidden node
		activation_H = []	
		for j in xrange(len(hiddenL)):
			aa = activation(net_input_H[j])
		#	if aa > 0.99:
		#		aa = 1
		#	else:
		#		aa = 0
			activation_H.append(aa)

		#print activation_H
			
		# **** Output Layer ****

		# Get net input of each hidden node
		net_input_O = []
		for j in xrange(len(outL)):
			net_input_O.append(netinput(activation_H,OLW,j))
		#Get the activation of each hidden node
		activation_O = []	
		for j in xrange(len(outL)):
			activation_O.append(activation(net_input_O[j]))
			
		#**** Check result ****
		testo = []
		for kk in activation_O:
			r = int(round(kk,2))
			testo.append(r)
			
		#print "Check results"
		#print testo
		#print activation_O
		#print Required_output
		
		if not(testo == Required_output):

			errorGradO = [0 for x in xrange(8)]
			deltaWO = [[0 for x in xrange(97)] for x in xrange(8)]

			errorGradH = [0 for x in xrange(97)]
			deltaWH = [[0 for x in xrange(65)] for x in xrange(97)]



			for j in xrange(8):
				for i in xrange(97):
					errorGradO[j] = activation_O[j] * (1 - activation_O[j]) * (Required_output[j] - activation_O[j])
					deltaWO[j][i] = 0.3 * activation_H[i] * errorGradO[j]			
					OLW[j][i] = OLW[j][i] + deltaWO[j][i]

			for j in xrange(97):
				for k in xrange(8):
					errorGradH[j] += activation_H[j] * (1 - activation_H[j]) * (errorGradO[k]*OLW[k][j])
				for i in xrange(65):
					deltaWH[j][i] = 0.3 * inode[i] * errorGradH[j]	
					HLW[j][i] = HLW[j][i] + deltaWH[j][i]
		
		else:
			Running = False

def testNet(targetLetter):
	
	global HLW,OLW,inode
	global hiddenL,outL
	
	# **** Hidden Layer ****

	# Get net input of each hidden node
	net_input_H = []
	for j in xrange(len(hiddenL)):
		net_input_H.append(netinput(inode,HLW,j))
	#Get the activation of each hidden node
	activation_H = []	
	for j in xrange(len(hiddenL)):
		aa = activation(net_input_H[j])

		activation_H.append(aa)
		
	# **** Output Layer ****

	# Get net input of each hidden node
	net_input_O = []
	for j in xrange(len(outL)):
		net_input_O.append(netinput(activation_H,OLW,j))
	#Get the activation of each hidden node
	activation_O = []	
	for j in xrange(len(outL)):
		activation_O.append(activation(net_input_O[j]))
		
	#**** Check result ****
	net_output = []
	
	m = max(activation_O)
	for kk in activation_O:
		if kk/m >= 0.8: r = 1
		if kk < 0.8: r = 0
		net_output.append(r)
		
	print "Check results"
	print "Result we want:"
	print targetLetter
	print "Result we have:"
	print net_output
	print activation_O
	
	#print Required_output
		
def saveWeights(weightsH,weightsO):
	target = open("weightsH.txt","w")
	json.dump(weightsH, target)
	target.close()
	target = open("weightsO.txt","w")
	json.dump(weightsO, target)
	target.close()				

# Prime the hidden layer & weights
(hiddenL,HLW) = hiddenlayer()
# Prime the output layer & weights
(outL,OLW) = outputlayer()

L = []
L.append([1,0,0,0,0,0,0,0])#A
L.append([0,1,0,0,0,0,0,0])#B
L.append([0,0,1,0,0,0,0,0])#C
L.append([0,0,0,1,0,0,0,0])#D
L.append([0,0,0,0,1,0,0,0])#E
L.append([0,0,0,0,0,1,0,0])#F
L.append([0,0,0,0,0,0,1,0])#G
L.append([0,0,0,0,0,0,0,1])#H
L.append([1,1,0,0,0,0,0,0])#I
L.append([0,1,1,0,0,0,0,0])#J
L.append([0,0,1,1,0,0,0,0])#K
L.append([0,0,0,1,1,0,0,0])#L
L.append([0,0,0,0,1,1,0,0])#M
L.append([0,0,0,0,0,1,1,0])#N
L.append([0,0,0,0,0,0,1,1])#O
L.append([1,1,1,0,0,0,0,0])#P
L.append([0,1,1,1,0,0,0,0])#Q
L.append([0,0,1,1,1,0,0,0])#R
L.append([0,0,0,1,1,1,0,0])#S
L.append([0,0,0,0,1,1,1,0])#T
L.append([0,0,0,0,0,1,1,1])#U
L.append([1,1,1,1,0,0,0,0])#V
L.append([0,1,1,1,1,0,0,0])#W
L.append([0,0,1,1,1,1,0,0])#X
L.append([0,0,0,1,1,1,1,0])#Y
L.append([0,0,0,0,1,1,1,1])#Z

Li = []
for i in ascii_uppercase:
	Li.append(i)

option = raw_input("Train net (1) or run the net (2)?")
if option == "1":
	for trainCount in xrange(100):
		for i in xrange(len(Li)):
			inputarray = definput(Li[i])
			# Feed in the input
			inode = inputlayer(inputarray)
			trainNet(L[i])

	saveWeights(HLW,OLW)

	# Test the net
	print "************"
	print "Test the net"
	print "************"
	count = 0
	for i in ascii_uppercase:
		inputarray = definput(i)
		inode = inputlayer(inputarray)
		#print inputarray
		testNet(L[count])
		count += 1			
elif option == "2":
	
	HiddenWeightsFile = open("weightsH.txt")
	HLW = json.load(HiddenWeightsFile)
	HiddenWeightsFile.close()
	OutputWeightsFile = open("weightsO.txt")
	OLW = json.load(OutputWeightsFile)
	OutputWeightsFile.close()
	
	# Test the net
	print "************"
	print "Test the net"
	print "************"
	count = 0
	for i in ascii_uppercase:
		inputarray = definput(i)
		inode = inputlayer(inputarray)
		#print inputarray
		testNet(L[count])
		count += 1		
	
else:
	print "You didnt select one of the options"
