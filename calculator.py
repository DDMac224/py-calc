import tkinter
from calculate import Calculate


def clear():
    entry_var.set("")


def display(character):
    if character == "=":
        try:
            entry_var.set(calc.solve())
        except SyntaxError as e:
            entry_var.set("SYNTAX ERROR")
            print(e)
        except ArithmeticError as e:
            print(e)
            entry_var.set("ARITHMETIC ERROR")
        except Exception as e:
            print(e)
            entry_var.set("UNEXPECTED ERROR")
    elif character == "\b":
        entry_var.set(entry_var.get()[:-1])
        calc.update(entry_var.get())
    else:
        entry_var.set(f"{entry_var.get()}{character}")
        calc.update(entry_var.get())


def draw_grid(
    entry_var, fonts=[("Arial", 14, "bold"), ("Arial", 14, "normal")], button_width=6
):
    # box and clear row 0
    entry_display = tkinter.Entry(
        frame, bd=2, width=(button_width * 3), textvariable=entry_var, font=fonts[1]
    )
    entry_display.grid(row=0, columnspan=3)
    button_clear = tkinter.Button(
        frame, text="Clear", width=button_width, font=fonts[0], command=clear
    )
    button_clear.grid(row=0, column=3)

    # row 1
    #    button_sin = tkinter.Button(
    #        frame,
    #        text="sin",
    #        width=button_width,
    #        font=fonts[0],
    #        command=lambda: display("sin("),
    #    )
    #    button_sin.grid(row=1, column=0)
    #    button_cos = tkinter.Button(
    #        frame,
    #        text="cos",
    #        width=button_width,
    #        font=fonts[0],
    #        command=lambda: display("cos("),
    #    )
    #    button_cos.grid(row=1, column=1)
    #    button_tan = tkinter.Button(
    #        frame,
    #        text="tan",
    #        width=button_width,
    #        font=fonts[0],
    #        command=lambda: display("tan("),
    #    )
    #    button_tan.grid(row=1, column=2)
    #    button_pi = tkinter.Button(
    #        frame,
    #        text="\u03C0",
    #        width=button_width,
    #        font=fonts[0],
    #        command=lambda: display("\u03C0"),
    #    )
    #    button_pi.grid(row=1, column=3)

    # row 2
    button_lparenth = tkinter.Button(
        frame, text="(", width=button_width, font=fonts[0], command=lambda: display("(")
    )
    button_lparenth.grid(row=2, column=0)
    button_rparenth = tkinter.Button(
        frame, text=")", width=button_width, font=fonts[0], command=lambda: display(")")
    )
    button_rparenth.grid(row=2, column=1)
    button_power = tkinter.Button(
        frame,
        text="^",
        width=button_width,
        font=fonts[0],
        command=lambda: display(" ^ "),
    )
    button_power.grid(row=2, column=2)
    button_back = tkinter.Button(
        frame,
        text="<-",
        width=button_width,
        font=fonts[0],
        command=lambda: display("\b"),
    )
    button_back.grid(row=2, column=3)

    # row 3
    button_1 = tkinter.Button(
        frame, text="1", width=button_width, font=fonts[0], command=lambda: display("1")
    )
    button_1.grid(row=3, column=0)
    button_2 = tkinter.Button(
        frame, text="2", width=button_width, font=fonts[0], command=lambda: display("2")
    )
    button_2.grid(row=3, column=1)
    button_3 = tkinter.Button(
        frame, text="3", width=button_width, font=fonts[0], command=lambda: display("3")
    )
    button_3.grid(row=3, column=2)
    button_plus = tkinter.Button(
        frame,
        text="+",
        width=button_width,
        font=fonts[0],
        command=lambda: display(" + "),
    )
    button_plus.grid(row=3, column=3)

    # row 4
    button_4 = tkinter.Button(
        frame, text="4", width=button_width, font=fonts[0], command=lambda: display("4")
    )
    button_4.grid(row=4, column=0)
    button_5 = tkinter.Button(
        frame, text="5", width=button_width, font=fonts[0], command=lambda: display("5")
    )
    button_5.grid(row=4, column=1)
    button_6 = tkinter.Button(
        frame, text="6", width=button_width, font=fonts[0], command=lambda: display("6")
    )
    button_6.grid(row=4, column=2)
    button_sub = tkinter.Button(
        frame,
        text="-",
        width=button_width,
        font=fonts[0],
        command=lambda: display(" - "),
    )
    button_sub.grid(row=4, column=3)

    # row 5
    button_7 = tkinter.Button(
        frame, text="7", width=button_width, font=fonts[0], command=lambda: display("7")
    )
    button_7.grid(row=5, column=0)
    button_8 = tkinter.Button(
        frame, text="8", width=button_width, font=fonts[0], command=lambda: display("8")
    )
    button_8.grid(row=5, column=1)
    button_9 = tkinter.Button(
        frame, text="9", width=button_width, font=fonts[0], command=lambda: display("9")
    )
    button_9.grid(row=5, column=2)
    button_mult = tkinter.Button(
        frame,
        text="*",
        width=button_width,
        font=fonts[0],
        command=lambda: display(" * "),
    )
    button_mult.grid(row=5, column=3)

    # row 6
    button_0 = tkinter.Button(
        frame, text="0", width=button_width, font=fonts[0], command=lambda: display("0")
    )
    button_0.grid(row=6, column=0)
    button_dec = tkinter.Button(
        frame, text=".", width=button_width, font=fonts[0], command=lambda: display(".")
    )
    button_dec.grid(row=6, column=1)
    button_div = tkinter.Button(
        frame,
        text="/",
        width=button_width,
        font=fonts[0],
        command=lambda: display(" / "),
    )
    button_div.grid(row=6, column=2)
    button_eq = tkinter.Button(
        frame, text="=", width=button_width, font=fonts[0], command=lambda: display("=")
    )
    button_eq.grid(row=6, column=3)


if __name__ == "__main__":
    window = tkinter.Tk()

    window.title("Calculator")
    window.geometry("400x300")
    frame = tkinter.Frame(window)
    frame.pack()

    label_font = ("Arial", 14, "bold")
    entry_font = ("Arial", 14, "normal")
    button_width = 4
    entry_var = tkinter.StringVar()

    calc = Calculate()

    draw_grid(entry_var, fonts=[label_font, entry_font], button_width=button_width)
    window.mainloop()
