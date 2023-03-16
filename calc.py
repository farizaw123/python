import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
# izaz
OFF_WHITE = "#afbcdb"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#2e3547"
LABEL_COLOR = "#25265E"
SAMA_DENGAN ="#f56b02"


class Calculator:
    def __init__(izaz):
    # fungsi window
        izaz.window = tk.Tk()
        izaz.window.geometry("375x697")
        izaz.window.resizable(0, 0)
        izaz.window.title("Calculator")

    # ----------------------------------

    # menampilkan display
        izaz.total_expression = ""
        izaz.current_expression = ""
        izaz.display_frame = izaz.create_display_frame()
        izaz.total_label, izaz.label = izaz.create_display_labels()
    # ------------------------------

    # membuat row digit dan simbol operasi
        izaz.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3), # 1 didepan koma itu row, klo 1 dibelakang koma barisnya jadi kalo (1,1) artinya row 1 baris 1
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        izaz.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} #membuat perintah operasi
        izaz.buttons_frame = izaz.create_buttons_frame()
    # ------------------------------------
        izaz.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            izaz.buttons_frame.rowconfigure(x, weight=1)
            izaz.buttons_frame.columnconfigure(x, weight=1)
        izaz.create_digit_buttons()
        izaz.create_operator_buttons()
        izaz.create_special_buttons()
        izaz.bind_keys()

    def bind_keys(izaz):
        izaz.window.bind("<Return>", lambda event: izaz.evaluate())
        izaz.window.bind("<BackSpace>", lambda event: izaz.backspace())
        izaz.window.bind("<Escape>", lambda event: izaz.clear())
        for key in izaz.digits:
            izaz.window.bind(str(key), lambda event, digit=key: izaz.add_to_expression(digit))

        for key in izaz.operations:
            izaz.window.bind(key, lambda event, operator=key: izaz.append_operator(operator))


# deklarasi button
    def create_special_buttons(izaz):
        izaz.create_clear_button()
        izaz.create_equals_button()
        izaz.create_square_button()
        izaz.create_backspace_button()
# ------------------

        
# menampilkan angka display
    def create_display_labels(izaz):
        total_label = tk.Label(izaz.display_frame, text=izaz.total_expression, wraplength=375, justify="right",anchor=tk.E, bg=LIGHT_GRAY,
                               fg=WHITE, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(izaz.display_frame, wraplength=375, justify="right", text=izaz.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=WHITE, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(izaz):
        frame = tk.Frame(izaz.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
# ------------------------


    def add_to_expression(izaz, value):
        izaz.current_expression += str(value)
        izaz.update_label()

    def create_digit_buttons(izaz):
        for digit, grid_value in izaz.digits.items():
            button = tk.Button(izaz.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: izaz.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=2, pady=2)

    def append_operator(izaz, operator):
        izaz.current_expression += operator
        izaz.total_expression += izaz.current_expression
        izaz.current_expression = ""
        izaz.update_total_label()
        izaz.update_label()

    def create_operator_buttons(izaz):
        i = 0
        for operator, symbol in izaz.operations.items():
            button = tk.Button(izaz.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: izaz.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW, padx=2, pady=2)
            i += 1


# fungsi clear
    def clear(izaz):
        izaz.current_expression = ""
        izaz.total_expression = ""
        izaz.update_label()
        izaz.update_total_label()

    def create_clear_button(izaz):
        button = tk.Button(izaz.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                           borderwidth=0, command=izaz.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW, padx=2, pady=2)
# ---------------------



# fungsi pangkat
    def square(izaz):
        izaz.current_expression = str(eval(f"{izaz.current_expression}**2"))
        izaz.update_label()

    def create_square_button(izaz):
        button = tk.Button(izaz.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                           borderwidth=0, command=izaz.square)
        button.grid(row=0, column=2, sticky=tk.NSEW, padx=2, pady=2)
# ----------------------


# fungsi backspace
    def backspace(izaz):
        if len(izaz.current_expression) > 0:
            izaz.current_expression = izaz.current_expression[:-1]
            izaz.update_label() 

    def create_backspace_button(izaz):
        button = tk.Button(izaz.buttons_frame, text="\u232B", bg=OFF_WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                           borderwidth=0, command=izaz.backspace)
        button.grid(row=0, column=3, sticky=tk.NSEW, padx=2, pady=2)
# ---------------------



# fungs hasil final
    def evaluate(izaz):
        izaz.total_expression += izaz.current_expression
        izaz.update_total_label()
        try:
            izaz.current_expression = str(eval(izaz.total_expression))

            izaz.total_expression = ""
        except Exception as e:
            izaz.current_expression = "Error"
        finally:
            izaz.update_label()

    def create_equals_button(izaz):
        button = tk.Button(izaz.buttons_frame, text="=", bg=SAMA_DENGAN, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=izaz.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW, padx=2, pady=2)
# --------------------




    def create_buttons_frame(izaz):
        frame = tk.Frame(izaz.window, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(izaz):
        expression = izaz.total_expression
        for operator, symbol in izaz.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        izaz.total_label.config(text=expression)

    def update_label(izaz):
        izaz.label.config(text=izaz.current_expression)

    def run(izaz):
        izaz.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()