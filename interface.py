from tkinter import *

class GUI:
    def __init__(self):

        # Main window
        self.App = Tk()
        self.App.title = "Weather App"
        self.App.geometry('500x500')

        # Search bar to search by city
        self.search_bar = Text(self.App, width = 15, height = 1)
        self.search_bar.place(x = 200, y = 25)

        # Search button hit to retrieve weather information
        self.search_button = Button(self.App, text = "Search",width = 15//2, height = 1)
        self.search_button.place(x = 215 + 30//2, y = 55)

        # Text label that displays the current location
        self.location_label = Label(self.App, width = 10, height = 1)
        self.location_label.place(x = 150, y = 85)
        self.location_label.config(font=("Helvetica", 26))
        
        self.App.resizable(False, False)
        #self.App.mainloop()
    
    def set_location(self, text):
        self.location_label['text'] = text