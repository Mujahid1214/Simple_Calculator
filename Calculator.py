import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator - By Mujahid Toorie")
        self.window.geometry("400x600")
        self.window.resizable(False, False)
        self.window.configure(bg='#2c3e50')

        # Variables
        self.expression = ""
        self.display_value = tk.StringVar(value="0")

        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(
            self.window,
            text="By Mujahid Toorie",
            font=('Arial', 16, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=(20, 15))

        # Display screen
        display_frame = tk.Frame(self.window, bg='#34495e', bd=5, relief='raised')
        display_frame.pack(pady=10, padx=20, fill='x')

        self.display = tk.Label(
            display_frame,
            textvariable=self.display_value,
            font=('Digital', 28, 'bold'),
            bg='#1a1a1a',
            fg='#00ff00',
            anchor='e',
            padx=15,
            pady=15,
            relief='sunken',
            bd=3
        )
        self.display.pack(fill='both', expand=True)

        # Buttons frame
        button_frame = tk.Frame(self.window, bg='#2c3e50')
        button_frame.pack(pady=20, padx=20, fill='both', expand=True)

        # Configure grid
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)

        # Row 0: Clear and operators
        self.create_button(button_frame, "C", 0, 0, '#e74c3c', self.clear, colspan=2)
        self.create_button(button_frame, "÷", 0, 2, '#f39c12', lambda: self.add_to_expression("÷"))
        self.create_button(button_frame, "×", 0, 3, '#f39c12', lambda: self.add_to_expression("×"))

        # Row 1: Numbers 7,8,9 and minus
        self.create_button(button_frame, "7", 1, 0, '#3498db', lambda: self.add_to_expression("7"))
        self.create_button(button_frame, "8", 1, 1, '#3498db', lambda: self.add_to_expression("8"))
        self.create_button(button_frame, "9", 1, 2, '#3498db', lambda: self.add_to_expression("9"))
        self.create_button(button_frame, "−", 1, 3, '#f39c12', lambda: self.add_to_expression("−"))

        # Row 2: Numbers 4,5,6 and plus
        self.create_button(button_frame, "4", 2, 0, '#3498db', lambda: self.add_to_expression("4"))
        self.create_button(button_frame, "5", 2, 1, '#3498db', lambda: self.add_to_expression("5"))
        self.create_button(button_frame, "6", 2, 2, '#3498db', lambda: self.add_to_expression("6"))
        self.create_button(button_frame, "+", 2, 3, '#f39c12', lambda: self.add_to_expression("+"))

        # Row 3: Numbers 1,2,3 and equals (spans 2 rows)
        self.create_button(button_frame, "1", 3, 0, '#3498db', lambda: self.add_to_expression("1"))
        self.create_button(button_frame, "2", 3, 1, '#3498db', lambda: self.add_to_expression("2"))
        self.create_button(button_frame, "3", 3, 2, '#3498db', lambda: self.add_to_expression("3"))
        self.create_button(button_frame, "=", 3, 3, '#27ae60', self.calculate, rowspan=2)

        # Row 4: Zero and decimal
        self.create_button(button_frame, "0", 4, 0, '#3498db', lambda: self.add_to_expression("0"), colspan=2)
        self.create_button(button_frame, ".", 4, 2, '#9b59b6', lambda: self.add_to_expression("."))

    def create_button(self, parent, text, row, col, color, command, colspan=1, rowspan=1):
        btn = tk.Button(
            parent,
            text=text,
            font=('Arial', 16, 'bold'),
            bg=color,
            fg='white',
            relief='raised',
            bd=3,
            command=command,
            activebackground=color,
            activeforeground='white'
        )
        btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan,
                 padx=2, pady=2, sticky='nsew')
        return btn

    def add_to_expression(self, value):
        # If display shows "0" and we're adding a number, replace it
        if self.display_value.get() == "0" and value.isdigit():
            self.expression = value
        # If display shows "Error", clear it first
        elif self.display_value.get() == "Error":
            self.expression = value
        else:
            self.expression += value

        # Update display
        self.display_value.set(self.expression)

    def calculate(self):
        try:
            if self.expression:
                # Replace symbols with Python operators
                calc_expression = self.expression
                calc_expression = calc_expression.replace("×", "*")
                calc_expression = calc_expression.replace("÷", "/")
                calc_expression = calc_expression.replace("−", "-")

                # Calculate result
                result = eval(calc_expression)

                # Format result (remove unnecessary decimal places)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                # Update display and expression
                self.display_value.set(str(result))
                self.expression = str(result)

        except ZeroDivisionError:
            self.display_value.set("Error")
            self.expression = ""
        except:
            self.display_value.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display_value.set("0")

    def run(self):
        self.window.mainloop()


# Run the calculator
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()