import cv2

cap = cv2.VideoCapture("video.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Yahan tum apna hologram effect/code laga sakte ho

    out.write(frame)

cap.release()
out.release()

print("Video export ho gaya: output.mp4")