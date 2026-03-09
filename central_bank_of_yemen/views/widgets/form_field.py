import customtkinter as ct
from ..settings import *


class FormField(ct.CTkFrame):
    def __init__(self, parent, field_label, var, row, column=0, columnspan=1, show=None):
        super().__init__(parent, fg_color='transparent')
        self.grid(row=row, column=column, columnspan=columnspan, sticky='nsew',
                  padx=INNER_CONTAINER, pady=BETWEEN_CARDS)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1), weight=1, uniform='a')

        ct.CTkLabel(self, text=field_label, font=('Ubuntu', 16)).grid(row=0, column=0, sticky='w')
        if show:
            ct.CTkEntry(self, textvariable=var, show=show).grid(row=1, column=0, sticky='ew')
        else:
            ct.CTkEntry(self, textvariable=var).grid(row=1, column=0, sticky='ew')
