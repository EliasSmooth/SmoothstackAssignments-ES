#Three is a Crowd PT.2
people = ["John", "Jimmy", "Johnson", "Quandingle"]

def check(list):
    amount = len(list)
    if amount > 3:
        print('Three is a crowd')
    else:
        print('This room is spacious')


check(people)
people.pop()

check(people)