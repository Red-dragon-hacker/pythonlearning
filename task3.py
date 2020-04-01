a=input('enter the first number:')
b=input('enter the second number:')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
x=input('enter your choice:')
try:
    if int(x)>4:
        print('INVALID PLEASE ENTER THE VALID CHOICE')
    if int(x)<=0:
        print('INVALID')
    else:
        if int(x)==1:
            try:
                sum=int(a)+int(b)
                print(sum)
            except:
                print(' INVALID PLEASE ENTER ANY NUMBER')
        elif int(x)==2:
            try:
                sum=int(a)-int(b)
                print(sum)
            except:
                print('INVALID PLEASE ENTER ANY NUMBER')
        elif int(x)==3:
            try:
                sum=int(a)*int(b)
                print(sum)
            except:
                    print('INVALID PLEASE ENTER ANY NUMBER')
        elif int(x)==4:
                try:
                    if int(b)==0:
                        print('infinity')
                    else:
                        sum=int(a)/int(b)
                        print(sum)
                except:
                    print("INVALID PLEASE ENTER ANY NUMBER")
except:
    print("INVALID   ")
