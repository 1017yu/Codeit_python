def hello(name):    # parameter를 통한 function 만들기
    print("Hello!")
    print(name)
    print("Welcome to Codeit!")

hello("Kled")

#################################################################################################

def print_sum(a, b, c):    # 여러 개의 parameter를 통한 sum function
    print(a + b + c)

print_sum(7, 3, 10)

##################################################################################################

def print_square(a):
    return(a*a)

y = (print_square(3))

print(y + y)


