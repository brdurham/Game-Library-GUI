#!usr/bin/python3
#Brady Durham
#2/10/2020

'''GUI Version of Game Library Console App'''


import pickle

import tkinter as tk

from tkinter import messagebox

from tkinter.scrolledtext import ScrolledText

TITLE_FONT = ("Times New Roman", "24")
BUTTON_FONT = ("Arial", "15")


class Screen(tk.Frame):    
    current = 0
   
    def __init__(self):
        tk.Frame.__init__(self)
       
    def switch_frame():
        screens[Screen.current].tkraise()
'''Frame containing all the buttons that lead to the different functions'''
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Game Library",
                             font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Add", font = BUTTON_FONT,
                                 command = self.go_add)
        self.btn_add.grid(row = 1, column = 0, sticky = "news")
       
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT,
                                 command = self.go_edit)
        self.btn_edit.grid(row = 2, column = 0, sticky = "news")
       
        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT,
                                 command = self.go_search)
        self.btn_search.grid(row = 3, column = 0, sticky = "news")
       
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT,
                                 command = self.go_remove)
        self.btn_remove.grid(row = 4, column = 0, sticky = "news")
       
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT,
                                 command = self.go_save)
        self.btn_save.grid(row = 5, column = 0, sticky = "news")
       
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
   
    def go_add(self):
        Screen.current = 1
        Screen.switch_frame()
       
    def go_clear(self):              
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])        
   
       
     
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit_list = EditGame1(pop_up)
        frm_edit_list.grid(row = 0, column = 0)
   
    def go_search(self):
        Screen.current = 4
        Screen.switch_frame()
       
    def go_remove(self):
        pop_up = tk.Tk()
        pop_up.title("Remove")
        frm_edit_list = Remove(pop_up)
        frm_edit_list.grid(row = 0, column = 0)
   
    def go_save(self):
        data_file = open("game_lib.pickle", "wb")
        pickle.dump(games, data_file)
        data_file.close()
        print("Saved Successfully.")
        
        pop_up = tk.Tk()
        pop_up.title("Save")
        frm_edit_list = PopMessage(pop_up, "Saved Successfully.")
        frm_edit_list.grid(row = 0, column = 0)
             


