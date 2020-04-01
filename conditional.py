x=input('enter a number:')
if int(x)%2==0:
    print('the number is even')
else:
    print('the number is odd')
try:
    int(x)%2==0
    print('the number is even and it is divided by 2')
except:
    print('the number is odd and it is not divided by 2')
