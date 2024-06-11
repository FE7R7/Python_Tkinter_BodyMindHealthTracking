from tkinter import *

from tkinter import simpledialog

from Assignment_1_Y2_S1_Body_Mind import *

window = Tk()
window.geometry("725x712")
window.title("Get Healthy")


# -------------End of tkinter/window settings-------------

def display(index):
    global current
    global user
    user = userList[index]
    current = index

    entry2.delete(0, END)
    entry2.insert(END, user.getWeekDaySelected())
    entry3.delete(0, END)
    entry3.insert(END, user.getUserName())
    entry4.delete(0, END)
    entry4.insert(END, user.getUserAge())
    entry5.delete(0, END)
    entry5.insert(END, user.getHydrationLevel())
    entry6.delete(0, END)
    entry6.insert(END, user.getHealthEating())
    entry7.delete(0, END)
    entry7.insert(END, user.getSpiritualSelfCare())
    entry8.delete(0, END)
    entry8.insert(END, user.getMeditation())
    entry9.delete(0, END)
    entry9.insert(END, user.getPreStretching())
    entry10.delete(0, END)
    entry10.insert(END, user.getPosStretching())
    entry11.delete(0, END)
    entry11.insert(END, user.getTrainingType())
    entry12.delete(0, END)
    entry12.insert(END, user.getTrainingTime())
    entryMsg.delete(0, END)

    entryTotal.delete(0, END)
    entryPercent.delete(0, END)

    weekDayVar.set("Select")
    ageVar.set("Select")
    hydrationVar.set("Select")
    healthEatingVar.set("Select")
    yesNoSpiritVar.set("Select")
    yesNoMeditationVar.set("Select")
    yesNoPreStretchVar.set("Select")
    yesNoPosStretchVar.set("Select")
    trainingTypeVar.set("Select")
    trainingTimeVar.set("Select")


# -------------End of event handling methods-------------

def weekDayCmd():
    day = str(weekDayVar.get())
    user.addWeekDay(day)
    display(current)


def ageCmd():
    try:
        age = ageVar.get()
        user.addAge(age)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")


# -------------

def hydrateCmd():
    try:
        hydrate = hydrationVar.get()
        user.addHydration(hydrate)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


def eatCmd():
    try:
        eat = healthEatingVar.get()
        user.addEating(eat)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


# -------------

def spiritCmd():
    try:
        spirit = yesNoSpiritVar.get()
        user.addSpiritual(spirit)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


def meditateCmd():
    try:
        meditate = yesNoMeditationVar.get()
        user.addMeditation(meditate)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


# -------------

def preStretchCmd():
    try:
        pre = yesNoPreStretchVar.get()
        user.addPreStretch(pre)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


def posStretchCmd():
    try:
        pos = yesNoPosStretchVar.get()
        user.addPosStretch(pos)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


# -------------

def trainingTypeCmd():
    try:
        tType = trainingTypeVar.get()
        user.addTrainingType(tType)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


def trainingTimeCmd():
    try:
        tTime = trainingTimeVar.get()
        user.addTrainingTime(tTime)
        display(current)

    except NoWeekDaySelected:
        entryMsg.insert(END, "No Week Day Selected!! ")

    except NoAgeSelected:
        entryMsg.insert(END, "No Age Selected!! ")


# -------------

def totalScoreCmd():
    totalResult = user.getTotalScore()
    entryTotal.delete(0, END)
    entryTotal.insert(END, (str(totalResult) + " Day Points"))


def percentageScoreCmd():
    percentResult = user.percentageScoreResult()
    entryPercent.delete(0, END)
    entryPercent.insert(END, (str(percentResult) + " %"))


# -------------

def resetCmd():
    global current
    user.resetAll()
    display(current)


# -------------

def nextCmd():
    global current
    if (current < (len(userList) - 1)):
        current += 1
        display(current)


def prevCmd():
    global current
    if (current > 0):
        current -= 1
        display(current)


# -------------

def firstCmd():
    display(0)


def lastCmd():
    display(len(userList) - 1)


# -------------End of Command(Cmd) Functions-------------

def clearData():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry11.delete(0, END)
    entry12.delete(0, END)
    entryMsg.delete(0, END)


def insertNewUser():
    userName = simpledialog.askstring("", "Please, Type Your Name: ")

    newUser = User(userName)
    userList.append(newUser)
    display(len(userList) - 1)


# ----------------------------------End of Method Declarations---------------------------------------


user1 = User("Fernando")
user2 = User("Andre")
user3 = User("Jose")
user4 = User("Marcia")
user5 = User("Reiki")
user6 = User("Daiane")
user7 = User("Benjamin")
user8 = User("Lavinia")

