import time
from collections import namedtuple

import cv2
import numpy as np

Point = namedtuple("Point", ["x", "y"])


def loop(cap: cv2.VideoCapture):
    # capture an image
    fetch_success, img = cap.read()

    if not fetch_success:
        print("fetch failed")
        return

    # load the image
    img = np.array(img)  # BGR format

    # ? extract circular region
    # ! use dummy region; central 24x24
    h, w, _ = img.shape
    roi_w, roi_h = 16, 16
    top_left = Point((w - roi_w) // 2, (h - roi_h) // 2)
    bottom_right = Point((w + roi_w) // 2, (h + roi_h) // 2)
    roi = img[top_left.y : bottom_right.y, top_left.x : bottom_right.x, :]

    # convert BGR to HSV
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV_FULL)

    # determine the color
    hue, saturation, value = hsv.reshape(-1, 3).mean(axis=0)

    # show detected color
    if 0 <= hue <= 50 and saturation >= 50 and value >= 50:
        color = "red"
    elif 140 <= hue <= 160 and saturation >= 50 and value >= 50:
        color = "blue"
    else:
        color = ""  # idk

    start = time.perf_counter_ns()
    cv2.putText(
        img,
        f"({int(hue)}, {int(saturation)}, {int(value)})",
        (2, 8),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.25,
        (0, 255, 0),
        1,
        cv2.LINE_AA,
    )
    cv2.putText(
        img,
        color,
        (top_left.x, top_left.y - 2),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.25,
        (0, 255, 0),
        1,
        cv2.LINE_AA,
    )
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0))
    retval = cv2.imwrite(f"./videos/{time.time()}.jpg", img)
    print(retval, time.perf_counter_ns() - start)


if __name__ == "__main__":
    # open video capture()
    cap = cv2.VideoCapture(
        filename="/dev/video0",
        apiPreference=cv2.CAP_V4L2,
    )
    if not cap.isOpened():
        print("Unable to connect to the camera")
        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 32)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 32)
    cap.set(cv2.CAP_PROP_FPS, 30)

    try:
        while True:
            time.sleep(0.02)
            loop(cap)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        retval = cap.release()
        print(retval)
        print("done!")
