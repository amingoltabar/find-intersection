def intersect(array_1,array_2):#This function receives 2 lists and creates a new list with their intersect elements.Then returns the new list.
    my_list=[]
    for i in range(5):
        for j in range(4):
            if array_1[i]==array_2[j]:
                my_list.append(array_1[i])
    return my_list
def delete_repeated_numbers(array):#This function receives a list and deletes the repeated elements.Then returns the new list.
    my_list=[]
    size=len(array)
    for i in range(size):
        count=0
        for j in range(size):
            if array[i]==array[j]:
                count+=1
        if count==1:
            my_list.append(array[i])
    return my_list
def receive():#Function for inputting integer
    count=0
    while count==0:
        a=input('Enter the integer :')
        try:
            val=int(a)
            count+=1
            return val
        except ValueError:
            try:
                val=float(a)
                print('You entered a float. ')
            except ValueError:
                print('You did not enter a number. ')
first_list=[]
print('Creating the first list')
while len(first_list)<7: #creating the first list
    first_list.append(receive())
second_list=[]
print('Creating the second list')
while len(second_list)<7: #creating the second list
    second_list.append(receive())
my_list=[]
my_list=intersect(first_list,second_list)
my_list=delete_repeated_numbers(my_list)
if len(my_list)==0:
    print('The lists you have entered do not have intersection.')
elif len(my_list)==1:
    print('Intersect number:',my_list)
else:
    print('Intersect numbers:',my_list)
   
        
    
            
        

    
    
    
    
