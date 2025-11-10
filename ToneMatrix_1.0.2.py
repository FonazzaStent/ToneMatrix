"""ToneMatrix 1.0.2 - Generate a random twelve-tone serial music matrix
Copyright (C) 2025  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import tkinter as tk
from tkinter import ttk
import random
from PIL import ImageGrab
from tkinter.filedialog import asksaveasfilename

notes=['C ','C#','D ','D#','E ','F ','F#','G ','G#','A ','A#','B ']
transpindex=0


def create_window():
    global root
    global top
    global newmatrix
    global basic_set_entry
    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAAXNSR0IB2cksfwAAAARnQU1BAACxjwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+kFBQ4tK4SpEQ0AAAL2SURBVEjHzZa9T/pAGMevLamVgjFQmviSsBzRxPo6uLBAHIiGAXRxII7+A24u/gMkmphgHEycXUwYDQnRFGKYxFFjHBQjLTQEgYJw19/QBEl/iEUx8Tu1d73n03t5vs8RmqaB3xQJflmmALe3t4qifJOgmVA4HAYAbG5unpycXF9fy7KsmRZhZg/W19fv7u4AAKqqViqVYrEYCoUCgYAgCBBCjuMIgvhsrFnA/f390NBQe9Lv7+9t2Nra2urq6uzsLISQ53kD7DsAwwrrsGq1WiwWV1ZWgsHg3NwchHBsbAwAYDG5VbIsj4yMMAxD07TeghBCCGGMMcYWi8Vut7Mse3Nzk0gkWq2Wzu4DsL+/L0lSPB4XRZFhmEqlgjEe5Cl6enrSNA0h9PLycnV1dXh4GAgEzETuD9ApjPHr66soirFYLBgMAgBIkuR5HkI4NTU1AIABls/n0+n08fFxOBzWD9IgAQaYnjT66+C9iCCI0dHRP2Z2fxrwkWi1Wk2WZYqiHA6H1Wod8Ayy2ezy8jKEEELodDp3d3dTqVSj0RgYIBqN1mq1+fl5QRCmp6fPz883NjZCoVAqlTJrCb0BiUSCoij9maIolmUnJydzuZzf7z84OKhWqz8FRCKRh4cHWZYbjQbGWNO0Vqulqmqz2dzZ2bm4uOg6uNlsKoryBV7Pt2w22/tH/s/ky8vLpaUlvXdra+vs7CyXy+ldkiR1sYpkMul2u3vUg87o5XKZ53mPx7O4uLiwsDAzM+N2u2majkaj+Xy+E/CRBz6fL5PJnJ6e+ny+ztA8z8fjcY7jOhvL5bIkScPDwyRJUhTFMAzHcYIgxGIxv98vimKvkokQKhQKiqLU63Wr1To+Pm632w3fvL29uVwumqYnJiZ0DAAAY1wqlR4fH9uLb7bgdNXR0VHb3ViWtdlshnLfh113laqqe3t7n+2Z1+v9KUA/yul0ent72xDd5XKJotjHxetLFQqF5+fnUqmEELLZbB6Px+Fw9HEv+tN2/Q8x2Lp9uoNtEAAAAABJRU5ErkJggg=='

    root = tk.Tk()
    top=root
    top.geometry ("756x490")
    top.title("ToneMatrix")
    top.resizable(0,0)
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)
    newmatrix = tk.Button(top, text="New Matrix", command=new_matrix)
    newmatrix.place(height=30,width=80,x=200,y=400)
    screenshot = tk.Button(top, text="Save", command=take_screenshot)
    screenshot.place(height=30,width=60,x=300,y=400)
    quitbutton = tk.Button(top, text="Exit", command=QuitApp)
    quitbutton.place(height=30,width=60,x=380,y=400)
    basic_set_entry=ttk.Entry(top)
    basic_set_entry.place(height=40, width=600,x=20,y=440)
    basic_set_entry.focus_set()
    basic_set_entry.bind('<Return>',basic_set_confirm_event)
    basic_set_button=tk.Button(top, text='OK', command=basic_set_confirm)
    basic_set_button.place(height=30, width=40, x=630,y=440)
    

def QuitApp():
    top.destroy()

def generate_twelve_tone_series():
    # Generate a list of numbers from 0 to 11
    series = list(range(12))
    # Shuffle the list to create a random twelve-tone series
    random.shuffle(series)
    return series

# Helper functions we have built so far
def modconvert(num):
  if num >= 0 and num < 12:
    return num
  else:
    return num % 12

def take_screenshot():
    global root
    data=[('JPG','*.jpg')]
    filename=asksaveasfilename(filetypes=data, defaultextension=data)
    if filename!='':
        # Get the window coordinates
        x = top.winfo_rootx()
        y = top.winfo_rooty()
        width = x + top.winfo_width()
        height=y+390

        # Take the screenshot
        ImageGrab.grab().crop((x, y, width, height)).save(filename)


def transpose_print (row, opci):
    transposed = [modconvert(x+opci) for x in row]
    
    notelist=[notes[y] for y in transposed]

    # Naming convention to tighten matrix's looks up

    labels[transpindex+1,0].config(text="P"+str(transposed[0]))
    labels[transpindex+1,13].config(text="R"+str(transposed[0]))
    for col in range (0,12):
        labels[transpindex+1,col+1].config(text=notelist[col])

def make_torder(row):
    # Creates the list of intervals by which 
    # You need to transpose and print the prime row
    # First el is always 0
    Torder = [0]
    
    # Append inversion of distance between each element and first element
    for x in range(1,12):
        i = modconvert(row[0] - row[x])
        Torder.append(i)
    
    return Torder

# Assembling helper functions
def generatematrix(row):

  # Make Torder
  Torder = make_torder(row)
  
  # Printing Matrix
  first_row_list=[]
  for el in row:
      first_row_list.append("I"+str(el))
  #print (first_row_list)
  for col in range (0,12):
      labels[0,col+1].config(text=first_row_list[col])


  for x in Torder:
      global transpindex
      transpose_print(row, x)
      transpindex=transpindex+1

  last_row_list=[]
  for el in row:
      last_row_list.append("RI"+str(el))
  #print (last_row_list)
  for col in range (0,12):
      labels[13,col+1].config(text=last_row_list[col])

def new_matrix():
    global labels
    global transpindex
    transpindex=0
    myrow=generate_twelve_tone_series()
    generatematrix(myrow)

def new_matrix_norand():
    global labels
    global transpindex
    transpindex=0
    generatematrix(myrow)
    #take_screenshot()

def basic_set_confirm_event(event):
    basic_set_confirm()

def basic_set_confirm():
    global labels
    global myrow
    basic_set_string=basic_set_entry.get()+'...'
    string_length=len (basic_set_string)
    simple=True
    basic_set_list=[]
    notes_check=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    notes_nospace=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    for n in range (0,string_length-1):
        single=basic_set_string[n]
        token=basic_set_string[n:n+2]
        counter=0
        for note in notes_check:
            if token[1]=='#' and token==note:
                simple=False
                if notes_check!=[]:
                    basic_set_list.append(note)
                    notes_check.remove(note)
                    counter=counter+1
        if simple==True:
            counter=0
            for note in notes_check:
                if single==note:
                    if notes_check!=[]:
                        basic_set_list.append(note)
                        notes_check.remove(note)
                        counter=counter+1


        simple=True
    random.shuffle(notes_check)
    basic_set_list=basic_set_list+notes_check
    myrow=[]
    counter=0
    for noteset in basic_set_list:
        myrow.append(notes_nospace.index(noteset))
    new_matrix_norand()            
                    
            


def create_matrix():
    global labels
    labels={}
    height = 14
    width = 14
    font = ("Helvetica", 14, "bold")
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Label(top, text="--", bg='white',font=font)
            labels[(i,j)]=b
            b.configure(width=4)
            b.grid(row=i, column=j)
    #myrow = [2, 11, 6, 5, 4, 3, 0, 8, 9, 7, 1, 10]
    myrow=generate_twelve_tone_series()

    generatematrix(myrow)
    #take_screenshot()

create_window()
create_matrix()
top.mainloop()     
