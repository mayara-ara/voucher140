#29. Crie um programa que calcule o menor número divisível por cada um dos números de 1 a 20? 
#Ex: 2520 e o menor número que pode ser dividido por cada um dos números de 1 a 10, sem 
#sobrar resto
import math


result = 1

for number in range(1, 21):
    
    result = abs(result * number) // math.gcd(result, number)

print(f"O menor número divisível por cada um dos números de 1 a 20 é: {result}")
