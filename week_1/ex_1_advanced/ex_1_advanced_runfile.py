#references 1
# Open a file in read mode
file_path_1 = 'references_1.txt'
with open(file_path_1, 'r', encoding='utf8') as file:
    lines = file.readlines()
#cleaning up the list
for i in range (len(lines)):
    lines[i]=lines[i].replace('\n','') #remove line breaks
    lines[i]=lines[i][3:] #remove the number before the reference
    lines[i]=lines[i].replace(' ','') #remove whitespaces
# Iterate through the list using enumerate to create a dictionary
my_dict = {str(index+1): value for index, value in enumerate(lines)}
print('Here is the dictionnary for reference_1.txt'+str(my_dict))

#references_2
file_path_2 = 'references_2.txt'
with open(file_path_2, 'r', encoding='utf8') as file:
    lines2 = file.readlines()
#cleaning up the list
for i in range (len(lines2)):
    lines2[i]=lines2[i].replace('\n','') #remove line breaks
    lines2[i]=lines2[i][3:] #remove the number before the reference
    lines2[i]=lines2[i].replace(' ','') #remove whitespaces
# Iterate through the list using enumerate to create a dictionary
my_dict2 = {str(index+1): value for index, value in enumerate(lines2)}
print('Here is the dictionnary for reference_2.txt'+str(my_dict2))

#status dictionnary
status={key:'' for key in range(1,61)}

#comparison of the dictionnaries
for i in range (60):
    if lines[i]==lines2[i]:
        status[i]='good'
    else:
        status[i]='mismatch detected'
print(status)










