#list of microbial population counts
MPC=[]
print('enter your values from day 1 to day 5')
for i in range (5):
    nombre=int(input(' :'))
    MPC.append(nombre)
print(MPC)

#Average population count
average=0
for i in MPC:
    average=average+i
average=average/5
print('The average is '+ str(average))

#Maximum population count
maximum=0
for i in MPC:
    if i>= maximum:
        maximum=i
print('The maximum is '+ str(maximum))

#Minimum population count
minimum = MPC[0]
for i in MPC:
    if i<=minimum:
        minimum=i
print('The minimum is '+str(minimum))

#days when >200
for i in MPC:
    if i>=200:
        print(f'The population is >= 200 on day {i}')




