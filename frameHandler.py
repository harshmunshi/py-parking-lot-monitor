import cv2
import time
import motionDetector
import mouseDetector
from datetime import datetime


class frameHandler:
	def __init__(self, inputCapture):
		self.capture = inputCapture
  		self.FrameMat = None
  		self.curGrayMat = None
  		self.bkGrayMat = None
  		self.frGrayMat = None
  		self.parkingPoint = []

  	def getBackground(self):
  		self.FrameMat = self.capture.read()
  		self.bkGrayMat = cv2.cvtColor(self.FrameMat, cv2.COLOR_BGR2GRAY)


  	def getForeground(self):
  		self.curGrayMat = cv2.cvtColor(FrameMat, cv2.COLOR_BGR2GRAY)
  		self.frGrayMat = cv2.absdiff(self.curGrayMat, self.bkGrayMat)
  		self.frGrayMat = cv2.threshold(self.frGrayMat, cv2.CV_THRESH_BINARY)


  	def detectMouse(self):
  		print "Please select the parking space with 4 clicks..."
  		mouseDetector.setMat(self.FrameMat)
  		cv2.namedWindow("parkingSpaceSelection", cv2.CV_WINDOW_AUTOSIZE);
  		cv2.setMouseCallback("parkingSpaceSelection", mouseDetector.onMouse, 0);
  		cv2.imshow("parkingSpaceSelection", mouseDetector.workingMat);
  		cv2.waitKey(0);

  	def handlerRun(self):
  		statusFlag = False
  		now = datetime.now()
  		unoccupiedStart = datetime.now()
		# clock_t unoccupiedStart = clock();
  		# clock_t occupiedStart;

  		parkingPoint = mouseDetector.getPoint()
  		#Here we temporarily use fixed parking space
  		pt1 = (325, 368)
  		pt2 = (680, 115)
  		pt3 = (532, 460)
  		pt4 = (876, 183)

  		while(self.capture.read(FrameMat)):
  			# get the foreground (the motion objects)
  			self.getForeground()
  			detector = motionDetector.motionDetector(self.FrameMat, self.frGrayMat, self.frGrayMat.cols, 0, self.frGrayMat.rows, 0)
  			detector.locateMotion()
  			detector.objectDrawing()

  			if (detector.checkOccupied(parkingPoint.at(0), parkingPoint.at(1), parkingPoint.at(2), parkingPoint.at(3))):
  				if statusFlag == False:
  					#this is the parking into transition
  					statusFlag = True
  					occupiedStart = datetime.now()
  					vacDuration = datetime.now() - unoccupiedStart
  					now = datetime.now()
  					dt = datetime.now()
	  			
				else:
					#this is the leaving transition
					if statusFlag == True:
						statusFlag = False
						unoccupiedStart = datetime.now()
						# double occDuration = (clock() - occupiedStart) / (double) CLOCKS_PER_SEC
						occDuration = datetime.now() - occupiedStart
						now = datetime.now()
						dt = datetime.now()
						print " to ", dt , " Duration ", occDuration, "s"
						print "Vacant time from ", dt

			#highlight the parking lot area
			cv2.line(self.FrameMat, parkingPoint.at(0), parkingPoint.at(1), (255,0,0), 5)
			cv2.line(self.FrameMat, parkingPoint.at(0), parkingPoint.at(2), (255,0,0), 5)
			cv2.line(self.FrameMat, parkingPoint.at(2), parkingPoint.at(3), (255,0,0), 5)
			cv2.line(self.FrameMat, parkingPoint.at(1), parkingPoint.at(3), (255,0,0), 5)

			#show the frame
			cv2.imshow("Vedio", self.FrameMat)

			#wait for 'esc' key press for 30 ms. If 'esc' key is pressed, break loop
			if cv2.waitKey(30) == 27:
				print "esc key is pressed by user"
				break

		# vacDuration = (clock() - unoccupiedStart) / (double) CLOCKS_PER_SEC
		vacDuration = datetime.now() - unoccupiedStart
		now = datetime.now()
		dt = datetime.now()
		print " to ", dt, "Duration: ", vacDuration, "s"

