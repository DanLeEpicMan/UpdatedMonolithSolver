# Foreword
Hello! I'd just like to immediately state that not everything in this tool is mine. This borrows code from two separate repos. [Here](https://github.com/Azshene/THM_Solver) is the repo for the solver itself (Azshene/THM_Solver), and [here](https://github.com/artur-ag/TreasureHuntParser) is the repo for the image parser (artur-ag/TreasureHuntParser). My code is any tweaks I made, along with the "start.py" script.

I'm uploading this for a few reasons. My initial motivation was the original solver had a few errors, and I fixed them and uploaded it here as a revised edition (hence the name UpdatedMonolithSolver). I then came back to this 2 years later after finding an automatic image converter (auto-parser) and updated everything to accomodate for it, in order to make this tool easier to use (by a few orders of magnitude).

# Instructions

To clarify, these instructions assume that you are using a computer with Windows. Contact me if you're having trouble (see below). 
- Mac: I'm unsure if these instructions apply for Mac. You should know how to open terminal and use it though. If Step 3 fails for you, then use the above two instructions.
- Linux: If you're using Linux, then you know what you're doing. My script won't run on Linux. Use the instructions for the above two repositories instead.

[Here is a video of me going over the instructions](https://youtu.be/63QQr9axij0). These instructions are newer, but should be mostly the same (except maybe Prerequisites and Installation).

Also know that you are free to contact me for whatever reason, whether you run into a problem with the program, want some tips for 100% completion, or simply want to talk. My contact information can be found in the [Afterword](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#afterword).

## Prerequisites and Installation

In order to run this script, you must have
- Python 3.6 (or newer)
- NumPy
- OpenCV

If you have no clue what any of those mean, then:
- You can download the Anaconda distribution of Python. [Here's the download link for Windows](https://www.anaconda.com/products/individual#windows). This comes with NumPy preinstalled.
- If you're not comfortable giving Anaconda your email, [you can download the latest version of Python instead](https://www.python.org/downloads/).

Note that my video instructions uses Anaconda.

Also, don't forget to download the solver itself. Make sure you unzip it somewhere you can easily access (e.g. Downloads).

## Step 1

### If you downloaded Anaconda

Open Anaconda prompt by searching "Anaconda" in the Windows search bar. Run the following command
```
pip install opencv-python
```
(Experienced developers might be wondering why I'm instructing users to use `pip` instead of `conda`. It's because I'm lazy and don't want to write instructions for `conda`. For our purposes, there's no difference anyways.)

### If you downloaded Python directly

Open command prompt by searching `cmd` in the Windows Search bar. Run the following commands
```
pip install numpy
pip install opencv-python
```

Either way, you should see a message telling you everything downloaded successfully. If you do not receive this message, contact me and I'll help you out. See [Afterword](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#afterword).

## Step 2

You'll want to change your directory to the unzipped folder. If you don't know how to do that:

### 2.1

In File Explorer, go into the Monolith folder (the default title is "UpdatedMonolithSolver-main") and copy the directory link. For example, my directory looked like this 
```
C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main
```
### 2.2

Then in Anaconda prompt, type `cd (whatever you just copied)`. For example, I would input this into my command prompt (press right click to paste)
```
cd C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main
```

If you just unzipped without changing the destimation, type `cd UpdatedMonolithSolver-main` again.

### If you have multiple hard drives...

If you're running the solver in a drive other than your C drive, then you must move to it before cd will work properly. You can type `(drive letter):` to do this. (If you don't understand what this means, then it probably doesn't apply to you.)
	
## Step 3

This step is where you actually start to use the solver. I highly recommend playing in Borderless Windowed mode since you will be pressing Alt+Tab a lot. 

I also recommend muting the game in Volume Mixer and playing your own music, as this minigame's music will most likely drive you insane.

### 3.1

Start a game and take a picture of the board by pressing `Prt Sc`. Then, pause the minigame by opening the controls **(F3 on QWERTY layout)**. 

You can also press `Windows Key + Shift + S`

**Make sure your hammer is away from the board and that you include the full screen.** This is what your screenshot should look like.
![Sample board](https://cdn.discordapp.com/attachments/785252922678181888/1285080932654645358/image.png?ex=66e8f861&is=66e7a6e1&hm=55029455db4d7f5aa6e8675880b0c0384152ef53602f3b8f9585cf77b053068e&)
Notice how the hammer is out of frame in the bottom left corner

### 3.2

Save your paint as a PNG file (JPG works too). Name it something you can easily remember.

If you don't know how, here's a quick-and-dirty way
- Open up Microsoft Paint by searching "paint" in the Windows search bar.
- Paste with `Ctrl + V`
- File -> Save As -> PNG
- Make sure you only save the image and not any extra background white space.

An even quicker and dirtier way is to paste into the DMs of a bot on Discord, clicking the image, "Open Original", and then saving it directly. Whichever way is easier.

### 3.3

**If the image parser fails during this step, then be sure to read the next note. It includes alternate instructions.**

Once that is all saved, go back to Anaconda prompt and type the following command
```
python start.py boardName
```
Replace boardName with whatever you named your screenshot. For example, I included a sample board in the screenshots folder; if I wanted to run the script on this board, I would input
```
python start.py testBoard
```
**If you saved your image as a JPG, include .jpg with the board name.**

### ModuleNotFoundError: No module named 'PIL'

If you get the above error, then run the following command.
```
pip install pillow
```

## Notes on Manually Making the Board

**Skip this note and move to [Step 4](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#step-4) if the parser worked fine for you.** 

Sometimes the parser may fail and generate an incorrect board. This shouldn't happen very often, but is nonetheless possible. If this is your case, go to the 'boards' folder and edit the file called `out`. Refer to the following images for correctly making a board:

This is the board I have

![The board I'd like to recreate](https://cdn.discordapp.com/attachments/786485904176971827/788300313815285770/unknown.png?ex=66e88120&is=66e72fa0&hm=42598a0c44379afa98204aa9b739e67b86ae016f08e5bfdfffd60d6a7a90fbaf&)
  
And this is how I would recreate it

![The recreation in Notepad](https://cdn.discordapp.com/attachments/786485904176971827/788300784487628800/unknown.png?ex=66e88190&is=66e73010&hm=1229fabae024a410d2215ccdf86a278f4a467803ab451ad1f7c4492fd3670659&)

**Note that 1=Gray, 2=Pink, 3=Orange, 4=Blue. Use 0 for open blocks.**

Since the start.py script only takes images as input, you won't be able to use it. To get around this, input the following command into Anaconda prompt
```
python THM.py out
```
Feel free to shoot me a message if you're having trouble (see [Afterword](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#afterword)).

Manually making the board is an incredibly tedious process. If you have to do it from scratch consistently, then I recommend trying out [this](https://github.com/westpipe/treasurefinder) alternate solver (westpipe/treasurefinder).

## Step 4

Once the program is done, it should open a file explorer window with a lot of images titled "step" and some number. Follow those steps in order, starting from Step 0. 

There is a small yellow box around the blob you should click.

### Incomplete Solution

Very rarely, the program may generate an incomplete solution. This is because the program is designed using the A* (A-Star) search algorithm, which stops running on its own after some time. By default, the program terminates once it has checked 5000 board states. If you ever run into this problem, input the following command into Anaconda prompt
```
python THM.py out 100 7500
```
That command will let the program check 7500 boards instead of 5000, increasing the likelihood of finding a more complete solution. It might take a few seconds longer though.

## Accounting for Treasure

**Note that this program does NOT account for your treasure!** As soon as you see treasure, stop following the solver and do everything you can to uncover it, since this solver may not obtain it in the end. (Especially if it's a Monokub.)

### Manually plan out your moves

As the title suggests, simply just plan your next moves manually. You can edit the screenshot you're on if it helps. This is usually pretty easy to do straightforward.

### Using the Solver

You can also have the solver figure plan your moves for you.
1. Head to the folder titles "boards".
2. Duplicate the file named `out`. Rename it to something you can remember, such as `region`.
3. Open it with notepad and delete all its contents
4. Recreate a small area around the treasure **(NOT THE WHOLE BOARD!)**. Refer to [this note](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#notes-on-manually-making-the-board)
5. Run the following command

```
python THM.py region
```

### Generating a new solution

Either way, after you get your treasure successfully, you can take another screenshot of the board and go back to [Step 3](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#step-3). 

Double check the solution it gives you, especially in areas with uncovered treasure. Refer to [this note](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#notes-on-manually-making-the-board) for changing the board manually.

## Restarting

If you have to restart after clearing the entire board, then go to [Step 3](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#step-3). 

If you have to reopen Anaconda/command prompt again, then start at [Step 2](https://github.com/DanLeEpicMan/UpdatedMonolithSolver#step-2) instead.

# Afterword

I hope my explanation was as informative as it could be! The two repositories I borrowed from had their own instructions, but I felt like I should write my own to help streamline everything. Remember that this tool won't guarantee success immediately, and you will most likely have to retry this a few times.

If you run into any issues (or just wanna have a chat), then please feel free to shoot me a message. **My Discord is _danleman1337_. Alternatively, you can add my [Steam account](https://steamcommunity.com/id/danleepicman/) if you prefer to use that instead** (in case the link doesn't work, my friend code is 442227082). I don't really have other contact info, so hopefully those two work with you!

Full credit to both authors I borrowed code from! Feel free to also modify and redistribute this as you wish. Released under MIT License.
