import tkinter as tk
from tkinter import messagebox
import os
from Config import Config


class WarningUI:
    def __init__(self, title, msg):
        self.title = title
        self.msg = msg

    def showMsg(self):
        messagebox.showinfo(self.title, self.msg)


class SettingsUI:
    def __init__(self):
        curFolder = os.path.dirname(os.path.abspath(__file__))
        self.window = tk.Tk()
        if os.name == 'nt':
            self.iconPath = curFolder + r'\resource\setting.ico'
        else:
            self.iconPath = curFolder + r'/resource/setting.xbm'
        self.releaseMainAllInOne = tk.IntVar()
        self.releaseIsrAllInOne = tk.IntVar()

        self.releaseSwitch = tk.IntVar()
        self.cgcSwitch = tk.IntVar()
        self.allSwitch = tk.IntVar()
        self.fidelitySwitch = tk.IntVar()

        self.releaseSwitchDef = 1
        self.allSwitchDef = 0
        self.cgcSwitchDef = 0
        self.fidelitySwitchDef = 0
        
        self.projectFidelity = tk.IntVar()
        self.projectCGC = tk.IntVar()
        self.projectAllProject = tk.IntVar()

        self.onWindows = tk.IntVar()
        self.onLinux = tk.IntVar()

        self.isCancelled = False

    def onOkClicked(self):
        if not self.onWindows.get() and not self.onLinux.get():
            messagebox.showinfo("Platform", "Must select at least 1 build platform!")
            return

        self.window.destroy()

    def onCancelClicked(self):
        self.isCancelled = True
        self.window.destroy()

    def onClosing(self):
        self.isCancelled = True
        self.window.destroy()

    def setReleaseSwitchingDef(self, value):
        self.releaseSwitchDef = value

    def setALLSwitchingDef(self, allVal):
        self.allSwitchDef = allVal

    def setCGCSwitchingDef(self, cgcVal):
        self.cgcSwitchDef = cgcVal

    def setFidelitySwitchingDef(self, fidelityVal):
        self.fidelitySwitchDef = fidelityVal

    def setReleaseSwitching(self, value):
        self.releaseSwitch.set(value)
        self.onReleaseSwitching()

    def setALLSwitching(self, value):
        self.allSwitch.set(value)
        self.onALLSwitching()

    def setCGCSwitching(self, value):
        self.cgcSwitch.set(value)
        self.onCGCSwitching()


    def setFidelitySwitching(self, value):
        self.fidelitySwitch.set(value)
        self.onFidelitySwitching()

    def onReleaseSwitching(self):
        release = self.releaseSwitch.get()
        if release == 1:  # Main QT
            self.releaseMainAllInOne.set(1)
            self.releaseIsrAllInOne.set(0)
        elif release == 2:  # RTM QT
            self.releaseMainAllInOne.set(0)
            self.releaseIsrAllInOne.set(1)
        else:
            print("Unknown Release!")
        
    def onCGCSwitching(self):
        cgc = self.cgcSwitch.get()
        if cgc == 1:
            self.projectCGC.set(1)

    def onFidelitySwitching(self):
        fidelity = self.fidelitySwitch.get()
        if fidelity == 1:
            self.projectFidelity.set(1)

    def onALLSwitching(self):
        all = self.allSwitch.get()
        if all == 1:
            self.projectAllProject.set(1)
        
    def showWindow(self, isCGC):
        self.window.title('Setting for Build')
        if os.name == 'nt':
            self.window.wm_iconbitmap(bitmap=self.iconPath)
        width = 420
        height = 220
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

        downHeight = 10
        tk.Label(self.window, text='Release: ').place(x=20, y=downHeight)
        rbMainAllInOne = tk.Radiobutton(self.window, text='Main Branch', variable=self.releaseSwitch, value=1, command=self.onReleaseSwitching)
        rbMainAllInOne.config(state="disabled")
        rbIsrAllInOne = tk.Radiobutton(self.window, text='ISR Branch', variable=self.releaseSwitch, value=2, command=self.onReleaseSwitching)
        rbIsrAllInOne.config(state="disabled")

        downHeight += 20
        rbMainAllInOne.place(x=50, y=downHeight)
        rbMainAllInOne.select()
        rbIsrAllInOne.place(x=250, y=downHeight)
        downHeight += 30
        tk.Label(self.window, text='Projects: ').place(x=20, y=downHeight)

        downHeight += 20

        chkCGCProject = tk.Checkbutton(self.window, text= Config.JobCGC, variable=self.cgcSwitch, onvalue= 1, offvalue= 0, command=self.onCGCSwitching)
        chkFidelityProject = tk.Checkbutton(self.window, text= Config.JobFidelity, variable=self.fidelitySwitch, onvalue= 1, offvalue= 0, command=self.onFidelitySwitching)
        chkAllProject = tk.Checkbutton(self.window, text= Config.JobAll, variable=self.allSwitch, onvalue= 1, offvalue= 0, command=self.onALLSwitching)

        chkAllProject.place(x=50, y=downHeight)
        chkAllProject.config(state="disabled")
        chkCGCProject.place(x=150, y=downHeight)
        chkCGCProject.config(state="disabled")
        chkFidelityProject.place(x=250, y=downHeight)
        chkFidelityProject.config(state="disabled")

        downHeight += 30
        tk.Label(self.window, text='Platform on: ').place(x=20, y=downHeight)
        chkWin = tk.Checkbutton(self.window, text='Windows', variable=self.onWindows, onvalue=1, offvalue=0)
        chkLinux = tk.Checkbutton(self.window, text='Linux', variable=self.onLinux, onvalue=1, offvalue=0)

        downHeight += 20
        chkWin.place(x=50, y=downHeight)
        chkLinux.place(x=250, y=downHeight)
        chkLinux.select()
        chkLinux.config(state="disabled")
        if isCGC == True:
            chkWin.select()
            chkWin.config(state="disabled")

        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)

        bottomFrame = tk.Frame(self.window, borderwidth=1)
        bottomFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        okBtn = tk.Button(self.window, text='OK', width=8, command=self.onOkClicked)
        cancelBtn = tk.Button(self.window, text='Cancel', width=8, command=self.onCancelClicked)
        cancelBtn.pack(in_=bottomFrame, side=tk.RIGHT, padx=15, pady=12)
        okBtn.pack(in_=bottomFrame, side=tk.RIGHT, padx=1, pady=12)

        self.setReleaseSwitching(self.releaseSwitchDef)
        self.setALLSwitching(self.allSwitchDef)
        self.setCGCSwitching(self.cgcSwitchDef)
        self.setFidelitySwitching(self.fidelitySwitchDef)
        self.window.mainloop()


if __name__ == "__main__":
    ui = SettingsUI()
    ui.showWindow()
    print(ui.isCancelled)

    if ui.releaseMainAllInOne.get():
        print('Main Branch')
    if ui.releaseIsrAllInOne.get():
        print('ISR Branch')

    print('switch: ' + str(ui.releaseSwitch.get()))

    if ui.onWindows.get():
        print('Windows')

    if ui.onLinux.get():
        print('Linux')

    if ui.projectCGC.get():
        print('CGC')

    if ui.projectFidelity.get():
        print('Fidelity')

        