#Задача 26:  
#Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def power(A, B):
    if B == 0:
        return 1
    else:
        return A * power(A, B-1)
    
print(power(int(input("N1: ")), int(input("N2: ")))) 
