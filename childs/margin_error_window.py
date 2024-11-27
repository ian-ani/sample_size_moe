# PYTHON VERSION: 3.12.7

import tkinter as tk
from tkinter.ttk import Label

import backend as bkd
import utils.utiles as util
from app_main_window import App


# Creates margin_error_main_window when "Calculate margin of error" button is pressed
class MarginErrorWindow(App):

    logger = ""

    def __init__(self):

        # Root window for MarginErrorWindow
        self.new_window = tk.Tk()
        self.new_window.title("Calculate margin of error")
        self.new_window.geometry(self.GEOMETRY)
        self.new_window.configure(bg=self.BACKGROUND_COLOR)
        self.new_window.resizable(False, False)

        # Title
        self.title = util.get_text_label(self.new_window, text=self.text_ui["enter_values_sample"])
        self.title.place(x=125, y=50)

        # Creates a frame for labels and entries
        self.central_frame = tk.Frame(self.new_window, bg=self.BACKGROUND_COLOR)
        self.central_frame.pack(side="top", anchor="center", pady=110)

        # Asks for population size
        Label(self.central_frame, 
              text=self.text_ui["ask_population_size"], 
              font=("sans-serif", 14), 
              relief="raised", 
              padding=5).grid(row=0, column=1, padx=10, pady=5)
        self.input_population_size = tk.Entry(self.central_frame, 
                                         width=15, 
                                         font=("sans-serif", 12))
        self.input_population_size.grid(row=1, column=1, padx=10, pady=5)

        # Asks for confidence level
        Label(self.central_frame, 
              text=self.text_ui["ask_confidence"], 
              font=("sans-serif", 14), 
              relief="raised", 
              padding=5).grid(row=0, column=2, padx=10, pady=5)
        self.input_confidence_level = tk.Entry(self.central_frame, 
                                          width=17, 
                                          font=("sans-serif", 12))
        self.input_confidence_level.grid(row=1, column=2, padx=10, pady=5)

        # Asks for sample size
        Label(self.central_frame,
              text=self.text_ui["ask_sample_size"],
              font=("sans-serif", 14),
              relief="raised",
              padding=5).grid(row=0, column=3, padx=10, pady=5)
        self.input_sample_size = tk.Entry(self.central_frame,
                                          width=12,
                                          font=("sans-serif", 12))
        self.input_sample_size.grid(row=1, column=3, padx=10, pady=5)

        # Calculate button and returns margin of error
        self.calculate_button = util.get_button(self.new_window, self.text_ui["get_margin_error"], "blue", self.calculate_margin_error)
        self.calculate_button.place(x=175, y=200)

        # Logger, shows result from calculated margin of error
        self.label_border = tk.Frame(self.new_window, bg="#f0f0f0", relief="sunken", bd=2)
        self.label_text = tk.Label(self.label_border, font=("Consolas", 15), anchor="center", width=20, height=1, bg="#f0f0f0", fg="#131313")
        self.label_text.pack(fill="both", expand=True, padx=1, pady=1)
        self.label_border.pack(anchor="nw", padx=175)
        self.output("")


    # Calculates margin of error when pressing "calculate margin of error" button
    def calculate_margin_error(self):

        # Gets population
        tmp_population = self.input_population_size.get()
        population = bkd.ask_population_size(tmp_population)

        # Gets confidence level, calculates and returns z_score from a table
        tmp_confidence = self.input_confidence_level.get()
        confidence = bkd.ask_confidence(tmp_confidence)
        z_score = bkd.get_zscore(confidence)

        # Gets sample size
        tmp_sample_size = self.input_sample_size.get()
        sample_size = bkd.ask_sample_size(tmp_sample_size)

        # Gets result from sample size calculation
        result = bkd.calculate_margin_error(population, z_score, sample_size)

        # Updates logger with the result
        self.output(str(result))


    # Gets output for logger and applies configuration
    def output(self, message):
        self.label_text.config(text=message)