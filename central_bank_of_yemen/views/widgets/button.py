import customtkinter as ct
from ..settings import *

class Button(ct.CTkButton):
    def __init__(self, parent, label, command, row, rowspan=1):
        super().__init__(parent, text=label, command=command, font=('Ubuntu',12,'bold'))
        self.grid(row=row, rowspan=rowspan,column=0, padx=INNER_CONTAINER)