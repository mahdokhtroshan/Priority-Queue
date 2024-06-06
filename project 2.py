class Person:
    def __init__(self,name, age, skill):
        self.name = name 
        self.age = age
        self.skill = skill

    def __lt__(self, other):
        if self.skill != other.skill:
            return self.skill < other.skill
        else:
            return self.age < other.age

class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def Add(self, name , age , skill):
        person = Person(name, age, skill)
        self.queue.append(person)
        self.queue.sort(key= lambda x: x.skill)
        

    def BestPerson(self):
        return self.queue.pop(0)

    def Find(self, person):
        for x in self.queue:
            if x == person:
                return x
        return None

    def Update(self, person, newskill):
        for x in self.queue:
            if x == person:
                x.skill = newskill
                self.queue.sort(key=lambda x : x.skill)
            break
                 
             


queue = PriorityQueue()
while True:
        print("options:")
        print("1. Add a new person")
        print("2. Get the best person")
        print("3. Update a person's skill level")
        print("4. Exit")

        choice = int(input("what would you like to do ? "))
        if choice == 1 :
            name = input("Enter the person's name : ")
            age = int(input("Enter the person's age :"))
            skill = input("Enter the person's skill: ") 
            person = Person(name, age, skill)
            queue.Add(name, age, skill)
            
        
        #elif choice == 2:
           #bestperson = queue.Pop()
           #print("The best person is :")
        #elif choice == 3:
            
            
        #elif choice == 4:
            #break
        #else:
            #print("Please try again{bestperson.name} + {bestperson.age} + {bestperson.skill}")