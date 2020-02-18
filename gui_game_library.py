#!usr/bin/python3
#Brady Durham
#2/10/2020

'''GUI Version of Game Library Console App'''

import pickle

import tkinter as tk

from tkinter.scrolledtext import ScrolledText


TITLE_FONT = ("Times New Roman", 24)

BUTTON_FONT = ("Arial", 15)

#Main Section
#if __name__ == "__main__":
        #datafile = open("game_lib.pickle", "rb")
        #games = pickle.load(datafile)
        #datafile.close()
        
#Main Menu 
#.
#.
#.
#screens = [MainMenu(), Search()]
#screens[0].grid(row = 0, column = 0, sticky = "news")
#.
#.
#.
#screens[2].tkraise()

 
        
class Screen(tk.Frame):  
  current = 0
  def __init__(self):
    tk.Frame.__init__(self)
    
class MainMenu(Screen):
  def __init__(self):
    Screen.__init__(self)
    
class Search(Screen):
  def __init__(self):
    Screen.__init_(self)
    
    self.lbl_search = tk.Label(text = "Search ", font = BUTTON_FONT)
    self.lbl_search.grid(row = 0, column = 1)
                         
    self.lbl_search_by = tk.Label(text = "Search By: ", font = BUTTON_FONT)
    self.lbl_search_by.grid(row = 2, column = 1)
    search_entry = tk.Entry()
    search_entry.grid(row = 2, column = 2)
    
    scroll_width=40  
    scroll_height=8  
    #scr=ScrolledText.ScrolledText(self, width=scroll_width, height=scroll_height)  
    #scr.grid(column=0, columnspan=3)                
    
    self.lbl_search_for = tk.Label(text = "Search For: ", font = BUTTON_FONT)
    self.lbl_search_for.grid(row = 1, column = 1)
    search_entry = tk.Entry()
    search_entry.grid(row = 1, column = 2)  
    
    
    
class Add(Screen):
  def __init__(self):
    Screen.__init_(self)
    
    self.lbl_add = tk.Label(text = "Add Game", font = TITLE_FONT)
    self.lbl_add.grid(row = 2, column = 2, sticky = "news")
    
    self.lbl_add_specifics = tk.Label(text = "Game Information", font = BUTTON_FONT)
    self.lbl_add_specifics.grid(row = 1, column = 1)
    
    Add.tkraise()
  
  
        
      
#class MainMenu(tk.Frame):
        #def __init__(self):
                #tk.Frame.__init__(self)
                #self.lbl_title = tk.Label(text = "Game Library", font = TITLE_FONT)
                #self.lbl_title.grid(row = 0, column = 0, sticky = "news")
                
                #self.button_add = tk.Button(text = "Add", font = BUTTON_FONT)
                #self.button_add.grid(row = 1, column = 0)
                
                        
class Search(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)
                self.lbl_search = tk.Label(text = "Search ", font = BUTTON_FONT)
                self.lbl_search.grid(row = 0, column = 1)
                                     
                self.lbl_search_by = tk.Label(text = "Search By: ", font = BUTTON_FONT)
                self.lbl_search_by.grid(row = 2, column = 1)
                search_entry = tk.Entry()
                search_entry.grid(row = 2, column = 2)
                
                scroll_width=40  
                scroll_height=8  
                #scr=ScrolledText.ScrolledText(self, width=scroll_width, height=scroll_height)  
                #scr.grid(column=0, columnspan=3)                
                
                self.lbl_search_for = tk.Label(text = "Search For: ", font = BUTTON_FONT)
                self.lbl_search_for.grid(row = 1, column = 1)
                search_entry = tk.Entry()
                search_entry.grid(row = 1, column = 2)
                

class Add(tk.Frame):
        def __init__(self):
            tk.Frame.__init__(self)
            self.lbl_add = tk.Label(text = "Add Game", font = TITLE_FONT)
            self.lbl_add.grid(row = 2, column = 2, sticky = "news")
            
            self.lbl_add_specifics = tk.Label(text = "Game Information", font = BUTTON_FONT)
            self.lbl_add_specifics.grid(row = 1, column = 1)
            
            
            
  
                
class OptFrame(tk.Frame):
        def __init__(self):
                tk.Frame.__init__(self)
                options = ["one", "two"]
                tk_var = tk.StringVar(self)
                self.tk_var = tk.StringVar(self)
                tk_var.set("options")
                self.menu = tk.OptionMenu(self, self.tk_var, *options)
                self.menu.grid(row = 0, column = 0)
                                
                
      
                
        
root = tk.Tk()
root.title("Game Library")
root.geometry("500x500")
#main_menu = MainMenu()
search = Search()
optmenu = OptFrame()
add = Add()

        
        


root.mainloop()
        


