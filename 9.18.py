"""
9.18 Implement a GUI application that allows users to compute their body mass index
(BMI), which we defined Practice Problem 5.1.

5.1 Implement function myBMI() that takes as input a person’s height (in inches) and weight
(in pounds) and computes the person’s Body Mass Index (BMI). The BMI formula is:
bmi = (weight ∗ 703)/height^2
Your functions should print the string 'Underweight' if bmi < 18.5, 'Normal' if 18.5 <=
bmi < 25, and Overweight if bmi >= 25

Solution:
After computing the BMI, we use a multiway if statement to decide what to print:
def myBMI(weight, height):
'prints BMI report'
bmi = weight * 703 / height**2
if bmi < 18.5:
print('Underweight')
elif bmi < 25:
print('Normal')
else: # bmi >= 25
print('Overweight')
"""

"""
Import library functions required
Button and Frame for class inheritance and for calculate bmi button
showinfo to create new info with bmi information after clicking calculate bmi button
Entry for user entering data
END as glo0bal variable for end of string in Entry

"""
import math
from tkinter import Tk, Frame, Button, Entry, Label, END
from tkinter.messagebox import showinfo

class BMI(Frame):
    """
    Class that calculate the BMI using a GUI and user input
    """

    def __init__(self, master):
        """
        Initializes and sets self.height, self.weight, organizes widget with labels and button
        """
        #override frame constructor
        Frame.__init__(self, master)
        self.pack() #pack organizes original widget

        #set the labelf or enetering height in the widget
        labelHeight = Label(self, text='Enter Height: ')
        labelHeight.grid(row=0, column=0)

        #get height using tkinter Entry module and set it next to Enter Height Label
        #uses instance variable
        self.height = Entry(self)
        self.height.grid(row=0, column=1)

        #set the label for entering weight in widget
        labelWeight = Label(self, text='Enter Weight: ')
        labelWeight.grid(row=1, column=0)

        #get user weight
        self.weight = Entry(self)
        self.weight.grid(row=1, column=1)

        #set up button
        button = Button(self, text='Compute BMI', command=self.clicked)
        button.grid(row=2, column=0, columnspan=2)

    def clicked(self):
        """
        Calculate BMI once button is clicked
        bmi = (weight ∗ 703)/height^2
        """
        #uses get function of the Entry object weight and height
        weight = float(self.weight.get())
        height = float(self.height.get())

        inter = weight * 703
        bmi = inter / pow(height,2)        

        showinfo(message= bmi)


#instantiate Tk object
root = Tk()
#create BMI class object
bmi = BMI(root)
#placed at top boundary of root
bmi.pack()
#create window 
root.mainloop()