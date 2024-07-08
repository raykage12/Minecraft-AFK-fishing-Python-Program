# Minecraft-AFK-fishing-Python-Program
a python program that automates fishing using sounddevice and VB-Audio-Virtual Cable. Not sure how efficient the program is or if there are simpler ways to create this, but it does the job.

video demonstration:
https://www.youtube.com/watch?v=wwxgR8Wa86A&ab_channel=RayMin

Program detects audio, so when something catches onto the bobber, it makes a loud sound and the program detects it, reels it in, and throws reel back out and the process starts again. Other sounds can throw off the program so make sure nothing nearby is making loud noises. eg. mobs, other players...


there are a couple steps that need to be completed before this program can function. 

1 - Download Python and set Path
python website:
https://www.python.org/

video tutorial: 
https://www.youtube.com/watch?v=yivyNCtVVDk&ab_channel=GeekyScript

path tutorial:
https://www.youtube.com/watch?v=lezhrFdVSVY&ab_channel=ExampleProgram

Once Python is installed and Path has been set, go to next step to download libraries

2 - Libraries
the libraries that need to be installed will be listed below.
sounddevice - pip install sounddevice
pyautogui - pip install pyautogui
nunmpy - pip install numpy
keyboard - pip install keyboard

to install these libraries, go to command prompt and type the pip installs provided. I think pip comes with python. 
if not, there are video tutorials online to get pip

3 - VB-Audio-Cable
website - 
https://vb-audio.com/Cable/

video tutorial - 
https://www.youtube.com/watch?v=4sGWzOyF82M&t=241s&ab_channel=TheFrugalStreamer

just the first 3-4 minutes of the video tutorial are needed. You will need to select this VB-Cable as your speaker in order for program to work.

4 - Start program

- Use whatever text editor you want and run the program. a print statement should say "Press F4 to start program."
- Go to the game, have rod out, and press F4 to start
- to stop, go back into editor and end program

Note: volume threshold may have to be adjusted. 2.5 is what works best for me but Ive only ever tried this on my computer. Adjust if needed.

lower = higher sensitivity

higher = lower sensitivity

to adjust, find volume_threshold variable on line 15 and change value
