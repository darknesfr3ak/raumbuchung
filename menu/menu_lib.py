import keyboard
import os
from time import sleep 

# Kein gutes Menü aber ist ok
# Ja hätte eig tkinter nutzen können aber naja egallll x_x

class TerminalMenu:
    def __init__(self, menu_entries, menu_index, menu_tab, continue_ = True): # Konstruktor halt ;-;
        self.setmenu_entries(menu_entries)
        self.setmenu_index(menu_index)
        self.setmenu_tab(menu_tab)
        self.setContinue_(continue_)


    def register_event(self, event): # Event für Aktionen, Kommunikation mit Main.py um Aktionen zu verwalten
        self.event = event

    def trigger_event(self, event): # Trigger Event
        if self.event is not None:
            self.event(event)



    # Setter

    def setmenu_entries(self, menu_entries):
        self.menu_entries = menu_entries

    def setmenu_index(self, menu_index):
        self.menu_index = menu_index

    def setmenu_tab(self, menu_tab):
        self.menu_tab = menu_tab

    def setContinue_(self, continue_): # Aktivieren/Deaktivieren von Keyboard Input, je nach Status im Menü
        if continue_ == False:
            keyboard.unhook_key("up")
            keyboard.unhook_key("down")
            keyboard.unhook_key("enter")
            keyboard.unhook_key("backspace")
        else:
            keyboard.on_press_key("up", self.up_arrow_event)
            keyboard.on_press_key("down", self.down_arrow_event)
            keyboard.on_press_key("enter", self.enter_event)
            keyboard.on_press_key("backspace", self.backspace_event)
        self.continue_ = continue_

    # Getter

    def getmenu_entries(self):
        return self.menu_entries
    
    def getmenu_index(self):
        return self.menu_index

    def getmenu_tab(self):
        return self.menu_tab
    
    def getContinue_(self):
        return self.continue_

    # Funktionen

    def updateConsole(self): # Aktualisieren des Menüs
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, v in enumerate(self.getmenu_entries()): # -> [], [] | Mehrere Listen bzw Tabs für Menü
            if i == self.getmenu_tab(): # Aktuelle Liste bzw Tab
                for i2, v2 in enumerate(v):
                    if i2 == 0: # Title + Description
                        print(f"== {v2[0]} ==")
                        print(f"= {v2[1]}")
                    else:
                        if i2 == self.getmenu_index(): # Selected Button
                            print("-> " + v2[0])
                        else: # Other Buttons
                            print("   " + v2[0])

    def up_arrow_event(self, e): # Event for Keyboard Input (Up Arrow)
        if self.getContinue_() == True:
            self.setmenu_index(self.getmenu_index() - 1) # Go to previous menu index
            if self.getmenu_index() < 1: # If is first menu index
                self.setmenu_index(len(self.getmenu_entries()[self.getmenu_tab()]) - 1)
            self.updateConsole()

    def down_arrow_event(self, e): # Event for Keyboard Input (Down Arrow)
        if self.getContinue_() == True:
            self.setmenu_index(self.getmenu_index() + 1) # Go to next menu index
            if self.getmenu_index() > len(self.getmenu_entries()[self.getmenu_tab()]) - 1: # If is last menu index
                self.setmenu_index(1)
            self.updateConsole()

    def enter_event(self, e): # Event for Keyboard Input (Enter)
        if self.getContinue_() == True:
            if self.getmenu_entries()[self.getmenu_tab()][self.getmenu_index()][1] < 0: # If is Action Key
                self.trigger_event(self.getmenu_entries()[self.getmenu_tab()][self.getmenu_index()][1]) # Trigger Event Action Key
            else:
                self.setmenu_tab(self.getmenu_entries()[self.getmenu_tab()][self.getmenu_index()][1]) # Go to next menu tab
                self.setmenu_index(1)
                self.updateConsole()
        

    def backspace_event(self, e): # Event for Keyboard Input (Backspace)
        if self.getContinue_() == True:
            self.setmenu_tab(self.getmenu_entries()[self.getmenu_tab()][self.getmenu_index()][2]) # Back to previous menu tab
            self.setmenu_index(1)
            self.updateConsole()


    def setupMenu(self): # Setup Menu
        self.updateConsole()
        #keyboard.on_press_key("up", self.up_arrow_event)
        #keyboard.on_press_key("down", self.down_arrow_event)
        #keyboard.on_press_key("enter", self.enter_event)
        #keyboard.on_press_key("backspace", self.backspace_event)
        while True: # Loop um Menü Interaktion zu ermöglichen
            sleep(0.01)

