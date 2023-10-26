microbial_pop_count = [100, 200, 150, 300, 50] #we create our variable that fits our list

for day, count in enumerate(microbial_pop_count, start=1): #we assiciate each day with a variable of our list which is the pop growth
    print(f'day {day}: {count}')

    if count >= 200: #each day we have more cell but when it reaches 200 we want the script to print the day associated to this overcome
        print(f'Day it reaches 200: {day}')

total = sum(microbial_pop_count) #standard calculus
print('average', total / 5)
print('min', min(microbial_pop_count))
print('max', max(microbial_pop_count))

