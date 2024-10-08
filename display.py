import tkinter as tk


class Display:
    def __init__(
        self,
        root,
        buttons,
        calc,
        fonts=(("Arial", 14, "bold"), ("Arial", 14, "normal")),
        button_width=6,
    ):
        self.__root = root
        self.__entry_var = tk.StringVar()
        self.__entry_var.set("")

        self.__rows, self.__columns = len(buttons), len(buttons[0])
        if self.__rows == 0 or self.__columns == 0:
            raise IndexError("buttons list cannon be empty")

        self.__assign_buttons(buttons, fonts, button_width, calc)

    def __assign_buttons(self, buttons, fonts, button_width, calc):
        tk.Entry(
            self.__root,
            bd=2,
            width=(button_width * len(buttons[0])),
            textvariable=self.__entry_var,
            font=fonts[1],
        ).grid(row=0, columnspan=len(buttons[0]) - 1)
        tk.Button(
            self.__root,
            text="Clear",
            width=button_width,
            font=fonts[0],
            command=lambda: self.__button_press("clear", calc),
        ).grid(row=0, column=len(buttons[0]) - 1)

        for i in range(self.__rows):
            for j in range(self.__columns):
                tk.Button(
                    self.__root,
                    text=buttons[i][j],
                    width=button_width,
                    font=fonts[1],
                    command=lambda x=buttons[i][j]: self.__button_press(x, calc),
                ).grid(row=i + 1, column=j)

    def __button_press(self, action, calc):
        if action == "clear":
            self.__entry_var.set("")
            calc.update(self.__entry_var.get())
        elif action == "=":
            try:
                self.__entry_var.set(calc.solve())
            except SyntaxError as e:
                self.__entry_var.set("SYNTAX ERROR")
                print(e)
            except ArithmeticError as e:
                print(e)
                self.__entry_var.set("ARITHMETIC ERROR")
            except Exception as e:
                print(e)
                self.__entry_var.set("UNEXPECTED ERROR")
        elif action == "<-":
            self.__entry_var.set(self.__entry_var.get()[:-1])
            calc.update(self.__entry_var.get())
        else:
            self.__entry_var.set(f"{self.__entry_var.get()}{action}")
            calc.update(self.__entry_var.get())
