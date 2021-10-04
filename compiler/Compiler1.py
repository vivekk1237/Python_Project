from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

def compile():
    compiler = Tk()
    compiler.title('My Compiler')




    # save as function


    # run code function
    def run():
        hello=open('P:/PythonProjects/LocoPy/compiler/hello.py','w')
        hello.truncate()
        hello.close()
        with open('P:/PythonProjects/LocoPy/compiler/hello.py', 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            file.close()
        command = f'python P:/PythonProjects/LocoPy/compiler/hello.py'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.delete('1.0', 'end')
        code_output.insert('1.0', output)
        code_output.insert('1.0',  error)
        

    # top menu bar for compiler
    menu_bar = Menu(compiler)


    run_bar = Menu(menu_bar, tearoff=0)
    run_bar.add_command(label='Run', command=run)
    menu_bar.add_cascade(label='Run', menu=run_bar)
    compiler.config(menu=menu_bar)

    #compiler input text box 
    editor = Text(height=25,width=120,bg="black",font= "times 15", fg="white",cursor="xterm white",insertbackground="white")
    editor.insert(INSERT, "#write Your code here")
    editor.pack()

    #ouput box
    code_output = Text(width=600,font= "times 17 bold")
    code_output.pack()
    compiler.mainloop()

