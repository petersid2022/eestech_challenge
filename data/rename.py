#!/usr/bin/env python3

import os
import numpy as np
from pandas import read_csv

if __name__ == "__main__":
    folder_path = "./IMG"

    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]

    image_files.sort()

    for i, filename in enumerate(image_files):
        new_filename = str(i) + ".jpg"
        os.rename(
            os.path.join(folder_path, filename), os.path.join(folder_path, new_filename)
        )

    columns = ["Center", "Left", "Right", "Steering", "Throttle", "Brake", "Speed"]
    data = read_csv("driving_log.csv", names=columns)

    arr = data["Steering"].to_numpy()

    np.save("./data.npy", arr)