userList = [user1, user2, user3, user4, user5, user6, user7, user8]
global current
global user
user = userList[0]

# --------------End of Name List of Initial Users definitions ---------------


menu1 = Menu(window)
window.config(menu=menu1)
subm1 = Menu(menu1)
menu1.add_cascade(label="Add_User_Options", menu=subm1)
subm1.add_command(label="Clear User Data", font=("arial", 12, "bold"), command=clearData)
subm1.add_command(label="Insert New User", font=("arial", 12, "bold"), command=insertNewUser)

# --------------------------End of window menu definitions----------------------------


frame = Frame(window, width=200, height=250)
frame.place(x=10, y=80)

# --------------------------------End of frame settings-------------------------------


# -----------------------------------Display Labels-----------------------------------

label1 = Label(window, text="Body and Mind Health Tracking", fg="green", font=("arial", 20, "bold"))
label1.place(x=220, y=30)

label1_1 = Label(window, text="---------------------------------------------------------", fg="green",
                 font=("arial", 16, "bold"))
label1_1.place(x=217, y=57)

# ----------------------------

label2 = Label(frame, text="                Week Day: ", fg="blue", width=7, font=("arial", 16, "bold"))
label2.grid(row=0, column=1, sticky=W + E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=2, sticky=W + E)

# ----------------------------

labelBlank = Label(frame,
                   text="     ---------------------------------------------------------",
                   fg="blue", width=15, font=("arial", 16, "bold"))
labelBlank.grid(row=1, column=0, columnspan=4, sticky=W + E)

# ----------------------------

label3 = Label(frame, text="Name: ", fg="blue", width=15, font=("arial", 12, "bold"))
label3.grid(row=2, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=2, column=1, sticky=W + E)

# --------

label4 = Label(frame, text="Age: ", fg="blue", width=15, font=("arial", 12, "bold"))
label4.grid(row=2, column=2, sticky=W + E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=3, column=0, columnspan=2, sticky=W + E)

# ----------------------------

label5_1 = Label(frame, text="Nutrition and Hydration: ", fg="yellow", bg="grey", width=15, font=("arial", 16, "bold"))
label5_1.grid(row=4, column=0, columnspan=4, sticky=W + E)

# --------

label5 = Label(frame, text="Hydration Level: ", fg="blue", width=15, font=("arial", 12, "bold"))
label5.grid(row=5, column=0, sticky=W + E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=5, column=1, sticky=W + E)

# --------

label6 = Label(frame, text="Health Eating: ", fg="blue", width=15, font=("arial", 12, "bold"))
label6.grid(row=5, column=2, sticky=W + E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=5, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=6, column=0, columnspan=2, sticky=W + E)

# ----------------------------

label7_1 = Label(frame, text="Mind: ", fg="yellow", bg="grey", width=15, font=("arial", 16, "bold"))
label7_1.grid(row=7, column=0, columnspan=4, sticky=W + E)

# --------

label7 = Label(frame, text="Spiritual Care: ", fg="blue", width=15, font=("arial", 12, "bold"))
label7.grid(row=8, column=0, sticky=W + E)

entry7 = Entry(frame)
entry7.insert(END, '0')
entry7.grid(row=8, column=1, sticky=W + E)

# --------

label8 = Label(frame, text="Meditation: ", fg="blue", width=15, font=("arial", 12, "bold"))
label8.grid(row=8, column=2, sticky=W + E)

entry8 = Entry(frame)
entry8.insert(END, '0')
entry8.grid(row=8, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=9, column=0, columnspan=2, sticky=W + E)

# ----------------------------

label9_1 = Label(frame, text="Body: ", fg="yellow", bg="grey", width=15, font=("arial", 16, "bold"))
label9_1.grid(row=10, column=0, columnspan=4, sticky=W + E)

# --------

label9 = Label(frame, text="Pre Stretching: ", fg="blue", width=15, font=("arial", 12, "bold"))
label9.grid(row=11, column=0, sticky=W + E)

entry9 = Entry(frame)
entry9.insert(END, '0')
entry9.grid(row=11, column=1, sticky=W + E)

# --------

label10 = Label(frame, text="Pos Stretching: ", fg="blue", width=15, font=("arial", 12, "bold"))
label10.grid(row=11, column=2, sticky=W + E)

entry10 = Entry(frame)
entry10.insert(END, '0')
entry10.grid(row=11, column=3, sticky=W + E)

# --------

