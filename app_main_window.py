# PYTHON VERSION: 3.12.7

import os.path
import tkinter as tk
from tkinter.messagebox import askyesno
import json

import utils.utiles as util


# Main window
class App:

    # Constants
    GEOMETRY = "600x400"
    BACKGROUND_COLOR = "#1a242b"
    DICT_FOLDER = "texts"
    DICT_FILE = "strings.json"

    # Dictionary to load UI text
    path_dict = os.path.join(DICT_FOLDER, DICT_FILE)
    with open(path_dict, "r", encoding="utf-8") as file:
            strings = json.load(file)

    text_ui = strings["text"]


    def __init__(self):

        # Root window
        self.main_window = tk.Tk()
        self.main_window.geometry(self.GEOMETRY)
        self.main_window.title(self.text_ui["title"])
        self.main_window.configure(bg=self.BACKGROUND_COLOR)
        self.main_window.resizable(False, False)

        # Button to create Sample Size window on click
        self.sample_size_main_window = util.get_button(self.main_window, self.text_ui["get_sample_size"], "blue", self.create_sample_size_window)
        self.sample_size_main_window.place(x=50, y=175)

        # Button to create Margin of Error on click
        self.margin_error_main_window = util.get_button(self.main_window, self.text_ui["get_margin_error"], "blue", self.create_margin_error_window)
        self.margin_error_main_window.place(x=320, y=175)


    # Child class SampleSizeWindow()
    def create_sample_size_window(self):
        # Needs to import file with child class here otherwise you get a circular import
        import childs.sample_size_window as SSW
        self.SSW = SSW.SampleSizeWindow()

    # Child class MarginErrorWindow()
    def create_margin_error_window(self):
        # Needs to import file with child class here otherwise you get a circular import
        import childs.margin_error_window as MEW
        self.MEW = MEW.MarginErrorWindow()

    # Exit button, asks, if yes it closes
    def exit_button(self):
        answer_exit = askyesno(self.text_ui["exit"], self.text_ui["checking_message"])

        if answer_exit:
            self.main_window.destroy()
        else:
            pass

    # Start loop
    def start(self):
        self.main_window.protocol("WM_DELETE_WINDOW", self.exit_button)
        self.main_window.mainloop()
