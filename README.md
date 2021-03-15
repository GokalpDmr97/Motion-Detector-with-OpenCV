# Motion Detector with OpenCV
 
 Used Libraries: 
* time 
* Pandas 
* cv2 (OpenCV)
* datetime
* Bokeh

I've built a program that detects moving objects in a video and then it records the time that the object enters the video frame and the time object exited the video frame. Detected object is surrended by a rectangle. 

![detection](https://user-images.githubusercontent.com/78566362/111184499-15279f80-85c2-11eb-861a-8297bac653fb.jpg)

When the video ended, an interactive graph which shows the times where the object entered the frame and exited the frame is created. 

![motiongraph](https://user-images.githubusercontent.com/78566362/111184504-1658cc80-85c2-11eb-859b-c7920d5f5d9d.jpg)

This Python program can be put in a Raspberry Pi server, for instance, to detect animals. You may want to know when the animal is entering the frame and when it is exiting.  
