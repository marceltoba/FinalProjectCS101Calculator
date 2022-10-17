import math

print("WELCOME TO MARCULATOR")
answer="Yes"
first_number=int(input("First number : "))
while answer=="Yes":
    operation=input("+/-/:/x/!/^/^- : ")
    if operation=="+":
        second_number=int(input("Second Number : "))
        first_number+=second_number
        print(first_number)
    elif operation=="-":
        second_number=int(input("Second Number : "))
        first_number-=second_number
        print(first_number)
    elif operation=="x":
        second_number=int(input("Second Number : "))
        first_number*=second_number
        print(first_number)
    elif operation==":":
        second_number=int(input("Second Number : "))
        first_number/=second_number
        print(first_number)
    elif operation=="!":
        def factorial(input_number):
            if(input_number==1 or input_number==0):
                return 1
            else:
                return (input_number*factorial(input_number-1))
        first_number=factorial(first_number)
        print(first_number)
    elif operation=="^":
        second_number=int(input("Second Number : "))
        first_number**=second_number
        print(first_number)
    elif operation=="^-":
        second_number=int(input("Second Number : "))
        first_number**=(1/second_number)
        print(math.ceil(first_number))
    else:
        print("Please type according to the example")
    answer=input("Want to continue : ").capitalize()
    if(answer!="No" or answer!="Yes"):
        print("Please answer yes or no!")
        continue
    else:
        continue
print("YOUR FINAL ANSWER IS : "+str(first_number))