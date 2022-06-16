guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  val = None
  while True:
    if val is not None:
      line_data= val.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
  
    age = int(line_data[1])
    guests[name] = age
    val = yield name, age
    

names=read_guestlist('guest_list.txt')
#for tup in names:
 # print(tup[0])
for i in range(14):
  next(names)

names.send('Jane,35')

over_21= (key for key,value in guests.items() if int(value)>21)

for guest in over_21:
  print(guest)


def Chicken():
  Food = 'Chicken'
  Table = 1
  for i in range(5):
    seat=i+1
    yield f'{Food}',f'Table: {Table}',f'Seat: {seat}'

def Beef():
  Food = 'Beef'
  Table = 2
  for i in range(5):
    seat = i+1
    yield f'{Food}',f'Table: {Table}',f'Seat: {seat}'

def Fish():
  Food = 'Fish'
  Table = 3
  for i in range(5):
    seat = i+1
    yield f'{Food}',f'Table: {Table}',f'Seat: {seat}'

def meal_assign(guests,gen1,gen2,gen3):
  people = list(guests.keys())
  for i in range(5):
    yield (people[i],next(gen1))
  for i in range(5):
    g= i +5
    yield (people[g],next(gen2))
  for i in range(5):
    g = i + 10
    yield (people[g],next(gen3))

guests_w_meal = meal_assign(guests,Chicken(),Beef(),Fish())

for guests in guests_w_meal:
  print(guests)
