#!/usr/bin/python3
import re
# taking binary data
print("enter binary data")
binary_string=input()
#print(string)
count = 0
#finding length of string
l=len(binary_string)
for i in range(0,l):
    if binary_string[i]=='1':     #counting number of 1's
        count+=1
#parity checking
if count%2==1:
    print("odd")    
    binary_string += '0'
else:
    binary_string += '1'

#printing binary data after parity check
print("Parity bit data :"+binary_string)
sub_string='010'

#finding indices after checking '010'
match_index = [k.start() for k in re.finditer(sub_string,binary_string)]

#convert string to list
list_string=list(binary_string)
for x in match_index:
    list_string[x+len(sub_string):x+len(sub_string)]='0'


#print(match_index)
#print(list_string)

#convet list to string
transmit_string=''.join(map(str,list_string))
print(transmit_string)
transmit_string+='0101'
#printing binary data after parity check
print("Transmitting data:"+transmit_string)