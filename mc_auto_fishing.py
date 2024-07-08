# Ray Min
# 07/07/2024
# This program is a program that automates fishing in minecraft
# When fishing, if the fish is on the bobber, it makes a loud sound. The program has a volume threshold,
# if that threshold is exceeded, it will reel the fish in and restart the process.

import sounddevice as sd
import numpy as np
import pyautogui
import time
import keyboard
import os

# Parameters
volume_threshold = 2.5  # Adjust this value based on your sound sensitivity
chunk_size = 1024  # Size of the audio chunks to process

def detect_sound(indata, frames, time, status):
    if status:
        print(status)
    volume_norm = np.linalg.norm(indata)  # Calculate the volume of the current chunk
    if volume_norm > volume_threshold:
        pyautogui.rightClick() # Right clicks when sound threshold is met
        print("Fish Detected")
        print("Reeling back in...")
        main() # Loops back to main to reset process

def main():
    time.sleep(1)
    os.system("cls")
    pyautogui.rightClick() # reels into water
    time.sleep(1)

    # List all available devices and find the virtual cable input device
    devices = sd.query_devices()
    virtual_cable_index = None
    for i, device in enumerate(devices):
        if 'CABLE' in device['name']:
            virtual_cable_index = i
            break

    if virtual_cable_index is None:
        raise Exception("Virtual audio cable not found. Please ensure it is installed and set up correctly.")

    with sd.InputStream(callback=detect_sound, channels=2, device=virtual_cable_index, blocksize=chunk_size):
        print("Listening for sound threshold to be met")
        sd.sleep(9999999)  # Keep the program running

if __name__ == "__main__":
        os.system("cls")
        print("Press F4 to start the program. Make sure you are in MC before starting")
        keyboard.on_press_key('F4', lambda _: main())
        keyboard.wait()