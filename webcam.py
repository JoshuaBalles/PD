import cv2


def open_webcam():
    # Initialize the video capture object with 720p resolution (1280x720)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    # Create a window with fixed dimensions and prevent resizing
    cv2.namedWindow("Webcam", cv2.WINDOW_AUTOSIZE)

    # Disable the maximize button
    cv2.setWindowProperty("Webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        # Read a new frame
        ret, frame = cap.read()

        # Check if frame is read correctly
        if not ret:
            break

        # Display the frame
        cv2.imshow("Webcam", frame)

        # Wait for a key press or close button event
        key = cv2.waitKey(1)

        if key == 27 or cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE) < 1:
            break

    # Release the video capture and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    open_webcam()
