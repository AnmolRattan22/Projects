import cv2 as cv


camera = cv.VideoCapture(0) # Initialize video capture (0 for internal camera, 1 for external)


tracker = cv.legacy.TrackerMOSSE_create() # Create the tracker using the legacy namespace


success, frame = camera.read() # Read the first frame from the camera
if not success:
    print("Failed to read from camera. Exiting...")
    exit()


box = cv.selectROI('Tracking', frame, False) # Select ROI for tracking
cv.destroyWindow('Tracking')  # Close the ROI selection window


tracker.init(frame, box) # Initialize the tracker with the first frame and the selected bounding box

def drawbox(img, box):  # Function to draw the bounding box
    (x, y, w, h) = [int(v) for v in box]
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv.putText(img, "Tracking", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

while True:
    timer = cv.getTickCount()

    success, img = camera.read()  # Read a new frame from the camera
    if not success:
        print("Failed to read from camera. Exiting...")
        break

    success, box = tracker.update(img)  # Update the tracker

    if success:
        drawbox(img, box)  # If tracking is successful, draw the bounding box
    else:
        cv.putText(img, "Lost the object", (75, 75), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)  # Display tracking failure message

    fps = cv.getTickFrequency() / (cv.getTickCount() - timer)
    cv.putText(img, f"FPS:{int(fps)}", (75, 50), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)  # Calculate and display FPS

    cv.imshow("Tracking", img)  # Show the image with the bounding box or error message

    if cv.waitKey(1) & 0xFF == ord('q'):  # Exit on pressing 'q'
        break

camera.release()
cv.destroyAllWindows()
