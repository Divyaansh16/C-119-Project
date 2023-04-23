import time
import cv2
import math
p1=525
p2=300
xb=[]
yb=[]
video = cv2.VideoCapture("footvolleyball.mp4")
tracker=cv2.TrackerCSRT_create()
print(tracker)
returned,image=video.read()
bbox=cv2.selectROI('Tracking',image,False)
print(bbox)
tracker.init(image,bbox)
def drawbox(image,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(image,(x,y),((x+w),(y+h)),(0,0,255),2,1)
    cv2.putText(image,"Tracking",(75,90),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,0,0),1)
def goal_tracker(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(img,(c1,c2),2,(0,0,225),5)
    cv2.circle(img,(int(p1),int(p2)),2,(0,225,0),5)
    distance=math.sqrt(((p1-c1)**2)+(p2-c2)**2)
    print(("The distance is:",distance))
    xb.append(c1)
    yb.append(c2)
    #for i in range(len(xb)):
    #    cv2.circle(img,(xb[i],yb[i]),2,(255,0,0),2)
    if distance<=50:
        cv2.putText(img,"GOAL REACHED",(300,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(254,255,135),2)
    else:
        for i in range(len(xb)):
            cv2.circle(img,(xb[i],yb[i]),2,(255,0,0),2)
while True:
    check,img = video.read()
    success,bbox=tracker.update(img)
    print("What is success:",success)  
    goal_tracker(img,bbox)
    if success==True:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,0,0),1)
    cv2.imshow("result",img)
    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped!")
        break
video.release()
cv2.destroyALLwindows()