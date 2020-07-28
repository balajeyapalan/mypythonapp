
start_number = 2000
end_number = 3200
result = " "
while(start_number <= end_number):
    if(start_number % 7 == 0 ) and (start_number % 5 != 0 ):
        print(start_number,end=" ")
        #result = result+","+str(start_number)
    start_number = start_number + 1

#print("Numbers are divisible by 7 and not multiple of 5 :\n " , result[2:len(result)])

