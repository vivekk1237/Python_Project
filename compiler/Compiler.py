from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

def compile():
    compiler = Tk()
    compiler.title('My Compiler')
    file_path = ''


    def set_file_path(path):
        global file_path
        file_path = path

    # open new file function
    def open_file():
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
            set_file_path(path)

    # save as function
    def save_as():
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)

    # run code function
    def run():
        if file_path == '':
            save_prompt = Toplevel()
            text = Label(save_prompt, text='Please save your code first than run your code....')
            text.pack()
            return
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert('1.0', output)
        code_output.insert('1.0',  error)
        

    # top menu bar for compiler
    menu_bar = Menu(compiler)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_command(label='Save', command=save_as)
    file_menu.add_command(label='Save As', command=save_as)
    file_menu.add_command(label='Exit', command=exit)
    menu_bar.add_cascade(label='File', menu=file_menu)

    run_bar = Menu(menu_bar, tearoff=0)
    run_bar.add_command(label='Run', command=run)
    menu_bar.add_cascade(label='Run', menu=run_bar)
    compiler.config(menu=menu_bar)

    #compiler input text box 
    editor = Text(height=25,width=120,bg="black",font= "times 15", fg="white",cursor="xterm white",insertbackground="white")
    text="#write your code here"
    editor.insert(INSERT,text)
    editor.pack()

    #ouput box
    code_output = Text(width=600,font= "times 17 bold")
    code_output.pack()
    compiler.mainloop()