label11 = Label(frame, text="Training Type: ", fg="blue", width=15, font=("arial", 12, "bold"))
label11.grid(row=12, column=0, sticky=W + E)

entry11 = Entry(frame)
entry11.insert(END, '0')
entry11.grid(row=12, column=1, sticky=W + E)

# --------

label12 = Label(frame, text="Training Time: ", fg="blue", width=15, font=("arial", 12, "bold"))
label12.grid(row=12, column=2, sticky=W + E)

entry12 = Entry(frame)
entry12.insert(END, '0')
entry12.grid(row=12, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=13, column=0, columnspan=2, sticky=W + E)

# ----------------------------


labelBlank = Label(frame,
                   text="------------------------------------------------------------------------------------------------------------------------------------",
                   fg="blue",
                   width=15,
                   font=("arial", 16, "bold"))
labelBlank.grid(row=14, column=0, columnspan=4, sticky=W + E)

# -----------------------------------------Buttons----------------------------------------

button1 = Button(frame, text="Week Day: ", fg="blue", font=("arial", 12, "bold"), command=weekDayCmd)
button1.grid(row=15, column=0, sticky=W + E)

listWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekDayVar = StringVar()
combo1 = OptionMenu(frame, weekDayVar, *listWeek)
weekDayVar.set("Select")
combo1.grid(row=15, column=1, sticky=W + E)

# --------

button2 = Button(frame, text="Age 50+: ", fg="blue", font=("arial", 12, "bold"), command=ageCmd)
button2.grid(row=15, column=2, sticky=W + E)

listAge = range(17, 101)
ageVar = StringVar()
combo1 = OptionMenu(frame, ageVar, *listAge)
ageVar.set("Select")
combo1.grid(row=15, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=16, column=0, columnspan=2, sticky=W + E)

# ----------------------------


labelBlank = Label(frame, text="Hydration & Nutrition: ", fg="yellow", bg="grey", width=15,
                   font=("arial", 16, "bold"))
labelBlank.grid(row=17, column=0, columnspan=4, sticky=W + E)

# ----------------------------


button3 = Button(frame, text="Hydration Level", fg="blue", font=("arial", 12, "bold"), command=hydrateCmd)
button3.grid(row=18, column=0, sticky=W + E)

listHydration = ['1 L', '2 L', '3 L']
hydrationVar = StringVar()
combo1 = OptionMenu(frame, hydrationVar, *listHydration)
hydrationVar.set("Select")
combo1.grid(row=18, column=1, sticky=W + E)

# --------

button4 = Button(frame, text="Health Eating", fg="blue", font=("arial", 12, "bold"), command=eatCmd)
button4.grid(row=18, column=2, sticky=W + E)

listHealthEating = ['Bad', 'Good', 'Excellent']
healthEatingVar = StringVar()
combo1 = OptionMenu(frame, healthEatingVar, *listHealthEating)
healthEatingVar.set("Select")
combo1.grid(row=18, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=19, column=0, columnspan=2, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text="Mind: ", fg="yellow", bg="grey", width=15, font=("arial", 16, "bold"))
labelBlank.grid(row=20, column=0, columnspan=4, sticky=W + E)

# ----------------------------

button5 = Button(frame, text="Spiritual Care: ", fg="blue", font=("arial", 12, "bold"), command=spiritCmd)
button5.grid(row=21, column=0, sticky=W + E)

listYesNo = ['Yes', 'No']
yesNoSpiritVar = StringVar()
combo1 = OptionMenu(frame, yesNoSpiritVar, *listYesNo)
yesNoSpiritVar.set("Select")
combo1.grid(row=21, column=1, sticky=W + E)

# --------

button6 = Button(frame, text="Meditation: ", fg="blue", font=("arial", 12, "bold"), command=meditateCmd)
button6.grid(row=21, column=2, sticky=W + E)

listYesNo = ['Yes', 'No']
yesNoMeditationVar = StringVar()
combo1 = OptionMenu(frame, yesNoMeditationVar, *listYesNo)
yesNoMeditationVar.set("Select")
combo1.grid(row=21, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=22, column=0, columnspan=2, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text="Body: ", fg="yellow", bg="grey", width=15, font=("arial", 16, "bold"))
labelBlank.grid(row=23, column=0, columnspan=4, sticky=W + E)

# ----------------------------

button7 = Button(frame, text="Pre Stretching: ", fg="blue", font=("arial", 12, "bold"), command=preStretchCmd)
button7.grid(row=24, column=0, sticky=W + E)

