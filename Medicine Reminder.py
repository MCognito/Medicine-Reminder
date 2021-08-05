import csv
import winsound
import time
from datetime import datetime
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

#Exist = False

try:
    open("Medicine_Data_File.txt", "x")
    Exist = False
    print("File Does Not Exist, creating file...")
except:
    Exist = True

class newGrid(GridLayout):
    def __init__(self, **kwargs):

        super(newGrid, self).__init__()

        self.cols = 1
        self.within = GridLayout()
        self.within.cols = 4

        self.within.add_widget(Label(text = "Medicine\n  Name: "))
        self.within.add_widget(Label(text="Amount\n   left : "))
        self.within.add_widget(Label(text="  Time \ninterval: "))
        self.within.add_widget(Label(text="Taken or\n   not: "))


        self.s_medName = TextInput(multiline = False)
        self.within.add_widget(self.s_medName)
        self.s_amount = TextInput(multiline = False)
        self.within.add_widget(self.s_amount)
        self.s_timeInterval = TextInput(multiline = False)
        self.within.add_widget(self.s_timeInterval)
        self.s_takenOrNot = CheckBox(active = False)
        self.within.add_widget(self.s_takenOrNot)
        self.add_widget(self.within)
        self.press = Button(text = "Update")
        self.press.bind(on_press=self.Update)
        self.add_widget(self.press)
        self.press = Button(text = "Exit")
        self.press.bind(on_press = self.Exit)
        self.add_widget(self.press)


    def Exit(self, instance):
        quit()

    def Update(self, instance):
        winsound.Beep(2500, 280)
        setHour = datetime.now().hour
        setMin = datetime.now().minute
        setSec = datetime.now().second

        timer = self.s_timeInterval.text
        timer = int(timer)

        MedName = self.s_medName.text
        count = self.s_amount.text
        count = int(count)

        setData = [setHour, setMin, setSec, timer, MedName, count]

        data = open("Medicine_Data_File.txt", "w")

        writer = csv.writer(data)
        writer.writerow(setData)

class ExsistingGrid(GridLayout):
    def __init__(self, **kwargs):

        super(ExsistingGrid, self).__init__()

        self.cols = 1
        self.within = GridLayout()
        self.within.cols = 4

        self.within.add_widget(Label(text = "Medicine\n  Name: "))
        self.within.add_widget(Label(text="Amount\n   left : "))
        self.within.add_widget(Label(text="  Time \ninterval: "))
        self.within.add_widget(Label(text="Taken or\n   not: "))

        with open("Medicine_Data_File.txt", "r") as rowData:
            myCsv = csv.reader(rowData)
            Names = []
            for item in myCsv:
                data = [item]
                Names.append(data)

        self.s_medName = self.within.add_widget(Label(text = Names[0][0][4]))

        self.s_amount = self.within.add_widget(Label(text = Names[0][0][5]))

        self.s_timeInterval = self.within.add_widget(Label(text = Names[0][0][3]))

        self.s_takenOrNot = CheckBox(active=False)
        self.within.add_widget(self.s_takenOrNot)
        self.add_widget(self.within)
        self.press = Button(text="Update")
        self.press.bind(on_press=self.Update)
        self.add_widget(self.press)
        self.press = Button(text="Exit")
        self.press.bind(on_press=self.Exit)
        self.add_widget(self.press)

    def Exit(self, instance):
        quit()

    def Update(self, instance):

        nowHour = datetime.now().hour
        nowMin = datetime.now().minute
        nowSec = datetime.now().second

        with open("Medicine_Data_File.txt", "r") as rowData:
            myCsv = csv.reader(rowData)
            Names = []
            for item in myCsv:
                data = [item]
                Names.append(data)

        setHour = Names[0][0][0]
        setMin = Names[0][0][1]
        setSec = Names[0][0][2]

        timer = Names[0][0][3]

        MedName = Names[0][0][4]
        count = Names[0][0][5]
        count = int(count)

        if self.s_takenOrNot.active:
            count = count - 1
        else:
            pass

        if (nowHour - int(setHour)) >= int(timer):
            winsound.Beep(2500, 280)

            setHour = datetime.now().hour
            setMin = datetime.now().minute
            setSec = datetime.now().second

        else:
            pass

        setData = [setHour, setMin, setSec, timer, MedName, count]

        data = open("Medicine_Data_File.txt", "w")

        writer = csv.writer(data)
        writer.writerow(setData)

class myApp(App):
    def build(self):
        if Exist == False:
            return newGrid()

        elif Exist == True:
            return ExsistingGrid()
        else:
            print("Error")
            quit()

with open("Medicine_Data_File.txt", "r") as rowData:
    myCsv = csv.reader(rowData)
    Names = []
    for item in myCsv:
        data = [item]
        Names.append(data)

if Exist == False:
    if __name__ == "__main__":
        myApp().run()
else:
    pass

now = datetime.now().hour

while Exist == True and (now - int(Names[0][0][0])) >= int(Names[0][0][3]):
    if __name__ == "__main__":
        winsound.Beep(2200, 280)
        winsound.Beep(2200, 280)
        time.sleep(1)
        winsound.Beep(2200, 280)
        winsound.Beep(2200, 280)
        myApp().run()
