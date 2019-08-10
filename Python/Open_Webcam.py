import cv2


video = cv2.VideoCapture(0)

	
while(True):
	ret, frame = video.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("Frame", frame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

video.release()

# Close all windows
cv2.destroyAllWindows()