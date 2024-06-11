# Python_Tkinter_BodyMindHealthTracking
Python application that links a GUI(Graphical User Interface using Tkinter library) to a list of objects.

Topic: Body and Mind Health Tracking

--------------------------------//--------------------------------

Brief Description of Main Functionality:

The User will be able to record and track daily data related to mind and body health, the application will assign a score to each activity carried out that day.

So, the User will be able to:

Add a Name, Age, select the Week Day, as well as test your Honesty when selecting how many Litres of Water you drank on the day and if you followed a Healthy Eating. The user will be able to record whether they practiced any activity related to Spiritual Care and Meditation practice. It will also be possible to select whether you practiced the Reading habit that day. Finally, you can record whether you did stretching, choose the type of physical training performed and whether it lasted more than 30 or 60 minutes on the day.

The application will provide the Total Score achieved according to the activities recorded during the day, such as a user percentage metric based on their score and a maximum value (100%) that can be reached in one day. 

The user will be able to consult a specific day of the week to visualise their activity log and day total score.

A Reset button will be available to clear the data.

An Exception will be raised if the user attempts to check the total points scored before any activity is recorded or a Name is entered.

--------------------------------//--------------------------------

Class: User

Class Data will include:        

User Name
User Age (Under / Over 50) —> 0 / 10
Week Day

Hydration Level 1L / 2L / 3L —> 5 / 10 /15
Flag indication whether the User had a Healthy Eating on the day  Bad / Good / Excellent —> 0 / 10 / 15

Spiritual Self Care —> 15
Meditation —> 15

Pre Stretching —> 5
Pos Stretching —> 5
Physical Training Type (HIIT / Strength / HIIT & Strength) —> 7 / 7 /15
Physical Training Time (Under / Over 29 minutes) —>  7 / 15

User Total Score
User Percentage Score

