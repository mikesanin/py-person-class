class Person:
    people = {}

def __init__(self, name, age):
    self.name = name
    self.age = age
    self.wife = None
    self.husband = None
    Person.people[name] = self

def create_person_list(people: list) -> list:
    person_list = []
    for people_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        if "wife" in person_dict and person_dict["husband"]:
            person.husband = Person.people.get(person_dict["husband"])
            person.husband.wife = person
        person_list.append(person)
    return person_list
