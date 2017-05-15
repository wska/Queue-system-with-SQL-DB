#Python 2.7.0
#William Skagerstrom, Teodor Karlgren

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
from ttk import Frame, Label, Entry
from ttk import *
from doctorForm import *
#from main import *


class queuePicker(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.queuePickerForm()



    def queuePickerForm(self):
        self.parent.title("Queue Picker")
        self.pack(fill=BOTH)
        self.parent.geometry("300x300+300+300")



        menuEntry = Entry(self)
        menuQuitButton = Button(self, text ="Exit", command=self.quit)
        menuQuitButton.pack(side=BOTTOM, pady = 5)


        nurseQueueButton1 = Button(self,text="Queue 1", command=self.open_Doctor1)
        nurseQueueButton1.pack(side=BOTTOM, pady = 5)

        nurseQueueButton2 = Button(self,text="Queue 2", command=self.open_Doctor2)
        nurseQueueButton2.pack(side=BOTTOM, pady = 5)

        nurseQueueButton3 = Button(self,text="Queue 3", command=self.open_Doctor3)
        nurseQueueButton3.pack(side=BOTTOM, pady = 5)

        nurseQueueButton4 = Button(self,text="Queue 4", command=self.open_Doctor4)
        nurseQueueButton4.pack(side=BOTTOM, pady = 5)

        nurseQueueButton5 = Button(self,text="Queue 5", command=self.open_Doctor5)
        nurseQueueButton5.pack(side=BOTTOM, pady = 5)

    def quit(self):
        self.parent.destroy()


    def open_Doctor1(self):
        #getQueue(conn, tId)
        self.doctorTeam = 1
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow, self.doctorTeam)

    def open_Doctor2(self):
        #getQueue(conn, tId)
        self.doctorTeam = 2
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow, self.doctorTeam)


    def open_Doctor3(self):
        #getQueue(conn, tId)
        self.doctorTeam = 3
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow, self.doctorTeam)

    def open_Doctor4(self):
        #getQueue(conn, tId)
        self.doctorTeam = 4
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow, self.doctorTeam)

    def open_Doctor5(self):
        #getQueue(conn, tId)
        self.doctorTeam = 5
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow, self.doctorTeam)




class nurseQueueSelect(Frame):

    def __init__(self, parent, patientInfo):
        Frame.__init__(self, parent)
        self.parent = parent
        self.patientInfo = patientInfo
        self.nurseQueueSelectForm()



    def nurseQueueSelectForm(self):
        self.parent.title("Queue Selection")
        self.pack(fill=BOTH)
        self.parent.geometry("300x300+300+300")



        menuEntry = Entry(self)
        menuQuitButton = Button(self, text ="Exit", command=self.quit)
        menuQuitButton.pack(side=BOTTOM, pady = 5)

        queues = self.patientInfo[5]

        '''
        for i in queues:
            if i == 1

            elif

            elif

            elif

            elif

            elif

            '''


    def quit(self):
        self.parent.destroy()


    def open_NurseQueue1(self):
        nurseQueueButton1 = Button(self,text="Queue 1", command=self.open_Doctor1)
        nurseQueueButton1.pack(side=BOTTOM, pady = 5)

    def open_NurseQueue2(self):
        nurseQueueButton2 = Button(self,text="Queue 2", command=self.open_Doctor2)
        nurseQueueButton2.pack(side=BOTTOM, pady = 5)


    def open_NurseQueue3(self):
        nurseQueueButton3 = Button(self,text="Queue 3", command=self.open_Doctor3)
        nurseQueueButton3.pack(side=BOTTOM, pady = 5)

    def open_NurseQueue4(self):
        nurseQueueButton4 = Button(self,text="Queue 4", command=self.open_Doctor4)
        nurseQueueButton4.pack(side=BOTTOM, pady = 5)

    def open_NurseQueue5(self):
        nurseQueueButton5 = Button(self,text="Queue 5", command=self.open_Doctor5)
        nurseQueueButton5.pack(side=BOTTOM, pady = 5)

    def quit(self):
        self.parent.destroy()


    def sendToDatabase(self):
        #getQueue(conn, tId)
        pass









'''
def main():

    root = Tk()
    root.geometry("700x300+300+300")
    app = queuePicker(root)
    root.mainloop()


if __name__ == '__main__':
    main()
'''
