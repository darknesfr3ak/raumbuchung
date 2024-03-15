"""
Bedienungsanleitung:
- [UP&Down Arrow] um sich im Menü zu bewegen
- [Enter] um eine Aktion/Button/Tab auszuführen
- [Backspace] um zurück zu gehen

Menü hat Bugs:
- Nach jeder Aktion bitte Script neu ausführen :P
  - Hierfür Safe Mode (Safety) eingeführt, auf False setzen um Bug zu sehen

Menü hätte man auch mit tkinter machen können, aber naja x_x
Spaß im Leben muss ja sein :P

Bidde Datenbank mit angeführter SQL aufsetzen dangeee c:
"""


# Imports
from sql import *
from classes.room import Room
import os
import keyboard
from time import sleep
import datetime

from menu.menu_lib import TerminalMenu

# Database (Test)

#import mysql.connector ## MySQL <3

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="",
#  database = "raumbuchung"
#)

Debug = True
Safety = True
global Zeiten
Zeiten = ["08:00 - 08:30", "08:30 - 09:00", "09:00 - 09:30", "09:30 - 10:00"]

# Stuff

# SQLite Test
"""
for i,v in enumerate(get_Worker()):
  print(f"{i+1}. {v[1]} {v[2]}")	

RoomList = []

def select_rooms():
  for i,v in enumerate(get_Room()):
    OG = v[1].split("_")[0]
    number_1 = v[1].split("_")[1]
    number_2 = v[1].split("_")[2]
    RoomList.append(Room(v[1], OG, number_1, number_2))
    
  for i,v in enumerate(RoomList):
    print(f"{i+1}. {v.getOG()} {v.getNumber_1()} {v.getNumber_2()}")

select_rooms()

for i,v in enumerate(get_Booking()):
  print(f"{i+1}. {v[1]} {v[2]} {v[3]}")
"""
  

# Menu
  
# SetUpMenu
# [ = Tab, ["Title", "Beschreibung"] ["Button", GoToTab/Action >0 (Seite/Tab) <0(Aktion), GoBackToTab (Wenn Backspace gedrückt wird, zu welchem Tab zurück gegangen wird)] ]
Menu = TerminalMenu(
  [
  [["HAUPTMENÜ","Mach was auch immer du zu tun hast arbeit oder so frag mich nicht ,_,"],["Verwaltung", 1, 0], ["Aktueller Tag", 5, 0], ["Exit", -999, 0]],
  [["Verwaltung",":D"], ["Mitarbeiter Verwalten", 2, 0], ["Räume Verwalten", 3, 0], ["Buchungen Verwalten", 4, 0]],
  [["Mitarbeiter",":D"], ["Mitarbeiter Hinzufügen", -301, 1], ["Mitarbeiter Löschen", -302, 1], ["Mitarbeiter Anzeigen", -303, 1]],
  [["Räume",":D"], ["Raum Hinzufügen", -401, 1], ["Raum Löschen", -402, 1], ["Räume Anzeigen", -403, 1]],
  [["Buchung",":D"], ["Buchung Hinzufügen", -501, 1], ["Buchung Löschen", -502, 1], ["Alle Buchungen Anzeigen", -503, 1]],
  [["Akuteller Tag","Siehe Wichtiges für den akutellen Tag ein"], ["Buchungen ansehen", -701, 0]]
  ], 
  1, # Start Menu Index
  0 # Start Menu Tab
  )

def GetDate(): # Akutelles Datum auf kompliziertere Art und Weise
  now = datetime.datetime.now()
  split_ = str(now).split("-")
  splitday = split_[2].split(" ")
  splitrest = splitday[1].split(":")
  splitsec = splitrest[2].split(".")
  newdate = []
  newdate.append(int(split_[0]))
  newdate.append(int(split_[1]))
  newdate.append(int(splitday[0]))
  newdate.append(int(splitrest[0]))
  newdate.append(int(splitrest[1]))
  newdate.append(int(splitsec[0]))
  finisheddate = str(newdate[0])+"."+str(newdate[1])+"."+str(newdate[2])
  return finisheddate

def UpdateConsole(message): # Update Console -> Zeit Vertreiben und Menu "Aktualisieren"
  for i in range(3):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(message)
    print("\n")
    print("Opening Menu" + "." * i)
    sleep(0.25)

  Menu.updateConsole()
  sleep(0.1)
  Menu.setContinue_(True)
  if Safety == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Exiting Menu for Safety \n Please restart the script to use the menu again")
    exit()

