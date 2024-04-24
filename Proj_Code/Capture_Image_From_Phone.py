import cv2

def capture_image():
    # Replace 'http://your_ip_address:4747/video' with your Droidcam IP address
    cap = cv2.VideoCapture('http://192.168.1.3:4747/video')
    
    if not cap.isOpened():
        print("Error: Could not open Droidcam")
        return
    
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame")
        return
    
    cv2.imwrite('droidcam_image.jpg', frame)
    print("Image captured and saved as 'droidcam_image.jpg'")
    
    cap.release()

if __name__ == "__main__":
    capture_image()
