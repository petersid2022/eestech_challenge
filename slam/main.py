#!/usr/bin/env python3

import cv2 as cv
import glob
import matplotlib.pyplot as plt
import numpy as np

"""
def extract_frames(cap):
    imgs = glob.glob("./imgs/*")

    for img in imgs:
        os.remove(img)

    i = 0
    while True:
        # Read a frame
        ret, frame = cap.read()
        if not ret:
            break

        # resize video
        original_w = int(cap.get(3))
        original_h = int(cap.get(4))

        frame = cv.resize(frame, (original_w // 2, original_h // 2))

        # grayscale the image
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        file_location = f"./imgs/{i}.png"
        cv.imwrite(file_location, frame)

        i += 1

    return i
"""


def process_frames():
    # frames_path = [f"./imgs/{i}.png" for i in range(0, framenr, 2)]
    frames_path = glob.glob(
        "/home/petrside/github/eestech_challenge/eestech_challenge/data/IMG/*.jpg"
    )

    for i in range(0, len(frames_path) - 1, 2):
        img1 = cv.imread(frames_path[i], cv.IMREAD_COLOR)
        img2 = cv.imread(frames_path[i + 1], cv.IMREAD_COLOR)

        # Initiate SIFT detector
        sift = cv.SIFT_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)

        # FLANN parameters
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary

        flann = cv.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des1, des2, k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0, 0] for i in range(len(matches))]

        # ratio test as per Lowe's paper
        for i, (m, n) in enumerate(matches):
            if m.distance < 0.7 * n.distance:
                matchesMask[i] = [1, 0]

        draw_params = dict(
            matchColor=(0, 255, 0),
            singlePointColor=(255, 0, 0),
            matchesMask=matchesMask,
            flags=cv.DrawMatchesFlags_DEFAULT,
        )

        out = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)

        cv.imshow("out", out)

        # plt.imshow(out)
        # plt.show()

        keyboard = cv.waitKey(30)
        if keyboard == 113:
            return


"""
def get_depth_info():
    frames_path = glob.glob(
        "/home/petrside/github/eestech_challenge/self-driving-car-sim/IMG/*.jpg"
    )

    for i in range(0, len(frames_path) - 1, 2):
        img1 = cv.imread(frames_path[i], cv.IMREAD_GRAYSCALE)
        img2 = cv.imread(frames_path[i + 1], cv.IMREAD_GRAYSCALE)

        stereo = cv.StereoBM.create(numDisparities=16, blockSize=15)
        disparity = stereo.compute(img1, img2)
        plt.imshow(disparity, "gray")
        plt.show()
"""


if __name__ == "__main__":
    # cap = cv.VideoCapture("./videos/test_drone.mp4")

    # if not cap.isOpened():
    #     exit(0)

    # framenr = extract_frames(cap)
    process_frames()

    cv.destroyAllWindows()
