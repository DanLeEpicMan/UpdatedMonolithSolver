# Foreword
Hello! I'd just like to immediately state that not everything in this tool is mine. This borrows code from two separate repos. [Here](https://github.com/Azshene/THM_Solver) is the repo for the solver itself (Azshene/THM_Solver), and [here](https://github.com/artur-ag/TreasureHuntParser) is the repo for the image parser (artur-ag/TreasureHuntParser). My code is any tweaks I made, along with the "start.py" script.

I'm uploading this for a few reasons. My initial motivation was the original solver had a few errors, and I fixed them and uploaded it here as a revised edition (hence the name UpdatedMonolithSolver). I later came back to this 2 years later after finding an auto-parser and updated everything to accomodate for it, in order to make this tool easier to use.

# Instructions

To clarify, these instructions assume that you are using a computer with Windows. If this is not your case, then you should still be able to run all the scripts fine, but none of the instructions will apply. Contact me if you're having trouble (see below). Also, if you prefer instructions in a video format then [you can find that here](https://youtu.be/2Rf2MQzMCJ8). I apologize in advance if I come off as pretentious, condescending, or redundant.

Also know that you are free to contact me for whatever reason, whether you run into a problem with the program, want some tips for 100% completion, or simply want to talk. My contact information can be found in the [Afterword](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#afterword).

## Prerequisites and Installation

Here I explain what you will need in order to run this script. Steps 1 and 2 are also related to setting up the solver; if you already know how to (decently) use command prompt and file explorer, then feel free to download the package in the next step and skip to [Step 3](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#step-3).

Since this program is written in Python, you will need to download Python 3.6 or a newer version. Additionally, you must also have the NumPy library installed. The Anaconda distribution includes both of these: [here's the download link for Windows](https://www.anaconda.com/products/individual#windows). If none of this step made sense to you, don't worry! Just download the Anaconda software and move onto Step 1. Moreover, don't forget to download this solver and unzip it to an easily accessible place, such as Downloads folder (which is where I put it!). You should also omit the "UpdatedMonolithSolver-main" bit from the extraction destination, as doing so won't create extraneous folders.

If you plan on using the automatic screnshot parser (which I highly recommend), you will need to install an additional package, OpenCV. I will explain how to do so in the next step.

## Step 1

First, download this solver by clicking the "Code" and "Download as Zip" option. Unzip it to an easily accessible place, such as Downloads folder (which is where I put it!). You should also omit the "UpdatedMonolithSolver-main" bit from the extraction destination, as doing so won't create extraneous folders.

Next, on the search bar in the bottom left corner of your screen, type the word "Anaconda" (if you're using Windows 11, click the magnifying glass for the search bar to appear). Open the program named "Anaconda Prompt" (or something very similar to that). If you don't have the search bar enabled, you can access it by clicking the Windows icon in the bottom left corner. If you didn't download Anaconda then open command prompt (or PowerShell) instead. I may also use "Anaconda prompt" and "Command prompt" interchangeably, so be aware of that in case there's any confusion.

If you plan on using the automatic screenshot parser (you really should), then run this command in Anaconda prompt.
```
pip install opencv-python
```

A neat little graphic that looks like a progress bar should appear and tell you that it downloaded successfully. If you do not receive this message, please contact me and I'll help you out. See [Afterword](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#afterword) for my contact info.

## Step 2

For those of you that have experience with command prompt, simply move into the unzipped folder using the cd command and move onto the next step. For those of you that don't, here's how to do that

### 2.1

In File Explorer, go into the Monolith folder (the default title is "UpdatedMonolithSolver-main") and copy the directory link. For example, my directory looked like this 
```
C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main
```
### 2.2

Then in Anaconda prompt, type (without quotes) "cd (whatever you just copied)". For example, I would input this into my command prompt
```
cd C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main
```
### Additional Notes

1: If you left the zip extraction destination unchanged from the installation step, then you'll have two folders called "UpdatedMonolithSolver-main". To check if you have two, open the unzipped folder and see if there's a single folder in there called "UpdatedMonolithSolver-main". You can either type "cd UpdatedMonolithSolver-main" or move the inner folder into Downloads (or wherever you'd like to keep it) and delete the empty folder.

2: If you place the Monolith folder in a drive other than the C drive, then you must move to that drive first before the cd command will work properly. To do this, simply type "(drive letter):" in command prompt (e.g. if you put the Monolith folder in your D: drive, type "D:" in the command prompt and it will move you there). If you ever need to verify whether you're in the right spot, type "dir" and see if command prompt displays the folder's contents (namely "boards", "THM.py", "sprites", etc.)
	
## Step 3

This step is where you actually start to use the solver. I highly recommend playing in Borderless Windowed mode since you will be pressing Alt+Tab a lot. I also recommend muting the game in Volume Mixer and playing your own music, as this minigame's music will most likely drive you insane.

The following instructions assume that you are using the automatic script parser (i.e. you aren't manually making the board) and have downloaded the additional package in [Step 1](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#step-1). I'll include additional notes at the end explaining how to manually make the board yourself; feel free to skip those if the parser worked well with you.

Also, you may find it easier to run the script midday into a game instead of using it at the start. The benefit of this is allowing you to incorporate some degree of personal strategy, as opposed to getting lucky. This was not my idea but instead someone else's ("HyungOppaHelper" from the comments of the YouTube instructions). Regardless, the difference between this approach and the following is when you decide to pause the game and make the board. Whichever one you prefer is up to your discretion.

### 3.1

Start a game and take a picture of the board by pressing Prt Sc (Print Screen, usually located near the numpad above the arrow keys). This will save a screenshot to your clipboard; make sure you don't copy anything else until the next step. If you have multiple monitors, then press Alt + Prt Sc instead (this will only screenshot the active monitor instead of all of them). **Make sure your hammer is away from the board and that you include the full screen** (see reference image). Then, pause the minigame by opening the controls **(F3 on QWERTY layout)**. If you don't have a Prt Sc key, press Windows Key + Shift + S instead.

This is what your screenshot should look like.
![Sample board](https://cdn.discordapp.com/attachments/906695285990899712/990763499137425438/unknown.png)
Notice how the hammer is out of frame in the bottom left corner

### 3.2

Open up Microsoft Paint by searching "paint" in the search bar at the bottom left corner (for Windows 11 Users, you have to press the magnifying glass for this to appear). If you have a different photo editing software, you can use this as well.
  
### 3.3

Save the screenshot to the "screenshots" folder included in the main Monolith folder. Click "File" then "Save As", and navigate to the screenshots folder and save it there. Make sure to name it something you can easily remember (board, myBoard, game, ...). **Check the File Type and make sure this is saved as either a PNG or JPG, as the parser will only accept those two image formats.**
	
### 3.4

Once that is all saved, go back to Anaconda prompt and type the following command
```
python start.py boardName
```
Replace boardName with whatever you named your board. I used the name "myBoard", so I would input the following
```
python start.py myBoard
```
You don't need to include the file extension if your screenshot is a PNG. If it's a JPG, include .jpg at the end.

## Notes on Manually Making the Board

**Skip this note and move to [Step 4](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#step-4) if the parser worked fine for you.** 

Sometimes the parser might not work and just generate an incorrect board. This shouldn't happen very often, but is nonetheless possible. If this is your case, then go to the 'boards' folder and edit the file called 'out.csv' (it might just be called 'out'). Refer to the following images for correctly making a board:

This is the board I have

![The board I'd like to recreate](https://cdn.discordapp.com/attachments/786485904176971827/788300313815285770/unknown.png)
  
And this is how I would recreate it

![The recreation in Notepad](https://cdn.discordapp.com/attachments/786485904176971827/788300784487628800/unknown.png)

Feel free to shoot me a message if you're having trouble.

## Step 4

If you correctly inputted that command then the program should run for a minute or two. Once it's done it should open a File Explorer with a lot of images titled "step" and some number. Follow those steps in order, starting from Step 0. There is a small yellow box around the blob you should click. For reference, the board in the above note has this yellow box at (x, y) coordinate (9, 9).

### Additional Notes

1: Ideally, you want at least 90% board clearance, since it'll most likely require minimal manual clearing. If you get below 80%, I reccommend starting over since you will have to do a lot of manual clearing. Unfortunately there's no restart option, so you will have to spam click the board until you can start a new game.

2: Very rarely, the program may generate an incomplete solution. This is because the program is designed using the A* (A-Star) search algorithm, which stops running on its own after some time. By default, the program terminates once it has checked 5000 board states. If you ever run into this problem, input the following command into Anaconda prompt
```
python THM.py out 100 7500
```
That command will let the program check 7500 boards instead of 5000, increasing the likelihood of finding a more complete solution. It might take a few seconds longer though.

### An Extra and (Hopefully) Helpful Tip 

**Note that this program does NOT account for your treasure!** It simply gives you the solution with the most blocks destroyed. Recall that you should have at least 2 Monokubs and 3-4 fish to earn the achievement, so if you happen to uncover treasure that you would like to be accounted for, I recommend manually clearing it (you can plan out your moves by taking a screenshot of the board and paste it into paint or some other image editting software). Once that has been done, you can take another screenshot of the board and go back to [Step 3](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#step-3).

Make sure to double check the board it gives you, since it might be a bit off. If you notice that the boards the program generates are off, then head to boards/out.csv and edit the file. You should see a bunch of numbers separated by commas; recreate the board manually as explained in [this note](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#notes-on-manually-making-the-board).

## Restarting

If you have to restart after clearing the entire board, then go to [Step 3](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#step-3). If you have to open Anaconda prompt again, then start at [Step 1](https://github.com/DanLeEpicMan/UpdatedMonolithSolver/blob/main/README.md#step-1) instead. Don't reinstall the OpenCV package if you've already installed it though (i.e. skip the command I tell you to input in Step 1 if you've done that before).

# Afterword

I hope my explanation was as informative as it could be! The two repositories I borrowed from had their own instructions, but I felt like I should write my own to help streamline everything. Remember that this tool won't guarantee success immediately, and you will most likely have to retry this a few times.

If you run into any issues (or just wanna have a chat), then please feel free to shoot me a message. **My Discord is _Dan Le Man 2#1890_. Alternatively, you can add my [Steam account](https://steamcommunity.com/id/danleepicman/) if you prefer to use that instead** (in case the link doesn't work, my friend code is 442227082). I don't really have other contact info, so hopefully those two work with you!

Full credit to both authors I borrowed code from! Feel free to also modify and redistribute this as you wish. Released under MIT License.
