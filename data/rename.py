#!/usr/bin/env python3

import os
import numpy as np
from pandas import read_csv

if __name__ == "__main__":
    path = "./IMG"

    for root, _, files in os.walk(path):
        for i, filename in enumerate(files, start=1):
            current_file = os.path.join(root, filename)
            new_file = os.path.join(root, str(i)) + ".jpg"

            os.rename(current_file, new_file)

    columns = ["Center", "Left", "Right", "Steering", "Throttle", "Brake", "Speed"]
    data = read_csv("driving_log.csv", names=columns)

    arr = data["Steering"].to_numpy()

    np.save("./data.npy", arr)
