from tkinter import *
import math
import tkinter.messagebox


root = Tk()
root.title("calculater")
root.resizable(width=False,height=False)
root.configure(background="orange")
root.geometry("480*624+20+20")

calc = Frame(root)
calc.grid()


#------------------------------------class inside functions------------------------------------------------------------------------------------------


class calc():
    def __init__(self):
        self.total=0
        self.current=" "
        self.input_value=True
        self.check_sum=True
        self.op=''
        self.result=False

    def NumberEnter(self,num):
        self.result = False
        FirstNum  = txtDisplay.get()
        Secondnum = float(num)
        if self.input_value:
            self.current = Secondnum
            self.input_value=False
        else:
            if Secondnum == '.':
                if Secondnum in FirstNum:
                    return
                self.current = FirstNum+Secondnum
            self.display(self.current)

    def sum_of_total(self):
         self.result=False
         self.current=float(self.current)
         if self.check_sum == True:
             self.valid_function()
         else:
            self.total = float(txtDisplay.get())

    def valid_function(self):
         if self.op == "add":
             self.total += self.current
         if self.op == "sub":
             self.total -= self.current
         if self.op == "multi":
             self.total *= self.current
         if self.op == "divide":
             self.total /= self.current
         if self.op == "mod":
             self.total %= self.current
         if self.op == "inv":
              self.total = 1 / self.current

         self.input_value = True
         self.check_sum = False
         self.display(self.total)

    def operation(self , op):
         self.current = float(self.current)
         if self.check_sum:
             self.valid_function()
         elif not self.result:
           self.total = self.current
           self.input_value = True
         self.check_sum = True
         self.op = op
         self.result = False


    def clear_entery(self):
        self.result = False
        self.current= "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entery(self):
        self.clear_entery()
        self.total = 0

    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0 , value)

    def tanh(self):
         self.result = False
         self.current = math.tanh(math.radians(float(txtDisplay)))
         self.display(self.current)

    def tan(self):
         self.result = False
         self.current = math.tan(math.radians(float(txtDisplay)))
         self.display(self.current)

    def cosh(self):
          self.result = False
          self.current = math.cosh(math.radians(float(txtDisplay)))
          self.display(self.current)

    def cos(self):
         self.result = False
         self.current = math.cos(math.radians(float(txtDisplay)))
         self.display(self.current)

    def sinh(self):
          self.result = False
          self.current = math.sinh(math.radians(float(txtDisplay)))
          self.display(self.current)

     def sin(self):
         self.result=False
         self.current=math.sin(math.radians(float(txtDisplay)))
         self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay)))
        self.display(self.current)

    def acosh(self):
         self.result = False
         self.current =math.acos(float(txtDisplay.get()))
         self.display(self.current)

    def asinh(self):
         self.result = False
         self.current = math.asinh(float(txtDisplay.get()))

    def log(self):
        self.result = False
        self.current =math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))

    def log10(self):
        self.result =False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
         self.result = False
         self.current = math.log1p(float(txtDisplay.get()))
         self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def lgamma(self):
         self.result = False
         self.current = math.lgamma(float(txtDisplay.get()))
         self.display(self.current)

    def expm1(self):
         self.result = False
         self.current = math.expm1(float(txtDisplay.get()))
         self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current =- (float(txtDisplay.get()))
        self.display(self.current)

    def squareROOT(self):
         self.result = False
         self.current = math.sqrt(float(txtDisplay.get()))
         self.display(self.current)

    def tau(self):
        self.result =False
        self.current = math.tau
        self.display(self.current)

    def degree(self):
         self.result = False
         self.current = math.degrees(float(txtDisplay.get()))
         self.display(self.current)

    def exp(self):
        self.result =False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

add_value = calc()
#------------------------------------display numbers---------------------------------------------------------------------------------------------------


numberpad ="789456123"
i=0
btn=[]

