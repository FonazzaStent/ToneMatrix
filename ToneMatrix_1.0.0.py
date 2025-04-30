"""ToneMatrix 1.0.0 - Generate a random twelve-tone serial music matrix
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

from tkinter import *
import random

notes=['C ','C#','D ','D#','E ','F ','F#','G ','G#','A ','A#','B ']

root = Tk()
top=root
top.geometry ("665x330")
top.title("Tone Matrix")
top.resizable(0,0)
transpindex=0

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

def transpose_print (row, opci):
    transposed = [modconvert(x+opci) for x in row]
    
    #newrow = f'P{transposed[0]} {transposed} R{transposed[0]}'
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


  

if __name__ == "__main__":
    labels={}
    height = 14
    width = 14
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = Label(top, text="--")
            labels[(i,j)]=b
            b.configure(width=6)
            b.grid(row=i, column=j)
    #myrow = [2, 11, 6, 5, 4, 3, 0, 8, 9, 7, 1, 10]
    myrow=generate_twelve_tone_series()

    generatematrix(myrow)

    mainloop()     
