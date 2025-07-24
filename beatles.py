beatles=[]
 
first_people = ['John Lennon','Paul McCartney','George Harrison']

for i in first_people:
    beatles.append(i)

second_batch = ['Stu Sutcliffe','Pete Best']

for i in range(2):
    user_input = input(f"Enter {second_batch[i]}: ")
    beatles.append(user_input)

for i in range(2):
    del beatles[-1]

beatles.insert(0,'Ringo Starr')
print(beatles)