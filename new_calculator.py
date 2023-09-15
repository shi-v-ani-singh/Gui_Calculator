# importing the modules
from tkinter import *
from tkinter import messagebox

# setting initial values
# setting the initial values of some variables  
var = ""  
A = 0  
operator = ""  
  
# defining the function for Button 1  
def _1_is_Clicked():  
    global var  
    var = var + "1"  
    data.set(var)  
# defining the function for Button 2  
def _2_is_Clicked():  
    global var  
    var = var + "2"  
    data.set(var)  
  
# defining the function for Button 3  
def _3_is_Clicked():  
    global var  
    var = var + "3"  
    data.set(var)  
  
# defining the function for Button 4  
def _4_is_Clicked():  
    global var  
    var = var + "4"  
    data.set(var)  
  
# defining the function for Button 5  
def _5_is_Clicked():  
    global var  
    var = var + "5"  
    data.set(var)  
  
# defining the function for Button 6  
def _6_is_Clicked():  
    global var  
    var = var + "6"  
    data.set(var)  
  
# defining the function for Button 7  
def _7_is_Clicked():  
    global var  
    var = var + "7"  
    data.set(var)  
  
# defining the function for Button 8  
def _8_is_Clicked():  
    global var  
    var = var + "8"  
    data.set(var)  
  
# defining the function for Button 9  
def _9_is_Clicked():  
    global var  
    var = var + "9"  
    data.set(var)  
  
# defining the function for Button 0  
def _0_is_Clicked():  
    global var  
    var = var + "0"  
    data.set(var)  
  
# defining the function for Button +  
def _Add_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    data.set(var)  
  
# defining the function for Button -  
def _Sub_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    data.set(var)  
  
# defining the function for Button *  
def _Mul_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    data.set(var)  
  
# defining the function for Button /  
def _Div_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    data.set(var)  
  
# defining the function for Button =  
def _Equal_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    data.set(var)  
  
# defining the function for Button C  
def _C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    data.set(var)  
  
# defining the function to display result  
def result():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            data.set(var)  
        else:  
            x = float(A/a)  
            data.set(x)  
            var = str(x)  
# creating window for the gui calculator

# creating obj as root of Tk() class
root = Tk()
# setting the size of window
root.geometry("320x499")
# disabling the resize option
root.resizable(0,0)
# setting the title of calculator window
root.title("GUI Calculator")
# creating the label for the window  
data = StringVar()  
display_Label = Label(  
    root,  
    text = "Label",  
    anchor = SE,  
    font = ("Cambria Math", 20),  
    textvariable = data,  
    background = "black",  
    fg = "white"  
)  
# using the pack() method  
display_Label.pack(expand = True, fill = "both")  

# creating the frames for the buttons  
# first frame  
frameOne = Frame(root, borderwidth=10 )
frameOne.pack(expand = True, fill = "both") # frame can expand if it gets some space  
  
# second frame  
frameTwo = Frame(root,borderwidth=10  )
frameTwo.pack(expand = True, fill = "both")  
  
# third frame  
frameThree = Frame(root,borderwidth=10 )
frameThree.pack(expand = True, fill = "both")  
  
# fourth frame  
frameFour = Frame(root,borderwidth=10) 
frameFour.pack(expand = True, fill = "both")  

# creating buttons for each frame  
# buttons for first frame  
# button 1  
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _1_is_Clicked  
)  
# placing buttons side by side  
buttonONE.pack(side = LEFT, expand = True, fill = "both")
# button 2  
buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _2_is_Clicked  
)  
# placing buttons side by side  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  

# button 3  
buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _3_is_Clicked  
)  
# placing buttons side by side  
buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  
  
# button C  
buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Cambria", 22),  
    relief = GROOVE, 
    bg="orange",
    border = 4,  
    command = _C_is_Clicked  
)  
# placing buttons side by side  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for second frame  
# button 4  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _4_is_Clicked  
)  
# placing buttons side by side  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
# button 5  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _5_is_Clicked  
)  
# placing buttons side by side  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 6  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _6_is_Clicked  
)  
# placing buttons side by side  
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,    
    bg="red",
    command =_Add_is_Clicked  
)  
# placing buttons side by side  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for third frame  
# button 7  
buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _7_is_Clicked  
)  
# placing buttons side by side  
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  
# button 8  
buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _8_is_Clicked  
)  
# placing buttons side by side  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
# button 9  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _9_is_Clicked  
)  
# placing buttons side by side  
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  
# button -  
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,   
    bg="red", 
    command = _Sub_is_Clicked  
)  
# placing buttons side by side  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for fourth frame  
# button 0  
buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    command = _0_is_Clicked  
)  
# placing buttons side by side  
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
# button *  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,   
    bg="red",
    command = _Mul_is_Clicked  
)  
# placing buttons side by side  
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
# button /  
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4,  
    bg="red",  
    command = _Div_is_Clicked  
)  
# placing buttons side by side  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 4, 
    bg="green",  
    command = result  
)  
# placing buttons side by side  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both") 
 
# running the GUI 
root.mainloop()  