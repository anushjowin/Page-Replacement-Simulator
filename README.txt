PAGE REPLACEMENT ALGORITHM SIMULATOR
====================================

Project Title:
--------------
Design and Implementation of a Page Replacement Algorithm Simulator Using Python


Project Description:
--------------------
This project is a GUI-based simulator developed using Python and Tkinter
to demonstrate the working of Page Replacement Algorithms in Operating Systems.

The simulator allows users to enter a reference string and the number of
memory frames, and then visualize how different page replacement algorithms
manage memory pages during execution.

The implemented algorithms are:
    1. FIFO (First-In-First-Out)
    2. LRU (Least Recently Used)
    3. Optimal Page Replacement


Features:
---------
• Modern graphical user interface using Tkinter
• Step-by-step memory frame visualization
• Animated simulation of page replacement
• Real-time graphical comparison of page faults
• Algorithm explanation popup
• Error handling for invalid inputs


Technologies Used:
------------------
• Python 3.x
• Tkinter (GUI Development)
• Matplotlib (Graph Visualization)


How to Run the Project:
-----------------------
1. Install Python (if not already installed).
2. Install required library:

   pip install matplotlib

3. Open terminal in the project folder.
4. Run the program using:

   python gui_page_replacement.py

5. Enter:
   - Reference String (space separated values)
   - Number of Frames
   - Select Algorithm
6. Click "Run Simulation" or "Compare All".


Sample Input:
-------------
Reference String:
7 0 1 2 0 3 0 4 2 3 0 3 2

Number of Frames:
3


Output:
-------
• Step-by-step frame updates
• Total number of page faults
• Bar graph comparison of FIFO, LRU, and Optimal


Algorithm Overview:
-------------------
FIFO:
Replaces the oldest page in memory based on queue principle.

LRU:
Replaces the page that has not been used for the longest time.

Optimal:
Replaces the page that will not be used for the longest time in the future.
It produces the minimum possible page faults (theoretical benchmark).


Conclusion:
-----------
This project demonstrates the practical working of major page replacement
algorithms and helps in understanding memory management concepts in
Operating Systems.


Course:
-------
Operating Systems Lab / Mini Project

Year:
-----
2026
