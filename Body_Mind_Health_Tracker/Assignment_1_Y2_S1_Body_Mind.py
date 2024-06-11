class NoWeekDaySelected(Exception): pass


class NoAgeSelected(Exception): pass


# ---------------------- End of Exceptions ----------------------#

class User:

    def __init__(self, userName):

        self.__userName = userName
        self.__weekDaySelected = ''
        self.__userAge = ''
        self.__hydrationLevel = ''
        self.__healthEating = ''
        self.__spiritualSelfCare = ''
        self.__meditation = ''
        self.__preStretching = ''
        self.__posStretching = ''
        self.__trainingType = ''
        self.__trainingTime = ''
        self.__totalScore = 0
        self.__percentageScore = 0
        self.__totalActivities = 0

    # ---------------------- End of Constructor ----------------------#
    def resetAll(self):

        self.__weekDaySelected = ''
        self.__userAge = ''
        self.__hydrationLevel = ''
        self.__healthEating = ''
        self.__spiritualSelfCare = ''
        self.__meditation = ''
        self.__preStretching = ''
        self.__posStretching = ''
        self.__trainingType = ''
        self.__trainingTime = ''
        self.__totalScore = 0
        self.__percentageScore = 0
        self.__totalActivities = 0

    # ---------------------- End of Reset All ----------------------#

    def addWeekDay(self, day):
        self.__weekDaySelected = day

    def addAge(self, age):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        else:

            self.__userAge = age

            if (self.__userAge != 'Select'):

                if (self.__userAge >= '50'):
                    self.__userAge = str(age) + ' --> 10+'
                    self.__totalScore += 10
                    self.__totalActivities += 2

                elif (self.__userAge < '50'):
                    self.__userAge = str(age)
                    self.__totalScore += 0
                    self.__totalActivities += 1
            else:
                self.__userAge = str(age)
                self.__totalScore += 0
                self.__totalActivities += 0

    def addHydration(self, hydration):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:

            self.__hydrationLevel = hydration

            if self.__hydrationLevel == '1 L':
                self.__hydrationLevel = hydration + ' --> 5+'
                self.__totalScore += 5
                self.__totalActivities += 1

            elif self.__hydrationLevel == '2 L':
                self.__hydrationLevel = hydration + ' --> 10+'
                self.__totalScore += 10
                self.__totalActivities += 2

            elif self.__hydrationLevel == '3 L':
                self.__hydrationLevel = hydration + ' --> 15+'
                self.__totalScore += 15
                self.__totalActivities += 3

            else:
                self.__hydrationLevel = 'Select'
                self.__totalScore += 0
                self.__totalActivities += 0

    def addEating(self, eating):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:

            self.__healthEating = eating

            if self.__healthEating == 'Bad':
                self.__healthEating = 'None'
                self.__totalScore += 0
                self.__totalActivities += 0

            elif self.__healthEating == 'Good':
                self.__healthEating = eating + ' --> 10+'
                self.__totalScore += 10
                self.__totalActivities += 1

            elif self.__healthEating == 'Excellent':
                self.__healthEating = eating + ' --> 15+'
                self.__totalScore += 15
                self.__totalActivities += 2

    def addSpiritual(self, spirit):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:

            self.__spiritualSelfCare = spirit

            if (self.__spiritualSelfCare == 'Yes'):
                self.__spiritualSelfCare = spirit + ' --> 15+'
                self.__totalScore += 15
                self.__totalActivities += 1

            elif (self.__spiritualSelfCare == 'No'):
                self.__spiritualSelfCare = 'None'
                self.__totalScore += 0
                self.__totalActivities += 0

    def addMeditation(self, meditate):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:

            self.__meditation = meditate

            if (self.__meditation == 'Yes'):
                self.__meditation = meditate + ' --> 15+'
                self.__totalScore += 15
                self.__totalActivities += 1

            elif (self.__meditation == 'No'):
                self.__meditation = 'None'
                self.__totalScore += 0
                self.__totalActivities += 0

    def addPreStretch(self, preStretch):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:

            self.__preStretching = preStretch

            if (self.__preStretching == 'Yes'):
                self.__preStretching = preStretch + ' --> 5+'
                self.__totalScore += 5
                self.__totalActivities += 1

            elif (self.__preStretching == 'No'):
                self.__preStretching = 'None'
                self.__totalScore += 0
                self.__totalActivities += 0

    def addPosStretch(self, posStretch):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:

            self.__posStretching = posStretch

            if (self.__posStretching == 'Yes'):
                self.__posStretching = posStretch + ' --> 5+'
                self.__totalScore += 5
                self.__totalActivities += 1

            elif (self.__posStretching == 'No'):
                self.__posStretching = 'None'
                self.__totalScore += 0
                self.__totalActivities += 0

    def addTrainingType(self, tType):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:
            self.__trainingType = tType

            if (self.__trainingType == 'HIIT'):
                self.__trainingType = tType + ' --> 7+'
                self.__totalScore += 7
                self.__totalActivities += 1
            elif (self.__trainingType == 'Strength'):
                self.__trainingType = tType + ' --> 7+'
                self.__totalScore += 7
                self.__totalActivities += 1
            elif (self.__trainingType == 'HIIT & Strength'):
                self.__trainingType = tType + ' --> 15+'
                self.__totalScore += 15
                self.__totalActivities += 2

            else:
                self.__trainingType = 'Select'
                self.__totalScore += 0
                self.__totalActivities += 0

    def addTrainingTime(self, tTime):
        if (self.__weekDaySelected == ''):

            raise NoWeekDaySelected

        elif (self.__userAge == ''):

            raise NoAgeSelected

        else:
            self.__trainingTime = tTime

            if (self.__trainingTime == '30- Min'):
                self.__trainingTime = tTime + ' --> 7+'
                self.__totalScore += 7
                self.__totalActivities += 1
            elif (self.__trainingTime == '30+ Min'):
                self.__trainingTime = tTime + ' --> 15+'
                self.__totalScore += 15
                self.__totalActivities += 2

            else:
                self.__trainingTime = 'Select'
                self.__totalScore += 0
                self.__totalActivities += 0

    # ---------------------- End of add Functions ----------------------#

    def totalScoreSum(self, totalScore):

        self.__totalScore += totalScore

    def percentageScoreResult(self):

        self.__percentageScore = format((((self.__totalScore + self.__totalActivities) * 100) / 114), '.2f')
        return self.__percentageScore

    # ---------------------- End of totalScore & percentageScore Functions ----------------------#

    def getWeekDaySelected(self):
        return self.__weekDaySelected

    def getUserName(self):
        return self.__userName

    def getUserAge(self):
        return self.__userAge

    def getHydrationLevel(self):
        return self.__hydrationLevel

    def getHealthEating(self):
        return self.__healthEating

    def getSpiritualSelfCare(self):
        return self.__spiritualSelfCare

    def getMeditation(self):
        return self.__meditation

    def getPreStretching(self):
        return self.__preStretching

    def getPosStretching(self):
        return self.__posStretching

    def getTrainingType(self):
        return self.__trainingType

    def getTrainingTime(self):
        return self.__trainingTime

    def getTotalScore(self):
        return self.__totalScore

    # ---------------------- End of get Functions ----------------------#
