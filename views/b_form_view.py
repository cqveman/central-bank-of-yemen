import ttkbootstrap as tb
import tkinter as tk


class BuildForm(tb.Frame):
    NEW_FIELD_PADDING = 12
    LABEL_FONT = ("Ubuntu", 12)
    SMALL_FONT = ("Ubuntu", 9)
    FORM_WIDTH = 520

    def __init__(self, parent, app, title):
        super().__init__(parent)
        self.app = app

        self.container = tb.Frame(self)
        self.container.pack(expand=True)

        self.card = tb.Frame(self.container, padding=30)
        self.card.pack()
        self.card.configure(width=BuildForm.FORM_WIDTH)

        tb.Label(self.card, text="Central Bank of Yemen", font=("Ubuntu", 22, "bold")).pack()
        tb.Label(self.card, text=title, font=("Ubuntu", 16)).pack(pady=(0, 20))

    def build_field(self, label, var, *, show=None, help_text=None):
        frame = tb.Frame(self.card)
        frame.pack(fill="x", pady=BuildForm.NEW_FIELD_PADDING)

        tb.Label(frame, text=label, font=self.LABEL_FONT).pack(anchor="w")
        tb.Entry(frame, textvariable=var, show=show).pack(fill="x")

        if help_text:
            tb.Label(frame, text=help_text, font=self.SMALL_FONT).pack(anchor="w")

    def build_row(self, fields):
        frame = tb.Frame(self.card)
        frame.pack(fill="x", pady=BuildForm.NEW_FIELD_PADDING)

        columns = []

        for i, (label, var, kwargs) in enumerate(fields):
            col = tb.Frame(frame)
            col.pack(side="left", expand=True, fill="x", padx=5)

            tb.Label(col, text=label, font=BuildForm.LABEL_FONT).pack(anchor="w")
            entry = tb.Entry(col, textvariable=var, **kwargs)
            entry.pack(fill="x")

            columns.append((col, entry))

        return columns
