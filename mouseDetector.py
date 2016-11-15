import cv2

total_points = 4


class mouseDetector():
	def __init__(self):
		self.n = total_points
		self.capturePoint = []
		self.workingMat

	def onMouse(self,event,x,y,flags,param):
		if self.event == CV_EVENT_LBUTTONDOWN:
			print "point" + x + y 
			self.capturePoint.append(x,y)
		self.n -= 1
		if self.n==0:
			cv2.destroyAllWindows()

	def setMat(self,inputMat):
		self.workingMat = self.inputMat

	def getPoint(self, point):
		return self.capturePoint