def GetMenuAction(ActionKey): # Alle Aktionen Verwalten
  if Debug == True:
    print(ActionKey) # Key der Aktion (Auslesbar vom Menu unten)
  
  Menu.setContinue_(False)
  Menu.setmenu_tab(Menu.getmenu_entries()[Menu.getmenu_tab()][Menu.getmenu_index()][2])
  Menu.setmenu_index(1)

  if ActionKey == -999: # Exit
    print("Program exited")
    exit()
  elif ActionKey == -301: # Mitarbeiter Hinzufügen
    os.system('cls' if os.name == 'nt' else 'clear')
    firstname = input("Vorname: ")
    lastname = input("Nachname: ")
    success = add_Worker(firstname, lastname) # SQL
    if success == True:
      UpdateConsole("Mitarbeiter hinzugefügt")
    else:
      UpdateConsole("Mitarbeiter konnte nicht hinzugefügt werden")
  elif ActionKey == -302: # Mitarbeiter Löschen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,v in enumerate(get_Worker()):
      print(f"ID: {v[0]} {v[1]} {v[2]}")
    print("\n")
    id = input("ID: ")
    success = remove_Worker(id) # SQL
    if success == True:
      UpdateConsole("Mitarbeiter gelöscht")
    else:
      UpdateConsole("Mitarbeiter konnte nicht gelöscht werden")
  elif ActionKey == -303: # Mitarbeiter Anzeigen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,v in enumerate(get_Worker()):
      print(f"ID: {v[0]} {v[1]} {v[2]}")
    Menu.setContinue_(True)
    print("\n Drücke [backspace] um zurück zum Menü zu gehen")
  
  
  elif ActionKey == -401: # Raum Hinzufügen
    os.system('cls' if os.name == 'nt' else 'clear')
    og = input("UG/EG/OG: ")
    number_1 = input("Geschoss Nummer: ")
    number_2 = input("Raum Nummer: ")
    success = add_Room(og+"_"+number_1+"_"+number_2)
    if success == True:
      UpdateConsole("Raum hinzugefügt")
    else:
      UpdateConsole("Raum konnte nicht hinzugefügt werden")
  elif ActionKey == -402: # Raum Löschen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,v in enumerate(get_Room()):
      print(f"ID: {v[0]} {v[1]}")
    print("\n")
    id = input("ID: ")
    success = remove_Room(id)
    if success == True:
      UpdateConsole("Raum gelöscht")
    else:
      UpdateConsole("Raum konnte nicht gelöscht werden")
  elif ActionKey == -403: # Räume Anzeigen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,v in enumerate(get_Room()):
      print(f"ID: {v[0]} {v[1]}")
    Menu.setContinue_(True)
    print("\n Drücke [backspace] um zurück zum Menü zu gehen")
  
  
  elif ActionKey == -501: # Buchung Hinzufügen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,v in enumerate(get_Worker()):
      print(f"ID: {v[0]} {v[1]} {v[2]}")
    print("\n")
    worker_id = input("Mitarbeiter ID: ")
    for i,v in enumerate(get_Room()):
      print(f"ID: {v[0]} {v[1]}")
    print("\n")
    room_id = input("Raum ID: ")
    date = GetDate()
    print(f"Datum: {date}")

    alleBuchungen = get_Booking()
    for i,v in enumerate(alleBuchungen):
      if v[3].split(".")[0] == date.split(".")[0] and v[3].split(".")[1] == date.split(".")[1] and v[3].split(".")[2] == date.split(".")[2]: # Gucken ob Buchung für den Tag schon existiert
        for _i, _v in enumerate(Zeiten):
          if _v == v[3]:
            Zeiten.pop(_i) # Wenn Ja dann raus aus unseren buchbaren Zeiten

    for i, v in enumerate(Zeiten):
      print(f"{i+1}. {v}")

    time = input("Uhrzeit Nummer: ")
    success = add_Booking(int(worker_id), int(room_id), date, Zeiten[int(time)-1])
    if success == True:
      UpdateConsole("Buchung hinzugefügt")
    else:
      UpdateConsole("Buchung konnte nicht hinzugefügt werden")
  elif ActionKey == -502: # Buchung Löschen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,v in enumerate(get_Booking()):
      print(f"ID: {v[0]} {v[1]} {v[2]} {v[3]}")
    print("\n")
    id = input("ID: ")
    success = remove_Booking(id)
    if success == True:
      UpdateConsole("Buchung gelöscht")
    else:
      UpdateConsole("Buchung konnte nicht gelöscht werden")
  elif ActionKey == -503: # Alle Buchungen Anzeigen
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,v in enumerate(get_Booking()):
      print(f"ID: {v[0]} {v[1]} {v[2]} {v[3]} {v[4]}")
    Menu.setContinue_(True)
    print("\n Drücke [backspace] um zurück zum Menü zu gehen")
  
  
  elif ActionKey == -701: # Buchungen ansehen für den aktuellen Tag
    os.system('cls' if os.name == 'nt' else 'clear')
    
    date = GetDate()
    print(f"Datum: {date}")

    aktuelleBuchungen = []
    alleBuchungen = get_Booking()
    for i,v in enumerate(alleBuchungen):
      if v[3].split(".")[0] == date.split(".")[0] and v[3].split(".")[1] == date.split(".")[1] and v[3].split(".")[2] == date.split(".")[2]: # Gucken ob Buchung für den Tag existiert
        for _i, _v in enumerate(Zeiten):
          if _v == v[4]:
            aktuelleBuchungen.append(v)

    for i,v in enumerate(aktuelleBuchungen):
      print(f"{i+1}. {v[1]} {v[2]} {v[3]} {v[4]}")

    Menu.setContinue_(True)
    print("\n Drücke [backspace] um zurück zum Menü zu gehen")

Menu.register_event(GetMenuAction)

Menu.setupMenu()

