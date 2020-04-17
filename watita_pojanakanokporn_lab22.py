
import os

outfile = open('numbers.txt', 'w')
    
for num in range(1, 11):
    outfile.write(str(num) + '\n')
    
outfile.close()

outfile = open('numbers.txt', 'r')

total = 0
for num in outfile:
    total += int(num)
    print(num)   
print(total) 

outfile.close()

outfile = open('numbers.txt', 'a')
for num in range(11, 21):
    outfile.write(str(num) + '\n')      
outfile.close()

tempfile = open('temp.txt', 'w')
outfile = open('numbers.txt', 'r')

for num in outfile:
    if int(num) < 16 or int(num) > 18:
        
    if int(num) == 10:
        tempfile.write(str(50) + '\n')
    else:    
        tempfile.write(str(num))

tempfile.close()
outfile.close()

os.remove('numbers.txt')
os.rename('temp.txt', 'numbers.txt')
