import cv2
import frameHandler as handler
import sys

arg = sys.argv[1]

def monitorLauncher(argm):
	capture = cv2.VideoCapture(argm)
	if not capture.isOpened():
		print "Cannot open the video file"
		exit(0)
	
def run():
	handler.getBackground(capture)
	handler.detectMouse(capture)
	handler.handlerRun(capture)

if __name__ == "__main__":
	Launcher = monitorLauncher(arg)
	Launcher.run()