for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc , width = 6 , height= 2 , font=('arial', 20 , 'bold'), bd=4 ,text = numberpad[i]))
        btn[i].grid(row=j , coloum= k , pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: add_value.NumberEnter(x)

#-------------------------------------------------------------------BUTTON STANDARD--------------------------------------------------------------------

btnClear=Button(calc ,text=chr(67), width=6 , height=2 , font=("ariel" , 20 , "bold", ), bd=4 , bg='powder blue' , command= add_value.clear_entery()).grid(row=1 ,coloum=0,pady=1)
btnAllClear=Button(calc ,text=chr(67) + chr(69), width=6 ,height=2 , font=("ariel", 20 , "bold"), bd=4 , bg='powder blue' , cpmmand=add_value.All_Clear_Entery()).grid(row=1,coloum=1,pady=1)

btnSquareROOT=Button(calc ,text="√", width=6 , height=2 , font=("ariel" , 20 , "bold"), bd=4 , bg = 'powder blue' , command=add_value.squareROOT()).grid(row=1 , coloum=2, pady=1)
btnadd=Button(calc ,text='+', width=6 , height= 2 ,font=("ariel" , 20 , "bold") , bd=4 , bg="powder blue" , command=add_value.operation('add')).grid(row=1,coloum=3,pady=1)

btnsub=Button(calc ,text="-", width=6 ,height=2, font=("ariel",20,'bold'), bd=4, bg="powder blue" , command=add_value.operation('sub')).grid(row=2,coloum=3,pady=1)
btnmulti=Button(calc ,text="×", width=6,height=2,font=('ariel' , 20,'bold'), bd=4 ,bg='powder blue',command=add_value.operation('multi')).grid(row=3,coloum=3,pady=1)


btnDivide =Button(calc ,text="chr(247)", width=6 , height=2 , font=("ariel", 20 , 'bold') ,  bd=4 , bg="powder blue" , command=add_value.operation("div")).grid(row=4 ,coloum=3, paddy=1)
btnEqual= Button(calc , text="=" , width=6 , height=2 , font= ("ariel" , 20 , "bold") , bd=4, bg="powder blue" , command= add_value.sum_of_total).grid(row=5,coloum=3 , pady=1)

btnpm= Button (calc , text= chr(177) , width=6 ,height= 2 ,font=("ariel" , 20 , "bold"),bd=4 , bg='powder blue' ,command=add_value.mathPM).grid(row='5',coloum='2', pady=1)
btnDOT=Button(calc, text='.',width=6 , height=2, font=("ariel",20,"bold"),bd=4 , bg="powder blue" ,command=add_value.NumberEnter).grid(row=5 , coloum='1',pady=1)

btnZero= Button(calc , text="0" , width=6 ,height=2 ,font=("ariel" ,20 ,"bold") ,bd=4, bg="powder blue" , command=add_value.NumberEnter(0)).grid(row=5,coloum=1,pady=1)


#-----------------------------------------------------------scientific calculater-------------------------------------------------------------------------------------------------------------------

btnpi=Button(calc,text='π' , width=6 ,height=2 , font=("ariel" , 20 , 'bold'), bd=4 , bg="powder blue" , command=add_value.pi).grid(row=1 , coloum=4 , pady=1)
btnCos=Button(calc ,text='cos' ,width=6 , height=2 ,font=('ariel' ,20 , 'bold'), bd=4 ,bg='powder blue' ,command=add_value.cos).grid(row=1,coloum=5,pady=1)

btnTan=Button(calc ,text='tan' ,width=6 ,height=2 , font=('ariel' , 20 ,'bold') , bd=4 ,bg='powder blue', command=add_value.tan).grid(row=1 ,coloum=6,pady=1)
btnSin=Button(calc , text='sin', width=6 , height=2 , font=('ariel',20,'bold'), bd=4 ,bg='powder blue' ,command=add_value.sin).grid(row=1,coloum=7,pady=1)

btn2pi=Button(calc , text='2π', width=6 ,height=2,font=('ariel',20,'bold'),bd=4 ,bg='powder blue',command=add_value.tau).grid(row=2,coloum=4,pady=1)
btnCosh=Button(calc ,text='cosh', width=6 , height=2 ,font=('ariel',20,'bold'),bd=4,bg='powder blue',command=add_value.cosh).grid(row=2,coloum=5,pady=1)

btnTanh=Button(calc , text='tanh',width=6,height=2,font=('ariel',20,'bold'),bd=4,bg='powder blue',command=add_value.tanh).grid(row=2,coloum=6,pady=1)
btnSinh=Button(calc , text='tanh',width=6,height=2,font=('ariel',20,'bold'),bd=4,bg='powder blue',command=add_value.sinh).grid(row=2,coloum=7,pady=1)

btnlog=Button(calc , text='log', width=6 ,height=2,font=('ariel',20,'bold'),bd=4 ,bg='powder blue',command=add_value.log).grid(row=3,coloum=4,pady=1)
btninv=Button(calc ,text='inv', width=6 , height=2 ,font=('ariel',20,'bold'),bd=4,bg='powder blue',command=add_value.operation('inv')).grid(row=3,coloum=5,pady=1)

btnmod=Button(calc , text='Mod',width=6,height=2,font=('ariel',20,'bold'),bd=4,bg='powder blue',command=add_value.operation('Mod')).grid(row=3,coloum=6,pady=1)
btne = Button(calc , text='e',width=6,height=2,font=('ariel',20,'bold'),bd=4,bg='powder blue',command=add_value.e).grid(row=3,coloum=7,pady=1)

btnlog2=Button(calc , text='log2',width=6 ,height=2 ,font=('ariel',20,'bold'),bd=4,bg='powder blue' , command=add_value.log2)






















#--------------------------------------Display------------------------------------------------------------------

txtDisplay=Entry (calc , relief = SUNKEN , font=("ariel" , "20" , "bold") , bg= 'orange', bd='30', width="30" ,justify="right")
txtDisplay.grid(row="0" , coloum="0" ,coloumspam="4" , pady= "1")
txtDisplay.insert(0,"0")

#--------------------------------------------          ----------------------------------------------------------------------------