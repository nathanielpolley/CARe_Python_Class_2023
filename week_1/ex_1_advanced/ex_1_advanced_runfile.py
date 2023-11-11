#YOUR CODE FOR EX_1 ADVANCED HERE
def str_sup(file_name, str_suppressed):
    with open(file_name,'r', encoding='utf-8') as file:
        content= file.read()
    content= content.replace(str_suppressed,'')
    with open(file_name,'w', encoding='utf-8') as file:
        file.write(content)
    return f"string {str_suppressed} was removed from {file_name}"

file_name1= "references_1.txt"
file_name2= "references_2.txt"
str_space= " "
ref1= str_sup(file_name1, str_space)
ref2= str_sup(file_name2,str_space)
print(ref1)
print(ref2)
