
## Function with arguments
def goodDay(name, ending):
    print("Good Day!"+ name)
    print(ending)

goodDay(" Atul", "Thank you!")
goodDay(" Atul", "Thank you!")
goodDay(" Atul", "Thank you!")



## function in return value or elements
def goodDay(name, ending):
    print("Good Day!"+ name)
    print(ending)
    return "ok"

a= goodDay(" Atul", "Thank you!")
print(a)