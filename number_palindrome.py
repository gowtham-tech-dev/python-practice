number=int(input("type the number: "))
#using String concept
if str(number)==str(number)[::-1]:
    print("number is palindrome")
else:
    print("number is not a palindrome")

#using logic
Actual=number
reverse=0

while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
    
if Actual==reverse:
    print("number is palindrome")
else:
    print("number is not a palindrome")