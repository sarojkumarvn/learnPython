def myFunction (user , age ) :
    print ("Hello", user )
    print ("You are", age , "years old")

# myFunction("Saroj" , 21)



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