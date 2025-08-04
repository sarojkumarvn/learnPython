
x = 2054 # global variable

def myfunc():
  x = 300 # local variable of myfunc
  def myinnerfunc():
    print(x) 
  myinnerfunc()

myfunc()
print(x)


def func3() :
  global y 
  y = 3255442
  print(y % 10000)



func3()
print(y)



