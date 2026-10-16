# Simple Tkinter GUI calculator
# Run: python gui_calc.py

import tkinter as tk

class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.expr = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.expr, font=("Segoe UI",18), justify='right', bd=4, relief='ridge')
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
        buttons = [
            ('C',1,0), ('⌫',1,1), ('%',1,2), ('/',1,3),
            ('7',2,0), ('8',2,1), ('9',2,2), ('*',2,3),
            ('4',3,0), ('5',3,1), ('6',3,2), ('-',3,3),
            ('1',4,0), ('2',4,1), ('3',4,2), ('+',4,3),
            ('0',5,0), ('.',5,1), ('=',5,2)
        ]
        for (txt,r,c) in buttons:
            if txt=='=':
                btn = tk.Button(self, text=txt, command=self.calculate, bg="#5cb85c", fg="white", width=6, height=2)
                btn.grid(row=r, column=c, columnspan=2, sticky="nsew")
            else:
                btn = tk.Button(self, text=txt, command=lambda t=txt: self.press(t), width=6, height=2)
                btn.grid(row=r, column=c, sticky="nsew")
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def press(self, ch):
        if ch=='C':
            self.expr.set('')
        elif ch=='⌫':
            self.expr.set(self.expr.get()[:-1])
        else:
            self.expr.set(self.expr.get() + ch)

    def calculate(self):
        import re
        s = self.expr.get()
        try:
            if not re.fullmatch(r"[0-9+\-*/().% ]+", s):
                raise ValueError("Invalid chars")
            s = re.sub(r"(\d+(\.\d+)?)%", r"(\1/100)", s)
            result = eval(s, {"__builtins__":None}, {})
            self.expr.set(str(result))
        except Exception:
            self.expr.set("Error")
            self.after(700, lambda: self.expr.set(''))

if __name__ == "__main__":
    Calc().mainloop()