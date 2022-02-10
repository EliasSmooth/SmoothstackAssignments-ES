#Six is a Mob
people = ["John", "Jimmy", "Johnson", "Quandingle", "Harry", "Jessica"]

def check(list):
    amount = len(list)
    if amount > 5:
        print('There is a mob in the room')
    elif amount >= 3 <= 5:
        print('This room is crowded')
    elif amount >=1 <= 2:
        print('This room is not crowded')
    elif amount == 0: 
        print('This room is empty')

check(people)
people.pop()

check(people)
people.pop()
people.pop()
people.pop()

check(people)
people.pop()
people.pop()

check(people)