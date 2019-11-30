import random


print("Hello World")

def get_random_number():  # Get random number
    answer = random.randint(1,3)
    return answer

answer = get_random_number() 

print(answer)

username="David"
print(f"Hello {username}")
companies = ["Constant Contact","Redhat","BAE"]
if answer==1:
    print(f"{companies[answer-1]}\n")
elif answer==2:
    print(f"{companies[answer-1]}\n")
elif answer==3:
    print(f"{companies[answer-1]}\n")

print("That is your answer")

companies.append("Not Raytheon")

finalValue=len(companies)-1

print(companies[finalValue])


class Person:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def run(self):
        print(f"Run {self.name} Run!")

class Father(Person):
    pass


david=Father("David","male")

print(david.name)
print(david.sex)
david.run()


jobs = {
    'll': 'MIT Lincoln Labs',
    'cc': 'Constant Contact',
    'rh': 'Red Hat',
    'bae': 'BAE',
    'ca': 'Collins Aerospace'
}

print(jobs['rh'])

print(f"Length of Jobs: {len(jobs)}")

print ('ray' in jobs)

print ('ca' in jobs)


for idx in jobs:
    print(f'jobs[idx]')

