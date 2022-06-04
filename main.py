import tkinter as tk
from tkinter import ttk

from file_organizer import organize

# root window
root = tk.Tk()
root.geometry('1000x500')
root.resizable(False, False)
root.title('File Organizer Tool')


def organized_file(event = None):
    result = organize(path_input_area.get())
    response.config(text="Provided Input: " + f'{result[0]}\n{result[1]}')
    response_1.config(text= ''.join(result[2]))

root.bind('<Return>',organized_file)
tk.Label(root, text="Folder Location").place(x=20, y=60)

path_input_area = tk.Entry(root, width=80)
path_input_area.place(x=130, y=60)

# organized button
organize_button = ttk.Button(
    root,
    text='Organize',
    command=lambda: organized_file()
)

organize_button.place(x=870, y=60)

response = tk.Label(root, text="")
response.pack()
response_1 = tk.Label(root, text="")
response_1.place(x=100, y=100)

root.mainloop()
