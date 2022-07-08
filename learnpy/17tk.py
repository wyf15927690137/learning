"""
测试
"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序的写法"""

    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.pythonHobby = IntVar()
        self.javaHobby = IntVar()
        self.cppHobby = IntVar()

        print(self.pythonHobby.get())  # 默认值为0
        self.c1 = Checkbutton(self, text='python', variable=self.pythonHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text='java', variable=self.javaHobby, onvalue=1, offvalue=0)
        self.c3 = Checkbutton(self, text='cpp', variable=self.cppHobby, onvalue=1, offvalue=0)
        self.c1.pack(side='left')
        self.c2.pack(side='left')
        self.c3.pack(side='left')

        Button(self, text='确定', command=self.choice).pack(side='left')

    def choice(self):
        if self.pythonHobby.get() == 1:
            messagebox.showinfo('python', '人生苦短，我用python！')
            self.cppHobby.set(1)
        if self.javaHobby.get() == 1:
            messagebox.showinfo('java', 'java是世界上排行第一的语言！')
        if self.cppHobby.get() == 1:
            messagebox.showinfo('cpp', 'cpp是世界上排行第一的语言！')


if __name__ == "__main__":
    root = Tk()
    root.geometry('400x60+200+200')
    root.title('please select a computer language')
    app = Application(master=root)
    root.mainloop()
