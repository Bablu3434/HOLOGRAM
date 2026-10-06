import cv2
import numpy as np

# Video file ka naam
video_path = "video.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video open nahi ho raha. Check karo ki video.mp4 same folder me hai.")
    exit()

canvas_size = 800
object_size = 250

while True:
    ret, frame = cap.read()

    # Video end ho jaaye to dobara start karo
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Resize
    frame = cv2.resize(frame, (object_size, object_size))

    # Black background
    canvas = np.zeros((canvas_size, canvas_size, 3), dtype=np.uint8)

    center = canvas_size // 2

    # TOP
    top = cv2.rotate(frame, cv2.ROTATE_180)
    canvas[
        center - object_size:center,
        center - object_size // 2:center + object_size // 2
    ] = top

    # BOTTOM
    bottom = frame.copy()
    canvas[
        center:center + object_size,
        center - object_size // 2:center + object_size // 2
    ] = bottom

    # LEFT
    left = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    canvas[
        center - object_size // 2:center + object_size // 2,
        center - object_size:center
    ] = left

    # RIGHT
    right = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    canvas[
        center - object_size // 2:center + object_size // 2,
        center:center + object_size
    ] = right

    cv2.imshow("3D Hologram Effect", canvas)

    # Q press karne se close
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()