# Foreword
Hello! I'd just like to immediately state that this tool is not mine. All credit goes to the creator of this program. [Here's the original repository/download](https://github.com/Azshene/THM_Solver).

The reason I'm uploading this is because the original version had a few errors, and I fixed them to make it usable again. I eventually decided to upload my revised edition to make this tool more accessible.

# Instructions
Anyways, I'll give instructions as to how to use this. If you prefer instructions in a video format then [you can find that here](https://youtu.be/Zsg8zKtLgPI), but still I recommend going over these written instructions. I apologize in advance if I come off as pretentious or redundant.

Step 1: Since this program is written in Python, you will need to download Python 3.6 or a newer version. Additionally, you must have the Numpy library installed. 
The Anaconda distribution includes both of these. [Here's the download link for Windows](https://www.anaconda.com/products/individual#windows). If none of this step made sense to you, don't worry! Just download the Anaconda software and move onto Step 2.
(Don't forget to also unzip the Monolith file and put it in a place you can easily access. I personally left it in the Downloads folder)

Step 2: On the search bar in the bottom left of your screen, type the word "Anaconda". A program called "Anaconda Prompt" (or something very similar) should appear. Open it. If you don't have the search bar enabled, you can access it by clicking the Windows icon in the bottom left corner. The search bar should then appear. If you didn't download Anaconda then open command prompt instead. One thing I'd also like to address: I will use Anaconda prompt and command prompt interchangeably. Know that I am referring to the same thing

Step 3: For those of you that have experience with command prompt, simply move into the unzipped folder using the cd command and move onto the next step. For those of you that don't, here's how to do that:

3a: In file explorer, go into the Monolith folder (the default title is "UpdatedMonolithSolver-main") and copy the directory link. For example, my directory looked like this: C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main

3b: Then in Anaconda prompt, type (without quotes) "cd (whatever you just copied)". For example, I would input this into my command prompt: cd C:\Users\Daniel\Downloads\UpdatedMonolithSolver-main

Note for Step 3: If you left the zip extraction destination unchanged then you'll have two folders called "UpdatedMonolithSolver-main". To check if you have two, open the unzipped folder and see if there's a single folder in there called "UpdatedMonolithSolver-main". You can either type "cd UpdatedMonolithSolver-main" or move the inner folder into Downloads (or wherever you'd like to keep it) and delete the empty folder. If you move the inner folder out however, you may need to restart this step.
	
Step 4: This step is probably the most tedious and time-consuming one. I highly recommend playing in Borderless Windowed mode since you will be Alt-Tabbing a lot. I also recommend muting the game in Volume Mixer and playing your own music, as this minigame's music will probably drive you insane.
  
4a: Start a game and take a picture of the board, then pause the minigame by opening the controls (F3 on QWERTY layout). You can use Windows Key+Shift+S to quickly open the snippet tool or press Print Screen (usually styled PrtSc, located near the numpad) to screenshot the entire screen. Alternatively, you can take a picture with your phone. Make sure you save this picture somewhere because you will need to access it. I personally pasted my screenshots in the DMs of a bot on Discord and expanded the image within Discord.
  
4b: In File Explorer, go into the folder called "boards" (located within the main file). You should see 5 files titled "example" and then a number after it. Then open Notepad (you can use the search bar in the bottom left corner to find Notepad)
  
4c: Recreate the board in Notepad. This is easier to explain in pictures so refer to the following images:
  
This is the board I have:
![The board I'd like to recreate](https://cdn.discordapp.com/attachments/786485904176971827/788300313815285770/unknown.png)
  
And this is how I would recreate it in Notepad:
	
![The recreation in Notepad](https://cdn.discordapp.com/attachments/786485904176971827/788300784487628800/unknown.png)
  
As you can see, each block is denoted by a number and separated by commas. Rows are separated by a new line. At first this will be annoying, but eventually you'll get accustomed to it. Notice that every color has a specific number of dots on it (1 for Gray, 2 for Pink, 3 for Orange, 4 for Blue).
	
4d: Once you finish recreating the board, click on "File" and "Save As" in Notepad. A menu that looks like File Explorer should pop up. For the box that says "File name", input "yourname.csv" (yourname can be anything. I used the name myBoard, so I would type myBoard.csv). Once you input the name, change the "Save as type" box to "All Files". Once both of those values are inputted, save your file into the boards folder from Step 4b. You can copy and paste the directory of the boards folder and input it into the newly opened File Explorer if needed. **MAKE SURE THAT IT'S A .CSV FILE AND NOT A .TXT FILE. IF YOU ARE HAVING TROUBLE THEN SIMPLY OPEN ONE OF THE EXAMPLES, PASTE YOUR BOARD INTO THERE, AND RENAME IT!**

Step 5: Once you have your file created, go back to Anaconda prompt and type this: "python THM.py yourname" (without quotes!). yourname is whatever you named your file, without the .csv at the end. For example, I would type "python THM.py myBoard" (without quotes!). **If you get an error while on this step that you can't figure out, please contact me and I'll do my best to help you. My contact information is located in the afterword.**

Note for Step 5: If you get an error about "python" being an unrecognizable command then you must make a PATH variable for it. [Here's instructions detailing how to do that](https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows). If you're using the Anaconda prompt then you won't run into this problem.

Step 6: If you correctly inputted that command then the program should state that it's "finding the best possible solution". After some time the program should say "The best determined solution can be found in the 'solutions folder". Once you notice that, go back to the main folder and go into the folder titled "solutions". In there you should see a bunch of images (typically between 70 and 90). Follow those images step by step (for each image, there is a small yellow box around the block you should click. For reference, the example board from Step 4 has this yellow box). You will have to Alt-Tab and pause a lot, so be warned. 

Note for Step 6: Ideally, you want at least 90% board clearance, since it'll most likely require minimal manual clearing. If you get below 80%, I reccommend starting over since you will have to do a lot of manual clearing. Unfortunately there's no restart option so you will have to spam click the board until you can start a new game.

Step 6.5: **Note that this program does NOT account for your treasure!** It simply gives you the solution with the most blocks destroyed. If you happen to uncover treasure that you would like to be accounted for, manually uncover it. Once that has been done, you can then recreate the board using 0 in place of destroyed blocks and rerun the program (If you would like to read what the original creator said about this, refer to Step 3.5 in their instructions. The original repository is linked in the foreword and afterword).

Step 7: If you have to restart after clearing the entire board, start from Step 4. You do not need to create a new CSV file however; you can simply replace your CSV file's contents with the new board and save it. If you have to open Anaconda prompt again, then start from Step 3 instead.
# Afterword

I hope my explanation was as informative as it could be! The original repository has its own instructions, but I felt like I should write my own. Remember that this tool won't guarantee success immediately, and you will most likely have to retry this many times. I personally used this tool between 10-15 times (not fun). Note that there are two other files that I did not mention. You won't have to use them when generating a solution, but if you're curious check out the original instructions. If you would like to contact me, my Discord is Dan Le Man 2#1890. Alternatively, [my Steam profile can be found here](https://steamcommunity.com/id/danleepicman/) if you prefer to not use Discord.

If you'd like me to convert this into an application with a graphical interface, please message me and give me a nudge because I currently have no serious resolve or motivation to do so. It's something I thought about.

If you are having any trouble please do not hesitate to contact me. I'm absolutely willing to help and I won't judge you for running into problems.

License: [Same one located here](https://github.com/Azshene/THM_Solver); No license, but give credit to the original creator where it's due.
