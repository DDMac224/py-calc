import tkinter as tk
from calculate import Calculate
from display import Display


def main():
    root = tk.Tk()

    root.title("Calculator")
    root.geometry("400x300")
    frame = tk.Frame(root)
    frame.pack()

    display_buttons = (
        ("(", ")", "^", "<-"),
        ("1", "2", "3", "+"),
        ("4", "5", "6", "-"),
        ("7", "8", "9", "*"),
        ("0", ".", "/", "="),
    )

    text_box_font = ("Arial", 14, "bold")
    button_font = ("Arial", 14, "normal")
    button_width = 4

    calc = Calculate()
    display = Display(
        frame, display_buttons, calc, (text_box_font, button_font), button_width
    )

    root.mainloop()


if __name__ == "__main__":
    main()
