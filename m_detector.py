import cv2, time, pandas
from datetime import datetime 
video = cv2.VideoCapture('sample.mp4')

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"])
if(video.isOpened() == False):
    print("Error. Please check opening video stream or file again.")

while (video.isOpened()): 
    ret, frame = video.read()
    
    if ret == True: 
        status = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blurred = cv2.GaussianBlur(gray, (21,21),0)
        if first_frame is None:
            first_frame = gray_blurred
            continue 
        
        delta_frame = cv2.absdiff(first_frame, gray_blurred)
        threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        threshold_frame = cv2.dilate(threshold_frame, None, iterations = 2)
        
        (contour, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnts in contour:
            if cv2.contourArea(cnts) < 2700: 
                continue
            status = 1
            (x, y, w, h) = cv2.boundingRect(cnts)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        status_list.append(status)    
        
        status_list = status_list[-2:]
        
        
        
        if status_list[-1] == 1 and status_list[-2] == 0: 
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1: 
            times.append(datetime.now())
        
        #cv2.imshow("Gray Frame", gray)
        #cv2.imshow("Delta Frame", delta_frame)
        #cv2.imshow("Threshold Frame", threshold_frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
        
        
    else:
        break
    
if status_list[-1] == 1 and status_list[-2] == 1:
    times.append(datetime.now())


end = None

if len(times) % 2 != 0:
    end = len(times) - 1
else:
    end = len(times)

for i in range(0, end, 2):
    df = df.append({"Start": times[i], "End": times[(i+1)]}, ignore_index = True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()