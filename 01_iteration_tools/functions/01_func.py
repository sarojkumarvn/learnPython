def myFunction (user , age ) :
    print ("Hello", user )
    print ("You are", age , "years old")

# myFunction("Saroj" , 21)• 



# args
def arbsFunc (*kids) :
    print ("The youngest child is " , kids[1])

arbsFunc("saroj" , "raja" , "viper")

#kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

def kwargFunc(age, **kid):
    print("His last name is", kid["lname"], "and he is", age, "years old")

kwargFunc(fname="Tobias", lname="Refsnes", age=21)



def countrySystem (country) :
    print ("I am from "  + country + ".")

countrySystem("Sweden")
countrySystem("India")

countrySystem("Brazil")


# sum of 2 num   
def sumNum (num1 , num2) :
    return num1 + num2

result = sumNum(2 , 3)
print(result)

def multNum(num1 , num2) :
    return num1 * num2

result = multNum( 'h' , 10)
print(result)

def circle(r) :
     area = 3.14 * r * r
     circumference = 2 * 3.14 * r

     return area , circumference


area , circumference = circle(10)
print(area)
print(circumference)


cube_num = lambda x : x ** 30 

print(cube_num(3))
    

def factorial(num) :
    if num == 1 :
         return 1 
    else :
        return num * factorial(num - 1)
    

print(factorial(5))



