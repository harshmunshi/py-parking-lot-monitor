import cv2
import numpy as np

###custom####
VERTITHRESHOLD = 20
HORITHRESHOLD = 30
SURRTHRESHOLD = 350
############

class motionDetector():

	def __init__(self, frameMat, grayMat, xmin, xmax, ymin, ymax):
					
		originMat = self.frameMat
 		workingMat = self.grayMat
		min_x = self.xmin
   		max_x = self.xmax
  		min_y = self.ymin
  		max_y = self.ymax
		self.centerP = [(0,0)]

	def locateMotion(self):
		for j in range(0, workingMat.shape[1], 2):
			for i in range(0, workingMat.shape[0], 2):
				if workingMat[i,j] == 255:
					if checkSurround(j,i):
						if min_x>i:
							min_x = i
						if max_x<i:
							max_x = i
						if min_y>j:
							min_y = j
						if max_y<j:
							max_y = j 
	def checkSurround(self, i, j):
		self.pointCounter = 0
		for m in range(max(0,j-VERTITHRESHOLD), min(workingMat.shape[1],j+VERTITHRESHOLD), 2):
			for n in range(max(0,i-HORITHRESHOLD), min(workingMat.shape[0],i+HORITHRESHOLD), 2):
				if workingMat[i,j] == 255:
					self.pointCounter += 1
		return True if pointCounter >= SURRTHRESHOLD else False
		
	def objectDrawing(self):
		self.xcord = (min_x + max_x) / 2
		self.ycord = (min_y + max_y) / 2
		self.centerP[0] = (self.xcord, self.ycord)
		if (self.centerP[0][0] != workingMat.shape[0]/2 and self.centerP[0][1] != workingMat.shape[1] /2):
			cv2.circle(originMat,centerP[0], 1, (0,255,0), 5)
			cv2.rectangle(originMat,(min_x, min_y),(max_x, max_y),(0,255,0),5)

	def checkOccupied(self, vertex):
		if(((centerP[0][0] - vertex[2][0]) * (vertex[3][1] - vertex[2][1]) + (vertex[3][0] - vertex[2][0]) * vertex[2][1] \
           >= centerP[0][1] * (vertex[3][0] - vertex[2][0])) and \
         ((centerP[0][0] - vertex[0][0]) * (vertex[1][1] - vertex[0][1]) + (vertex[1][0] - vertex[0][0]) * vertex[0][1] \
           <= centerP[0][1] * (vertex[1][0] - vertex[0][0])) and \
         ((centerP[0][0] - vertex[2][0]) * (vertex[0][1] - vertex[2][1]) + (vertex[0][0] - vertex[2][0]) * vertex[2][1] \
           <= centerP[0][1] * (vertex[0][0] - vertex[2][0])) and \
         ((centerP[0][0] - vertex[3][0]) * (vertex[1][1] - vertex[3][1]) + (vertex[1][0] - vertex[3][0]) * vertex[3][1] \
           >= centerP[0][1] * (vertex[1][0] - vertex[3][0])) and \
         (centerP[0][0] != workingMat.shape[0]/2 and centerP[0][1] != workingMat.shape[1]/2)):
			return True
		else:
			return False
