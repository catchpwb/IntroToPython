"""
9.19 Develop a GUI application whose purpose is to compute the monthly mortgage payment given a loan amount (in $), the interest rate (in %), and the loan term (i.e., the number
of months that it will take to repay the loan). The GUI should have three labels and three entry boxes for users to enter this information. It should also have a button labeled 
“Compute mortgage” that, when clicked, should compute and display the monthly mortgage in a fourth entry box.
The monthly mortgage m is computed from the loan amount a, interest rate r, and loan terms t as:
    m = (a*c*(1+c)^t) / ((1+c)^t - 1)
where c = r/1200.
"""
import math
from tkinter import Tk, Frame, Button, Entry, Label, END
from tkinter.messagebox import showinfo

class monthlyMortgage(Frame):
    """
    Class that caclulates the monthly mortgage payment
    """

    def __init__(self, master):
        """
        extends the Frame __init__() constructor.
        There are two reasons why we are doing that:
            1. We want the monthlyMortgage widget to get initialized just like a Frame widget so it is a
            full-fledged Frame widget.
            2. We want the monthlyMortgage widget to be assigned a master the same way any Frame
            widget is assigned a master; we thus pass the master input argument of the ClickIt
            constructor to the Frame constructor.

        """
        Frame.__init__(self, master)
        master.geometry("400x90")   #set size of window
        master.title("Monthly Mortgage Calculator") #add title to window
        self.pack()
        
        #set the label for entering loanAmount in the widget
        loanAmount = Label(self, text='Enter the loan amoun in $: ')
        loanAmount.grid(row=0, column=0)

        #get loan amount using tkinter Entry module and set it next to loan amount Label
        #uses instance variable
        self.loanAmount = Entry(self)
        self.loanAmount.grid(row=0, column=1)

        #set the label for entering interestRate in the widget
        interestRate = Label(self, text='Enter the interest rate in %: ')
        interestRate.grid(row=1, column=0)

        #get interestRate using tkinter Entry module and set it next to interestRate Label
        #uses instance variable
        self.interestRate = Entry(self)
        self.interestRate.grid(row=1, column=1)

        #set the label for entering loanTerm in the widget
        loanTerm = Label(self, text='Enter the loan term in months: ')
        loanTerm.grid(row=2, column=0)

        #get loanTerm using tkinter Entry module and set it next to loanTerm Label
        #uses instance variable
        self.loanTerm = Entry(self)
        self.loanTerm.grid(row=2, column=1)

        #initilize empty Label
        #must be an instance variable since we are changing it
        self.mortgageLabel = Label(self, text='')
        self.mortgageLabel.grid(row=3, column=1)

        #set up button
        button = Button(self, text='Compute monthly Mortgage: ', command=self.clicked)
        button.grid(row=3, column=0)


    def clicked(self):
        """
        The monthly mortgage m is computed from the loan amount a, interest rate r, and loan terms t as:
            m = (a*c*(1+c)^t) / ((1+c)^t - 1)
        where c = r/1200.
        """
        #checks to make sure data is a number
        try:
            amount = float(self.loanAmount.get())
            rate = float(self.interestRate.get())
            terms = float(self.loanTerm.get())
        except:
            showinfo(message="Loan amount, interest rate, and loan terms must be numbers. Try again")
        else:
            c = rate / 1200
            inter1 = amount * c * pow(1+c, terms)
            inter2 = pow(1+c,terms) - 1

            txt = inter1/inter2
            self.mortgageLabel.config(text= str(txt))


if __name__ == '__main__':
    #avoids running code if module is imported
    #add just in case
    #instantiate Tk object
    root = Tk()
    #create BMI class object
    mortgage = monthlyMortgage(root)
    #placed at top boundary of root
    mortgage.pack()
    #create window 
    root.mainloop()
    print("in main")