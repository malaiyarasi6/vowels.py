input_string=input("enter a string:")
input_string=input_string.casefold()
vowels="aeiou"
vowelsdata={}.fromkeys(vowels,0)
totalvowelscount=0
for character in input_string:
    if  character in vowels:
        vowelsdata[character]+=1
        totalvowelscount+=1
print(totalvowelscount)
for vowels in vowelsdata:
    print(vowels,"==>",vowelsdata[vowels]) 

               

