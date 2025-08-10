import time

# if you want to create decorator then yo have to create a function inside another function 


def timer(func) :
    def wrapper(*args ,**kwargs  ) :
        start = time.time()
        result = func(*args , **kwargs )
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer   #----> it is a decorator , means when we declare this it works like a tool gate so all the function will go through this 
def example_function(n) :
    time.sleep(n)
    print("Hello")

example_function(1)    