'''entry boxes for all the things needed for a new game'''
class Add(Screen):
    def __init__(self):
        Screen.__init__(self)        
        self.lbl_title = tk.Label(self, text = "Add Game",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, columnspan = 4, sticky ="news")
       
        #Genre entrybox
        self.lbl_search_by = tk.Label(self, text = "Genre: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0, sticky ="news")        
        self.ent_genre = tk.Entry (self)
        self.ent_genre.grid(row = 1, column = 1)
        #Title entrybox
        self.lbl_search_by = tk.Label(self, text = "Title: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 2, column = 0, sticky ="news")        
        self.ent_title = tk.Entry (self)
        self.ent_title.grid(row = 2, column = 1)
        #Devoloper entrybox
        self.lbl_search_by = tk.Label(self, text = "Devoloper: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 0, sticky ="news")        
        self.ent_devoloper = tk.Entry (self)
        self.ent_devoloper.grid(row = 3, column = 1)  
        #Publisher entrybox
        self.lbl_search_by = tk.Label(self, text = "Publisher: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 4, column = 0, sticky ="news")        
        self.ent_publisher = tk.Entry (self)
        self.ent_publisher.grid(row = 4, column = 1)  
        #Year entrybox
        self.lbl_search_by = tk.Label(self, text = "Year: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 5, column = 0, sticky ="news")        
        self.ent_year = tk.Entry (self)
        self.ent_year.grid(row = 5, column = 1)
       
        self.lbl_search_by = tk.Label(self, text = "Release Year: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 2, sticky ="news")        
        self.ent_release_year = tk.Entry (self)
        self.ent_release_year.grid(row = 1, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Rating: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 2, column = 2, sticky ="news")        
        self.ent_rating = tk.Entry (self)
        self.ent_rating.grid(row = 2, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Single/Multiplayer: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 2, sticky ="news")        
        self.ent_single_multi = tk.Entry (self)
        self.ent_single_multi.grid(row = 3, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Price: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 4, column = 2, sticky ="news")        
        self.ent_price = tk.Entry (self)
        self.ent_price.grid(row = 4, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Played it?: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 5, column = 2, sticky ="news")        
        self.ent_played = tk.Entry (self)
        self.ent_played.grid(row = 5, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Purchase Date: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 6, column = 0, sticky ="news")        
        self.ent_purchase_date = tk.Entry (self)
        self.ent_purchase_date.grid(row = 6, column = 1)        
       
        #Notes Scrolled text box
        self.lbl_search_by = tk.Label(self, text = "Notes: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 7, column = 0, sticky ="news")                
        self.notes = ScrolledText(self, height = 8, width = 40)
        self.notes.grid(row = 8, columnspan = 3)
        #Cancel Reset Remove Buttons
        self.btn_add = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                 command = self.go_main)
        self.btn_add.grid(row = 9, column = 0, sticky ="news")
        self.btn_add = tk.Button(self, text = "Reset", font = BUTTON_FONT,
                                 command = self.go_clear)
        self.btn_add.grid(row = 9, column = 1, sticky ="news")
        self.btn_add = tk.Button(self, text = "Confirm", font = BUTTON_FONT)
        self.btn_add.grid(row = 9, column = 2, sticky ="news")        
       
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
        self.grid_columnconfigure(5, weight = 1)
        self.grid_columnconfigure(6, weight = 1)
        self.grid_columnconfigure(7, weight = 1)
        self.grid_columnconfigure(8, weight = 1)
        self.grid_columnconfigure(9, weight = 1)
        self.grid_columnconfigure(10, weight = 1)
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        #messagebox.showinfo(message = "Entry has been added.")


    def go_clear(self):              
         
        self.ent_genre.delete(0, "end")
        self.ent_title.delete(0, "end")
        self.ent_devoloper.delete(0, "end")
        self.ent_publisher.delete(0, "end")
       
        self.ent_year.delete(0, "end")
        self.ent_release_year.delete(0, "end")        
        self.ent_rating.delete(0, "end")
        self.ent_single_multi.delete(0, "end")
        self.ent_price.delete(0, "end")
        self.ent_played.delete(0, "end")
        self.ent_purchase_date.delete(0, "end")
        self.ent_notes.delete(0, "end")

'''a dropdown menu to select which game you would like to edit'''
class EditGame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
       
        def confirm_edit(self):
            entry = []
            entry.append(self.ent_genre.get())
            entry.append(self.ent_title.get())
            entry.append(self.ent_developer.get())
            entry.append(self.ent_publisher.get())
            entry.append(self.ent_platform.get())
            entry.append(self.ent_release_year.get())
            entry.append(self.ent_rating.get())
            entry.append(self.ent_single_multi.get())
            entry.append(self.ent_price.get())
            entry.append(self.ent_played.get())
            entry.append(self.ent_purchase_date.get())

            entry.append(self.scr_notes.get(0.0, "end"))
            games[self.edit_key] = entry
       
        self.lbl_remove = tk.Label(self, text = "Which Game do You Want to Edit",
                                 font = BUTTON_FONT)
        self.lbl_remove.grid(row = 0, columnspan = 2,
                                sticky = "news")
       
        self.options = ["Select a Title"]
        for key in games.keys():
            self.options.append(games[key][1])
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *self.options)
        self.menu.grid(row = 1, columnspan = 2,
                       sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 2, column = 0,
                          sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Ok", font = BUTTON_FONT,
                                command = self.go_edit_two)
        self.btn_ok.grid(row = 2, column = 1,
                          sticky = "news")
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        self.parent.destroy()
       
    def go_edit_two(self):
       
        if self.tkvar.get() == self.options[0]:
            popup = tk.Tk()
            popup.title("Select A Title")
            msg="ERROR, select a title"
            frm_error = PopMessage(popup, "Select A Title")
            frm_error.grid(row=0, column=0)
            
        else:
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    screens[2].edit_key = i
                    break
            Screen.current = 2
            screens[Screen.current].update()
            Screen.switch_frame()
            self.parent.destroy()
           




'''entry boxes for all of the diferent things needed to know about a new game'''
class EditTwo(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.edit_key = 0
   
       
       
        self.lbl_title = tk.Label(self, text = "Edit Game",  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, columnspan = 4, sticky ="news")
        #Genre entrybox
        self.lbl_search_by = tk.Label(self, text = "Genre: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0, sticky ="news")        
        self.ent_genre = tk.Entry (self)
        self.ent_genre.grid(row = 1, column = 1)
        #Title entrybox
        self.lbl_search_by = tk.Label(self, text = "Title: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 2, column = 0, sticky ="news")        
        self.ent_title = tk.Entry (self)
        self.ent_title.grid(row = 2, column = 1)
        #Decoloper entrybox
        self.lbl_search_by = tk.Label(self, text = "Devoloper: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 0, sticky ="news")        
        self.ent_developer = tk.Entry (self)
        self.ent_developer.grid(row = 3, column = 1)  
        #Publisher entrybox
        self.lbl_search_by = tk.Label(self, text = "Publisher: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 4, column = 0, sticky ="news")        
        self.ent_publisher = tk.Entry (self)
        self.ent_publisher.grid(row = 4, column = 1)  
        #Year entrybox
        self.lbl_search_by = tk.Label(self, text = "Platform: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 5, column = 0, sticky ="news")        
        self.ent_platform = tk.Entry (self)
        self.ent_platform.grid(row = 5, column = 1)
       
        self.lbl_search_by = tk.Label(self, text = "Release Year: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 2, sticky ="news")        
        self.ent_release_year = tk.Entry (self)
        self.ent_release_year.grid(row = 1, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Rating: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 2, column = 2, sticky ="news")        
        self.ent_rating = tk.Entry (self)
        self.ent_rating.grid(row = 2, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Single/Multiplayer: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 3, column = 2, sticky ="news")        
        self.ent_single_multi = tk.Entry (self)
        self.ent_single_multi.grid(row = 3, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Price: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 4, column = 2, sticky ="news")        
        self.ent_price = tk.Entry (self)
        self.ent_price.grid(row = 4, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Played it?: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 5, column = 2, sticky ="news")        
        self.ent_played = tk.Entry (self)
        self.ent_played.grid(row = 5, column = 3)
       
        self.lbl_search_by = tk.Label(self, text = "Purchase Date: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 6, column = 0, sticky ="news")        
        self.ent_purchase_date = tk.Entry (self)
        self.ent_purchase_date.grid(row = 6, column = 1)        
       
        #Notes Scrolled text box
        self.lbl_search_by = tk.Label(self, text = "Notes: ", font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 7, column = 0, sticky ="news")                
        self.results = ScrolledText(self, height = 8, width = 40)
        self.results.grid(row = 8, columnspan = 3)
       
        #Cancel Reset Remove Buttons
        self.btn_add = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                 command = self.go_edit)
        self.btn_add.grid(row = 9, column = 0, sticky ="news")
        self.btn_add = tk.Button(self, text = "Reset", font = BUTTON_FONT,
                                 command = self.reset)
        self.btn_add.grid(row = 9, column = 1, sticky ="news")
        self.btn_add = tk.Button(self, text = "Confirm", font = BUTTON_FONT,
                                 command = self.confirm)
        self.btn_add.grid(row = 9, column = 2, sticky ="news")        
       
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
        self.grid_columnconfigure(5, weight = 1)
        self.grid_columnconfigure(6, weight = 1)
        self.grid_columnconfigure(7, weight = 1)
        self.grid_columnconfigure(8, weight = 1)
        self.grid_columnconfigure(9, weight = 1)
        self.grid_columnconfigure(10, weight = 1)


    def update(self):
        entry = games[self.edit_key]
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])
        self.ent_title.delete(0, "end")
        self.ent_title.insert(0, entry[1])
        self.ent_developer.delete(0, "end")
        self.ent_developer.insert(0, entry[2])
        self.ent_publisher.delete(0, "end")
        self.ent_publisher.insert(0, entry[3])
        self.ent_platform.delete(0, "end")
        self.ent_platform.insert(0, entry[4])
        self.ent_purchase_date.delete(0, "end")
        self.ent_purchase_date.insert(0, entry[5])
        self.ent_release_year.delete(0, "end")
        self.ent_release_year.insert(0, entry[6])
        self.ent_rating.delete(0, "end")
        self.ent_rating.insert(0, entry[7])    
        self.ent_single_multi.delete(0, "end")
        self.ent_single_multi.insert(0, entry[8])
        self.ent_price.delete(0, "end")
        self.ent_price.insert(0, entry[9])
        self.ent_played.delete(0, "end")
        self.ent_played.insert(0, entry[10])          
        
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit_list = EditGame1(pop_up)
        frm_edit_list.grid(row = 0, column = 0)    
        
    def reset(self):
        self.update()
        
    def confirm(self):
        Screen.current = 0
        Screen.switch_frame()        
  		        
        


'''Sub-frame containing all the checkboxes with the different search parameters'''
class SearchParameters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
       
        self.genre_var = tk.BooleanVar(self)
        self.genre_var.set(True)
        self.chk_genre = tk.Checkbutton(self, text = "Genre" , var = self.genre_var)
        self.chk_genre.grid(row = 0, column = 0, sticky = "nws")
       
        self.title_var = tk.BooleanVar(self)
        self.title_var.set(True)
        self.chk_title = tk.Checkbutton(self, text = "Title", var = self.title_var)
        self.chk_title.grid(row = 1, column = 0, sticky = "nws")
               
   
        self.developer_var = tk.BooleanVar(self)
        self.developer_var.set(True)          
        self.chk_developer = tk.Checkbutton(self, text = "Developer", var = self.developer_var)
        self.chk_developer.grid(row = 2, column = 0, sticky = "nws")
       
        self.publisher_var = tk.BooleanVar(self)
        self.publisher_var.set(True)
        self.chk_publisher = tk.Checkbutton(self, text = "Publisher", var = self.publisher_var)
        self.chk_publisher.grid(row = 3, column = 0, sticky = "nws")
                 
       
        self.platform_var = tk.BooleanVar(self)
        self.platform_var.set(True)
        self.chk_platform = tk.Checkbutton(self, text = "Platform", var = self.platform_var)
        self.chk_platform.grid(row = 4, column = 0, sticky = "nws")
               
       
        self.release_year_var = tk.BooleanVar(self)
        self.release_year_var.set(True)        
        self.chk_release_year = tk.Checkbutton(self, text = "Release Year", var = self.release_year_var)
        self.chk_release_year.grid(row = 0, column = 1, sticky = "nws")
       
        self.rating_var = tk.BooleanVar(self)
        self.rating_var.set(True)
        self.chk_rating = tk.Checkbutton(self, text = "Rating", var = self.rating_var)
        self.chk_rating.grid(row = 1, column = 1, sticky = "nws")
                 
       
        self.single_multi_var = tk.BooleanVar(self)
        self.single_multi_var.set(True)  
        self.chk_single_multi = tk.Checkbutton(self, text = "Single/Multi", var = self.single_multi_var)
        self.chk_single_multi.grid(row = 2, column = 1, sticky = "nws")
               
       
        self.price_var = tk.BooleanVar(self)
        self.price_var.set(True)
        self.chk_price = tk.Checkbutton(self, text = "Price", var = self.price_var)
        self.chk_price.grid(row = 3, column = 1, sticky = "nws")
                 
       
        self.played_var = tk.BooleanVar(self)
        self.played_var.set(True)  
        self.chk_played = tk.Checkbutton(self, text = "Played?", var = self.played_var)
        self.chk_played.grid(row = 4, column = 1, sticky = "nws")
                       
       
        self.purchase_date_var = tk.BooleanVar(self)
        self.purchase_date_var.set(True)
        self.chk_purchase_date = tk.Checkbutton(self, text = "Purchase Date", var = self.purchase_date_var)
        self.chk_purchase_date.grid(row = 0, column = 2, sticky = "nws")
                       
       
        self.notes_var = tk.BooleanVar(self)
        self.notes_var.set(True)  
        self.chk_notes = tk.Checkbutton(self, text = "Notes", var = self.notes_var)
        self.chk_notes.grid(row = 1, column = 2, sticky = "nws")
               
   
       
       
       
       
       
               
       

'''contains all of the diferent search parameters and an entry box to search for a game'''
class SearchGame(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "SEARCH",
                             font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0,
                            sticky = "news")
        self.lbl_search_by = tk.Label(self, text = "Search By",
                             font = BUTTON_FONT)
        self.lbl_search_by.grid(row = 1, column = 0,
                            sticky = "news") 
        self.options = [
                  "Select Option",
                  "Genre",
                  "Title",
                  "Company",
                  "Publisher",
                  "Console",
                  "Release Year",
                  "Rating",
                  "Multi/Single player",
                  "Price",
                  "Beaten",
                  "Date Purchase"
              ]
        self.tkvar_search_by = tk.StringVar(self)
        self.tkvar_search_by.set(self.options[0])
              
        self.dbx_search_by = tk.OptionMenu(self,self.tkvar_search_by,*self.options)
        self.dbx_search_by.grid(row=2,column=0,sticky="new")          
       
        options = ["Genre", "Title", "Publisher", "Developer", "Platform", "Release Year",
                   "Rating", "Single/Multiplayer", "Price", "Played?", "Purchase Date"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *options)
        self.menu.grid(row = 2, column = 3)                
       
        self.lbl_search_for = tk.Label(self, text = "Search For",
                             font = BUTTON_FONT)
        self.lbl_search_for.grid(row = 3, column = 0,
                            sticky = "news")        
        self.entry = tk.Entry(self)
        self.entry.grid(row = 4, column = 0,
                        sticky = "news")        
       
        self.results = ScrolledText(self, height = '8', width = '40')
        self.results.grid(row = 5, columnspan = 3,
                          sticky = "news")
       
        self.frm_search_parameters = SearchParameters(self)
        self.frm_search_parameters.grid(row = 1, column = 3, columnspan = 3, rowspan = 4,
                                        sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Back", font = BUTTON_FONT,
                                 command = self.go_main)
        self.btn_add.grid(row = 6, column = 0,
                          sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Clear", font = BUTTON_FONT,
                                 command = self.clear)
        self.btn_add.grid(row = 6, column = 1,
                          sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Submit", font = BUTTON_FONT,
                                 command = self.submit_search)
        self.btn_add.grid(row = 6, column = 2,
                          sticky = "news")
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)      
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def clear(self):
        self.frm_search_parameters.genre_var.set(False)
        self.frm_search_parameters.title_var.set(False)
        self.frm_search_parameters.developer_var.set(False)
        self.frm_search_parameters.publisher_var.set(False)
        self.frm_search_parameters.platform_var.set(False)
        self.frm_search_parameters.release_year_var.set(False)
        self.frm_search_parameters.rating_var.set(False)
        self.frm_search_parameters.single_multi_var.set(False)
        self.frm_search_parameters.price_var.set(False)
        self.frm_search_parameters.played_var.set(False)
        self.frm_search_parameters.purchase_date_var.set(False)
        self.frm_search_parameters.notes_var.set(False)
        self.results.delete(0.0, "end")
        
        
    def submit_search(self):
        '''self.scr_results.delete(0.0, "end")
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)'''
        self.filter_print()
            
    
             
    def filter_print(self, entry):
        if self.frm_search_parameters.genre_var.get() == True:
            msg = entry[0] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.title_var.get() == True:
            msg = entry[1] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.developer_var.get() == True:
            msg = entry[2] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.publisher_var.get() == True:
            msg = entry[3] + "\n"
            self.results.insert("insert", msg)        
           
        if self.frm_search_parameters.platform_var.get() == True:
            msg = entry[4] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.release_year_var.get() == True:
            msg = entry[5] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.rating_var.get() == True:
            msg = entry[6] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.single_multi_var.get() == True:
            msg = entry[7] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.price_var.get() == True:
            msg = entry[8] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.played_var.get() == True:
            msg = entry[9] + "\n"
            self.results.insert("insert", msg)
           
        if self.frm_search_parameters.purchase_date_var.get() == True:
            msg = entry[10] + "\n"
            self.results.insert("insert", msg)
       
        if self.frm_search_parameters.notes_var.get() == True:
            msg = entry[11] + "\n"
            self.results.insert("insert", msg)    
                           
        msg = " **************************************\n"
        self.results.insert("insert", msg)
        
        
    def print_search(self):
        self.scr_results.delete(0.0, "end")
        keyword = self.ent_search_for.get()
        for key in games.keys():
            entry = games[key]
            if self.search_by_var == self.options[0]:
                entry = games[key]
                self.filter_print(entry)
                
            if self.search_by_var.get() == self.options[1]:
                if keyword in entry[0]:
                    self.filter_print(entry)
            

'''class Save(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)    
        self.lbl_file_saved = tk.Label(self, text = "File Saved",
                                 font = BUTTON_FONT)
        self.lbl_file_saved.grid(row = 0, column = 0,
                                sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Ok", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 1, column = 0,
                          sticky = "news")
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()    '''


'''Contains a dropdown menu to select which game you would like to remove'''
class Remove(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.lbl_remove = tk.Label(self, text = "Which Game do You Want to Remove",
                                 font = BUTTON_FONT)
        self.lbl_remove.grid(row = 0, columnspan = 2,
                                sticky = "news")
       
        options = ["Halo3", "Halo2", "GTA 5"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *options)
        self.menu.grid(row = 1, columnspan = 2,
                       sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Cancel", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 2, column = 0,
                          sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Remove", font = BUTTON_FONT,
                                command = self.go_remove_two)
        self.btn_ok.grid(row = 2, column = 1,
                          sticky = "news")
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        self.parent.destroy()
       
    def go_remove_two(self):
        Screen.current = 3
        Screen.switch_frame()    
        self.parent.destroy()
       
       

'''Lists all of the games marked for removal'''
class RemoveTwo(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_remove = tk.Label(self, text = "These Games are Marked for Removal",
                                 font = BUTTON_FONT)
        self.lbl_remove.grid(row = 0, columnspan = 3,
                                sticky = "news")
       
        self.results = ScrolledText(self, height = '8', width = '40')
        self.results.grid(row = 6, columnspan = 3,
                          sticky = "news")
       
        self.btn_ok = tk.Button(self, text = "Main Menu", font = BUTTON_FONT,
                                command = self.go_main)
        self.btn_ok.grid(row = 7, column = 0,
                          sticky = "news")
       
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame() 
        
        
        
class PopMessage(tk.Frame):
        def __init__(self, parent, msg= "generic"):
            tk.Frame.__init__(self, master = parent)
            self.parent = parent
            
            self.lbl_continue = tk.Label(self, text = msg)
            self.lbl_continue.grid(row=0, column=0, columnspan=3)
            
            self.btn_ok = tk.Button(self, text = "OK", command = self.parent.destroy)
            self.btn_ok.grid(row=1, column=1, columnspan=1)
            

'''class OptFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        options = ["One", "Two", "Three", "Four", "Five", "Six"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, self.tkvar, *options)
        self.menu.grid(row = 0, column = 0)'''



   



'''Parent frame of all the other frames'''



##MAIN

if __name__ == "__main__":
    data_file = open("game_lib.pickle", "rb")
    games = pickle.load(data_file)
    data_file.close()
   
    root = tk.Tk()
    root.title("Game_Lib")
    root.geometry("700x500")
    screens = [MainMenu(), Add(), EditTwo(), RemoveTwo(),
                SearchGame()]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
   
    screens[0].tkraise()
    '''main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0,
                   sticky = "news")
   
    add_game = Add()
    add_game.grid(row = 0, column = 0,
                   sticky = "news")
       
    edit_game_1 = EditGame1()
    edit_game_1.grid(row = 0, column = 0,
                   sticky = "news")
       
    edit_two = EditTwo()
    edit_two.grid(row = 0, column = 0,
                   sticky = "news")
   
    remove_game = Remove()
    remove_game.grid(row = 0, column = 0,
                   sticky = "news")
   
    remove_two = RemoveTwo()
    remove_two.grid(row = 0, column = 0,
                   sticky = "news")
   
    save = Save()
    save.grid(row = 0, column = 0,
                   sticky = "news")
   
    search_game = SearchGame()
    search_game.grid(row = 0, column = 0,
                   sticky = "news")
   
    screen = Screen()
    screen.grid(row = 0, column = 0,
                   sticky = "news")
   
    add_game.tkraise()'''
    root.grid_columnconfigure(0, weight = 1)
    

    root.mainloop()