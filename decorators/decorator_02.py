import time
# debug works like a wrapper which will give us the start and end time 
def debug(func) :
    def wrapper(*args , **kwargs) :
        # start = time.time() #starting time
        args_value = ', '.join(str(arg) for arg in args )
        result = func(*args , **kwargs)  #result of this function 
        kwargs_value = ', '.join(f"{k} = {v}" for k , v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")

        # end = time.time() #Ending time
        # print(f"{func.__name__} takes time {end - start}")
        return result


    return wrapper


@debug
def hello(*args , **kwargs):
    print(*args , **kwargs)



hello("Hello" , "namaste")




@debug
def greet(name , greetings = "Hello") :
    print (f"{greetings} , {name}")


greet('saroj bhaiya' , greetings="Han ji")   