import pip
import barcode

# import the modules 

from barcode import EAN13
from barcode.writer import ImageWriter
import win32print
import os 

def get_and_save_barcode():
   #Ask for a number as input 
   number = input("Enter the part code: ")

   # Create a barcode object with the number and the image writer 
   my_barcode = EAN13(number, writer=ImageWriter())

   # Save the barcode as an image file 
   filename = input("What do you want to save your barcode as: ")
   my_barcode.save(filename)

   # Print a message to confirm 
   print("Your barcode is saved as "+filename)
 
get_and_save_barcode()

def print_file(filename):
   # Get the default printer name 
   default_printer_name = win32print.GetDefaultPrinter()
   





