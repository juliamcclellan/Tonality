import tkinter
import json

from watson import analyze

class gui(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.record = tkinter.Button(self, text='Record',command=self.OnClickRecord)
        self.record.grid(column=0,row=0)

        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=1,sticky='EW')
        self.entry.bind('<Return>',self.OnPressEnter)
        self.entryVariable.set('Enter text here')

        enter = tkinter.Button(self,text='Enter text',command=self.OnClickEnter)
        enter.grid(column=1,row=1)

        #self.label = tkinter.Text(self)
        #self.label.insert('1.0',' ')
        #self.label.tag_add('txt', '1.0')
        #self.label.grid(column=0,row=2,sticky='EW')

        self.resizable(True,True)

    def OnPressEnter(self,event):
        self.textAnalyze()

    def OnClickEnter(self):
        self.textAnalyze()

    def OnClickRecord(self):
        pass

    def textAnalyze(self):
        analysis = analyze(self.entryVariable).get())
        print(json.dumps(analysis, indent=2))
        #self.label.tag_delete('txt')

        #self.label.insert(tkinter.INSERT, analysis)


        #self.label.tag_add('txt', '1.0')

if __name__ == "__main__":
    app = gui(None)
    app.title("Tonality")
    app.mainloop()
