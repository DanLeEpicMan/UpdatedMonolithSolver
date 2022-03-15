# Foreword
Hello! I'd just like to immediately state that this tool is not mine. All credit goes to the creator of this program. [Here's the original repository/download](https://github.com/Azshene/THM_Solver).

The reason why I'm uploading this is because the original version had a few errors, and I fixed them to restore the program. Eventually, I decided to upload my revised edition in order to make this tool more accessible.

# Instructions
To clarify, these instructions assume that you are using a computer with Windows; if you are not using Windows, then you must know how to navigate files, use your OS's command-line interpreter, and create CSV files (I recommend using the original repository's instructions if this is your case). Also, if you prefer instructions in a video format then [you can find that here](https://youtu.be/2Rf2MQzMCJ8). I apologize in advance if I come off as pretentious, condescending, or redundant.

Also know that you are free to contact me for whatever reason, whether you run into a problem with the program, want some tips for 100% completion, or simply want to talk. My contact information can be found in the afterword.

Step 1: Since this program is written in Python, you will need to download Python 3.6 or a newer version. Additionally, you must also have the NumPy library installed. The Anaconda distribution includes both of these: [here's the download link for Windows](https://www.anaconda.com/products/individual#windows). If none of this step made sense to you, don't worry! Just download the Anaconda software and move onto Step 2. Moreover, don't forget to download this solver and unzip it to an easily accessible place, such as Downloads folder (which is where I put it!). You should also omit the "UpdatedMonolithSolver-main" bit from the extraction destination, as doing so will create a single folder instead of two folders.

Step 2: On the search bar in the bottom left corner of your screen, type the word "Anaconda". Open the program named "Anaconda Prompt" (or something very similar to that). If you don't have the search bar enabled, you can access it by clicking the Windows icon in the bottom left corner. If you didn't download Anaconda then open command prompt instead. I may also use "Anaconda prompt" and "Command prompt" interchangeably, so be aware of that in case there's any confusion.

Step 3: For those of you that have experience with command prompt, simply move into the unzipped folder using the cd command and move onto the next step. For those of you that don't, here's how to do that:

3a: In File Explorer, go into the Monolith folder (the default title is "UpdatedMonolithSolver-main") and copy the directory link. For example, my directory looked like this: C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main

3b: Then in Anaconda prompt, type (without quotes) "cd (whatever you just copied)". For example, I would input this into my command prompt: cd C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main

Note for Step 3: If you left the zip extraction destination unchanged from Step 1 then you'll have two folders called "UpdatedMonolithSolver-main". To check if you have two, open the unzipped folder and see if there's a single folder in there called "UpdatedMonolithSolver-main". You can either type "cd UpdatedMonolithSolver-main" or move the inner folder into Downloads (or wherever you'd like to keep it) and delete the empty folder.

Note #2: If you place the Monolith folder in a drive other than the C: drive, then you must move to that drive first before the cd command will work properly. To accomplish this, simply type "(drive letter):" in command prompt (e.g. if you put the Monolith folder in your D: drive, type "D:" in the command prompt and it will move you there). If you ever need to verify whether you're in the right spot, type "dir" and see if command prompt displays the folder's contents (namely "boards", "THM.py", "sprites", etc.)
	
Step 4: This step is probably the most tedious and time-consuming one. I highly recommend playing in Borderless Windowed mode since you will be pressing Alt+Tab a lot. I also recommend muting the game in Volume Mixer and playing your own music, as this minigame's music will most likely drive you insane.

**Before you continue on**, consider this alternative approach. The next few steps instruct you to input the board from the start. Instead of using the solver at the beginning, you can try to uncover some treasures on your own and then input the board midway through. While more heuristic and less determinant, I feel like this approach allows incorporation of some personal strategy, thereby reducing total time spent on this terrible minigame. This was not my idea but instead someone else's ("HyungOppaHelper" from the comments of the YouTube instructions). Regardless, the difference between this approach and the following is when you decide to pause the game and make the board. Whichever one you prefer is up to your discretion.

4a: Start a game and take a picture of the board, then pause the minigame by opening the controls **(F3 on QWERTY layout)**. You can use Windows Key+Shift+S to quickly open the snippet tool or press Print Screen (usually styled PrtSc, located near the numpad) to screenshot the entire screen. Alternatively, you can take a picture with a phone or some other camera. Make sure you save this picture somewhere because you will need to refer to it.
  
4b: In File Explorer, go into the folder called "boards" (located within the main Monolith folder). You should see 5 text files titled "example" and then a number after it. Then open Notepad (you can use the search bar in the bottom left corner to find Notepad)
  
4c: Recreate the board in Notepad. This is easier to explain in pictures so refer to the following images:

This is the board I have:
![The board I'd like to recreate](https://cdn.discordapp.com/attachments/786485904176971827/788300313815285770/unknown.png)
  
And this is how I would recreate it in Notepad:
	
![The recreation in Notepad](https://cdn.discordapp.com/attachments/786485904176971827/788300784487628800/unknown.png)
  
As you can see, each block is denoted by a number and separated by commas. Rows are separated by a new line. At first this will be annoying, but eventually you'll get accustomed to it. Notice that every color has a specific number of dots on it (1 for Gray, 2 for Pink, 3 for Orange, 4 for Blue). For any empty cells, use 0 to denote it.
	
4d: Once you finish recreating the board, click on "File" and "Save As" in Notepad. A menu that looks like File Explorer should pop up. For the box that says "File name", input "yourname.csv" (yourname can be anything; I used the name myBoard, so I would type myBoard.csv). Once you input the name, change the "Save as type" box to "All Files". Once both of those values are inputted, save your file into the boards folder from Step 4b. You can copy and paste the directory of the boards folder and input it into the newly opened File Explorer window if needed. **MAKE SURE THAT IT'S A .CSV FILE AND NOT A .TXT FILE. IF YOU ARE HAVING TROUBLE THEN SIMPLY OPEN ONE OF THE EXAMPLES, PASTE YOUR BOARD INTO THERE, AND RENAME IT!**

Step 5: Once you have your file created, go back to Anaconda prompt and type "python THM.py yourname" (without quotes!). yourname is whatever you named your file, without the .csv at the end (e.g. I would type "python THM.py myBoard"). **If you get an error while on this step that you can't figure out, please contact me and I'll do my best to help you. As mentioned earlier, my contact information is located in the afterword.**

Step 6: If you correctly inputted that command then the program should state that it's "finding the best possible solution". After some time the program should say "The best determined solution can be found in the 'solutions folder". Once you notice that, go back to the main folder and go into the folder titled "solutions". In there you should see a large series of images (typically between 70 and 90). Follow those images step by step (for each image, there is a small yellow box around the block you should click. For reference, the example board from Step 4 has this yellow box at x-y coordinate (9,9)). You will have to Alt+Tab and pause a lot, so be warned. 

Note for Step 6: Ideally, you want at least 90% board clearance, since it'll most likely require minimal manual clearing. If you get below 80%, I reccommend starting over since you will have to do a lot of manual clearing. Unfortunately there's no restart option, so you will have to spam click the board until you can start a new game.

Note #2: Very rarely, the program may generate an incomplete solution. This is because the program is designed using the A* (A-Star) algorithm, which is similar to a trial-and-error method of searching (huge oversimplification by the way). By default, the program terminates once it has checked 5000 board states. If you ever run into this problem, I recommend inputting the following command into command prompt: "python THM.py yourname 100 7500" (without quotes and replace yourname). That command will allow the program to check 7500 boards instead of 5000, increasing the likelihood of finding a more complete solution (You can change 7500 to any number you'd like by the way; 10000 is good too, though a tad too much. You could also decrease the number if you want to speed up the runtime, although this makes the returning of an incomplete and suboptimal solution more likely).

Step 6.5: **Note that this program does NOT account for your treasure!** It simply gives you the solution with the most blocks destroyed. Recall that you should have at least 2 Monokubs and 3-4 fish to earn the achievement, so if you happen to uncover treasure that you would like to be accounted for, I recommend manually clearing it. Once that has been done, you can then recreate the board using 0 in place of destroyed blocks and rerun the program. This step is of course optional and will increase the amount of time spent on an individual board, but I recommend following it, as it will make the solution more useful, possibly reducing the total amount of attempts and, consequently, the total time spent on this atrocious minigame.

Step 7: If you have to restart after clearing the entire board, then go to Step 4. You do not need to create a new CSV file however; you can simply replace your CSV file's contents with the new board and save it. If you have to open Anaconda prompt again, then go to Step 3 instead.
# Afterword

If you run into any issues (or just wanna have a chat), then please feel free to shoot me a message. **My Discord is _Dan Le Man 2#1890_. Alternatively, you can add my [Steam account](https://steamcommunity.com/id/danleepicman/) if you prefer to use that instead** (in case the link doesn't work, my friend code is 442227082). I don't really have other contact info, so hopefully those two work with you!

I hope my explanation was as informative as it could be! The original repository has its own instructions, but I felt like I should write my own. Remember that this tool won't guarantee success immediately, and you will most likely have to retry this many times. I personally used this tool between 10-15 times (not fun). Note that there are two other files that I did not mention. You won't have to use them when generating a solution, but if you're curious check out the original instructions.

In the future I hope to add my own bit to this program by automating Step 4 (the Board-to-Notepad process). I thought of a way to approach this, namely a program that will take a picture of the board, partition the board into a grid, and checking the color at each individual location, thereby converting the color into a number. I imagine this is much easier said than done, but honestly the hardest part of this sounds like partitioning the board, since image recognition models exist online that I could "borrow". Hopefully I'll be able to figure this out one day so I can both contribute to a (partial) end of suffering and add more than bug fixes.

License: [Same one located here](https://github.com/Azshene/THM_Solver); No license, but give credit to the original creator when due.