listYesNo = ['Yes', 'No']
yesNoPreStretchVar = StringVar()
combo1 = OptionMenu(frame, yesNoPreStretchVar, *listYesNo)
yesNoPreStretchVar.set("Select")
combo1.grid(row=24, column=1, sticky=W + E)

# --------

button8 = Button(frame, text="Pos Stretching", fg="blue", font=("arial", 12, "bold"), command=posStretchCmd)
button8.grid(row=24, column=2, sticky=W + E)

listYesNo = ['Yes', 'No']
yesNoPosStretchVar = StringVar()
combo1 = OptionMenu(frame, yesNoPosStretchVar, *listYesNo)
yesNoPosStretchVar.set("Select")
combo1.grid(row=24, column=3, sticky=W + E)

# ----------------------------

button9 = Button(frame, text="Training Type", fg="blue", font=("arial", 12, "bold"), command=trainingTypeCmd)
button9.grid(row=25, column=0, sticky=W + E)

listTrainingType = ['HIIT', 'Strength', 'HIIT & Strength']
trainingTypeVar = StringVar()
combo1 = OptionMenu(frame, trainingTypeVar, *listTrainingType)
trainingTypeVar.set("Select")
combo1.grid(row=25, column=1, sticky=W + E)

# --------

button10 = Button(frame, text="Training Time", fg="blue", font=("arial", 12, "bold"), command=trainingTimeCmd)
button10.grid(row=25, column=2, sticky=W + E)

listTrainingTime = ['30+ Min', '30- Min']
trainingTimeVar = StringVar()
combo1 = OptionMenu(frame, trainingTimeVar, *listTrainingTime)
trainingTimeVar.set("Select")
combo1.grid(row=25, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame,
                   text="------------------------------------------------------------------------------------------------------------------------------------",
                   fg="blue", width=15, font=("arial", 16, "bold"))
labelBlank.grid(row=26, column=0, columnspan=4, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text="Day Achievement: ", fg="yellow", bg="grey", width=15, font=("arial", 16, "bold"))
labelBlank.grid(row=27, column=0, columnspan=4, sticky=W + E)

# ----------------------------

buttonTotal = Button(frame, text="Total Score: ", fg="blue", font=("arial", 12, "bold"), command=totalScoreCmd)
buttonTotal.grid(row=28, column=0, sticky=W + E)

entryTotal = Entry(frame)
entryTotal.insert(END, '0')
entryTotal.grid(row=28, column=1, sticky=W + E)

# --------

buttonPercentage = Button(frame, text="Percentage Score: ", fg="blue", font=("arial", 12, "bold"),
                          command=percentageScoreCmd)
buttonPercentage.grid(row=28, column=2, sticky=W + E)

entryPercent = Entry(frame)
entryPercent.insert(END, '0')
entryPercent.grid(row=28, column=3, sticky=W + E)

# ----------------------------

labelBlank = Label(frame,
                   text="------------------------------------------------------------------------------------------------------------------------------------",
                   fg="blue", width=15, font=("arial", 16, "bold"))
labelBlank.grid(row=29, column=0, columnspan=4, sticky=W + E)

# ----------------------------

labelBlank = Label(frame, text="Navigation: ", fg="yellow", bg="grey", width=15, font=("arial", 16, "bold"))
labelBlank.grid(row=30, column=0, columnspan=4, sticky=W + E)

# ----------------------------

button11 = Button(frame, text="Next", fg="blue", font=("arial", 12, "bold"), command=nextCmd)
button11.grid(row=31, column=0, sticky=W + E)

# --------

button12 = Button(frame, text="Prev", fg="blue", font=("arial", 12, "bold"), command=prevCmd)
button12.grid(row=31, column=1, sticky=W + E)

# ----------------------------


button13 = Button(frame, text="First", fg="blue", font=("arial", 12, "bold"), command=firstCmd)
button13.grid(row=31, column=2, sticky=W + E)

# --------

button14 = Button(frame, text="Last", fg="blue", font=("arial", 12, "bold"), command=lastCmd)
button14.grid(row=31, column=3, sticky=W + E)

# ----------------------------

button15 = Button(frame, text="Reset Data", fg="blue", font=("arial", 12, "bold"), command=resetCmd)
button15.grid(row=32, column=0, sticky=W + E)

# ----------------------------

labelMsg = Label(frame, text="       Error Message: ", fg="Red", width=15, font=("arial", 14, "bold"))
labelMsg.grid(row=32, column=1, sticky=W + E)

entryMsg = Entry(frame)
entryMsg.insert(END, '')
entryMsg.grid(row=32, column=2, columnspan=2, sticky=W + E)

# -------------------------------------------------------------------------------

display(0)

window.mainloop()
