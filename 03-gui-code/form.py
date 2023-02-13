from tkinter import *

class Form():
    def __init__(self, labels, parent=None):
        labelsize = max(len(i) for i in labels) + 2
        form = Frame(parent)
        form.pack(expand=YES, fill=X)
        rows = Frame(form, bd=2, relief=GROOVE)
        rows.pack(side=TOP, expand=YES, fill=X)
        self.content = {}
        for label in labels:
            row = Frame(rows)
            row.pack(fill=X)
            Label(row, text=label, width=labelsize).pack(side=LEFT)
            entry = Entry(row)
            entry.pack(side=RIGHT, expand=YES, fill=X)
            self.content[label] = entry
        Button(form, text='Cancel', command=self.onCancel).pack(side=RIGHT)
        Button(form, text='Submit', command=self.onSubmit).pack(side=RIGHT)
        form.master.bind('<Return>', (lambda event: self.onSubmit()))

    def onSubmit(self):
        for key in self.content:
            print(key, '\t=>\t', self.content[key].get())
        
    def onCancel(self):
        Tk().quit()
    
class DynamicForm(Form):
    def __init__(self, labels=None):
        labels = input('Enter the labels names: ').split()
        Form.__init__(self, labels)

    def onSubmit(self):
        Form.onSubmit(self)
        self.onCancel()

if __name__ == '__main__':
    import sys
    if sys.argv == 1:
        Form(['Name', 'Age', 'Job'])
    else:
        DynamicForm()
    mainloop()
    