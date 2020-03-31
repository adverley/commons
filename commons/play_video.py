import cv2


def bgr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def play_video(path, on_frame_func=None, start_from_frame=0, fps=10):
    playing_speed = int((1.0 / fps) * 1000)
    cap = cv2.VideoCapture(path)

    # Check if camera opened successfully
    if cap.isOpened() == False:
        print(f"Error opening video stream or file with path '{path}'")

    frame_nr = 0
    # Read until video is completed
    while cap.isOpened():
        ret, frame = cap.read()

        if frame_nr < start_from_frame:
            frame_nr += 1
            continue

        if on_frame_func is not None:
            frame = on_frame_func(frame_nr, frame)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        # if cv2.waitKey(playing_speed) & 0xFF == ord('q'):
        #     break

        if cv2.waitKey() & 0xFF == ord('q'):
            pass

        frame_nr += 1

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
