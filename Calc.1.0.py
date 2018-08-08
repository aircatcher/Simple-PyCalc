from Tkinter import *
import Tkinter
import tkMessageBox

root = Tk()

''' Title Bar '''
root.title("PyCalc 1.0")

''' Calculator '''
L1 = Label(root, text = "Py Calc 0.1 by @aircatcher", font = 'Arial 12 bold').grid(row = 0, column = 0, columnspan = 2)
L1 = Label(root).grid(row = 1, column = 0)
L2 = Label(root, text = "Number 1", font = 'Arial 12').grid(row = 2, column = 0)
L3 = Label(root, text = "Number 2", font = 'Arial 12').grid(row = 3, column = 0)
L4 = Label(root, text = "Operator", font = 'Arial 12').grid(row = 4, column = 0)
L5 = Label(root, text = "Answer", font = 'Arial 12').grid(row = 5, column = 0)
errText = StringVar()
L6 = Label(root, textvariable = errText)

E1 = Entry(root, bd =5)
E1.grid(row = 2, column = 1)
E2 = Entry(root, bd =5)
E2.grid(row = 3, column = 1)
E3 = Entry(root, bd =5)
E3.grid(row = 4, column = 1)
E4 = Entry(root, bd =5)
E4.grid(row = 5, column = 1)

''' Simple calculation function '''
def beginCalculate():
  if Entry.get(E1) and Entry.get(E2) and Entry.get(E3):
    numStr1 = Entry.get(E1)
    num1 = float(numStr1)

    numStr2 = Entry.get(E2)
    num2 = float(numStr2)

    operator = Entry.get(E3)
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
      if operator == '+':
        result = num1 + num2
      if operator == '-':
        result = num1 - num2
      if operator == '*':
        result = num1 * num2
      if operator == '/':
        result = num1 / num2

      '''
      Make it more pretty by converting it to standard integer when the result doesn't have float in it
      Like for e.g
      >> 12.0
      By converting it to integer type, the .0 will be gone
      '''
      resultInString = str(result)
      if resultInString[-2:] == '.0':
        result = int(result)

      if not Entry.get(E4):
        # Result box is empty
        Entry.insert(E4, 0, result)
      else:
        # Result box is not empty
        E4.delete(0, END)
        Entry.insert(E4, 0, result)
    else:
      errText.set('Wrong operator, please enter +, -, *, or /')
  else:
    errText.set('Fill in the boxes correctly')

Button(root, text ="Calculate", command = beginCalculate).grid(row = 6, column = 1)

root.mainloop()