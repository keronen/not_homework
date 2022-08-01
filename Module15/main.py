empl_ID = []

number = int(input('please enter a  numbers of employes: '))

for _ in range(number):
 id = int(input('please enter an ID of employe: '))
 empl_ID.append(id)

print(empl_ID)

while True:
 id = int(input('please enter an ID of employe we search: '))
 for i in empl_ID:
  if i == id:
   print('he is on office')
   break
 else:
  print('he is out office')


