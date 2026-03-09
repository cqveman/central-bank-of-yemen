import customtkinter as ct
from ..settings import *


class FormRow(ct.CTkFrame):
    def __init__(self, parent, row_label, row_row, *args):
        super().__init__(parent, fg_color='transparent')
        self.grid(row=row_row, column=0, sticky='nsew', padx=INNER_CONTAINER, pady=BETWEEN_CARDS)

        self.rowconfigure((0, 1, 2), weight=1, uniform='a')
        ct.CTkLabel(self, text=row_label, font=('Ubuntu', 16)).grid(row=0, column=0, sticky='w')

        for col, (var, field_label) in enumerate(args):
            self.columnconfigure(col, weight=1, uniform='a')
            ct.CTkEntry(self, textvariable=var).grid(row=1, column=col, sticky='ew', padx=(0, BETWEEN_CARDS))
            ct.CTkLabel(self, text=field_label, font=('Ubuntu', 11)).grid(row=2, column=col, sticky='w', padx=(0, BETWEEN_CARDS))
