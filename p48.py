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
first_list=[]
second_list=[]
for i in range(5):
    first_list.append(int(input('Create your first list.Enter the number: ')))
for i in range(4):
    second_list.append(int(input('Create your second list.Enter the number: ')))
my_list=intersect(first_list,second_list)
my_list=delete_repeated_numbers(my_list)
if len(my_list)==0:
    print('The lists you have entered do not have intersection.')
elif len(my_list)==1:
    print('Intersect number:',my_list)
else:
    print('Intersect numbers:',my_list)
   
        
    
            
        

    
    
    
    
