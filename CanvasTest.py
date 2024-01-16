# import tkinter
#
#
# def on_selection(event):
#     selected_indices = listbox.curselection()
#     for index in selected_indices:
#         print("Selected items: ", listbox.get(index))
#
#
# # Create main window
# window = tkinter.Tk()
# window.geometry("300x200")
# window.title("PythonExample")
#
# listbox = tkinter.Listbox(window)
# listbox.pack()
#
# listbox.insert(tkinter.END, "item 1")
# listbox.insert(tkinter.END, "item 2")
# listbox.insert(tkinter.END, "item 3")
# listbox.insert(tkinter.END, "item 4")
#
# listbox.bind("<<ListboxSelect>>", on_selection)
# # Create a frame widget
# # frame_1 = tkinter.Frame(window, background="red", padx=50, pady=50)
# # frame_1.pack()
#
# # Create some widgets inside the frame
# # label_1 = tkinter.Label(window, text="This is a label inside frame")
# # label_1.pack()
#
# # # Create a Canvas widget
# # canvas_1 = tkinter.Canvas(window, width=300, height=200)
# # canvas_1.pack()
#
# # # Create a line on the canvas
# # rectangle_1 = canvas_1.create_rectangle(50, 50, 200, 150, fill='green')
#
# window.mainloop()


# ========================================================================================
# import tkinter
# from tkinter import messagebox
#
# window = tkinter.Tk()
# window.geometry("300x200")
#
# messagebox.showinfo("Великолепно", "Всем привет. Добро пожаловать")
# messagebox.showwarning("Shit", "Its a big problem")
#
# result = messagebox.askyesno("Вопрос", "Выбираем да или нет?")
# if result:
#     print("Вы выбрали да")
# else:
#     print("Вы выбрали нет")
#
#
# window.mainloop()

# ================================================================================================================

# import tkinter
# from tkinter import simpledialog
#
# window = tkinter.Tk()
# window.title("PythonExample")
# window.geometry("300x200")
#
# # Вводим данные имени
# input_value = simpledialog.askstring("input", "Введите ваше имя")
# print(input_value)
#
# # Дисплей выводит данные
# user_name = input_value if input_value is not None else "User"
# label = tkinter.Label(window, text="Hello " + user_name + "!")
# label.pack()
#
# window.mainloop()
# =======================================================================================

import tkinter
from tkinter.filedialog import askopenfile

window = tkinter.Tk()
window.title("Example")
window.geometry("300x200")


def open_file():
    file = askopenfile()
    if file:
        lines = file.readlines()
        print(lines)
    else:
        print("Не найде файл")


# Create button
button = tkinter.Button(window, text="Open file", command=open_file)
button.pack()

window.mainloop()