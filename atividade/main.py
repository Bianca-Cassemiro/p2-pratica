import cv2

face_cascade = cv2.CascadeClassifier(
    filename=f"../assets/haarcascade_frontalface_alt.xml"
)
input_video = cv2.VideoCapture('../assets/arsene.mp4')

width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))


output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))


while True:
 
    ret, frame = input_video.read()

  
    if not ret:
        break
    
    gray_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
    image= gray_frame, 
    scaleFactor=1.1, 
    minNeighbors=10 
)

    x, y, w, h = faces[0]

    cv2.rectangle(
    img=frame,
    pt1=(x, y),
    pt2=(x+w, y+h),
    color=(0,0,255),
    thickness=2
)
   
    cv2.imshow('Video Playback', frame)
    
    output_video.write(frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
output_video.release()
input_video.release()
cv2.destroyAllWindows()