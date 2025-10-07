"""
8.25 pg 325
Implement class Worker that supports methods:
• __init__(): Constructor that takes as input the worker’s name (as a string) and the
hourly pay rate (as a number)
• changeRate(): Takes the new pay rate as input and changes the worker’s pay rate
to the new hourly rate
• pay(): Takes the number of hours worked as input and prints 'Not Implemented'

Next develop classes HourlyWorker and SalariedWorker as subclasses of Worker. Each
overloads the inherited method pay() to compute the weekly pay for the worker. Hourly
workers are paid the hourly rate for the actual hours worked; any overtime hours above
40 are paid double. Salaried workers are paid for 40 hours regardless of the number of
hours worked. Because the number of hours is not relevant, the method pay() for salaried
workers should also be callable without an input argument.
>>> w1 = Worker('Joe', 15)
>>> w1.pay(35)
Not implemented
>>> w2 = SalariedWorker('Sue', 14.50)
>>> w2.pay()
580.0
>>> w2.pay(60)
580.0
>>> w3 = HourlyWorker('Dana', 20)
>>> w3.pay(25)
500
>>> w3.changeRate(35)
>>> w3.pay(25)
875
"""

class Worker:
    
    def __init__(self, workerName, workerPayRate):
         
         self.workerName = workerName
         self.workerPayRate = workerPayRate

    def changeRate(self, newPayRate):
         self.workerPayRate = newPayRate
        
    def pay(self, numHours):
         print("NOT IMPLEMENTED")

class HourlyWorker(Worker):
     "child class of worker that extends the pay method for hourly workers"
     def pay(self,numHours):
        if(0 <= numHours <= 40):
            print(numHours * self.workerPayRate)
        elif(numHours > 40):
            print((numHours - 40) * self.workerPayRate * 2 + 40 * self.workerPayRate)

class SalariedWorker(Worker):
    "child class of worker that extends pay method to salaried employess"
    def pay(self,numHours = 40):
        print(40 * self.workerPayRate)

w1 = Worker('Joe', 15)
w1.pay(35)
w2 = SalariedWorker('Sue', 14.50)
w2.pay()
w2.pay(60)
w3 = HourlyWorker('Dana', 20)
w3.pay(25)
w3.changeRate(35)
w3.pay(25)
