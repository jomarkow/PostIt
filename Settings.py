import tkinter as tk
import random as rd
from tkinter.colorchooser import askcolor

font = "Arial"

class Settings:
    
    def __init__(self):
        
        self.color = "#FFFFFF" # White default
        
        self.width = 250
        self.eight = 250
        self.MIN_WIDTH = 100
        self.MIN_HEIGHT = 100
        self.MAX_WIDTH = 1000
        self.MAX_HEIGHT = 1000
                
    def set_widht(self, value):
        
        if value < self.MIN_WIDTH or value > self.MAX_WIDTH: 
            title = "Limits exceded"
            message = f"Set a width greater than {self.MIN_WIDTH} and smaller than {self.MAX_WIDTH}"
            tk.messagebox.showwarning(title= title, message=message)
            
        else: self.width = value
        
    def set_eight(self, value):

        if value < self.MIN_HEIGHT or value > self.MAX_HEIGHT: 
            title = "Limits exceded"
            message = f"Set a eight greater than {self.MIN_HEIGHT} and smaller than {self.MAX_HEIGHT}"
            tk.messagebox.showwarning(title= title, message=message)
            
        else: self.height = value      
        
    def select_color(self):
        
        self.color = askcolor(title="Post It Color Chooser")[1]

    def random_color(self):
        
        self.color = ["#"+''.join([rd.choice('0123456789ABCDEF') for i in range(6)])]

