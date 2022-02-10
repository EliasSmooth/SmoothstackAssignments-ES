#Three is a Crowd

people = ["John", "Jimmy", "Johnson", "Quandingle"]

def check(list):
    amount = len(list)
    if amount > 3:
        print('Three is a crowd')

check(people)
people.pop()

check(people)
