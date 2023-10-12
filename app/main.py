from typing import List, Union


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife: Union[None, "Person"] = None
        self.husband: Union[None, "Person"] = None
        Person.people[name] = self


def create_person_list(people: List[dict]) -> List[Person]:
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people.get(person_dict["wife"])
            if person.wife:
                person.wife.husband = person
        if 'husband' in person_dict and person_dict["husband"]:
            person.husband = Person.people.get(person_dict["husband"])
            if person.husband:
                person.husband.wife = person
        person_list.append(person)
    return person_list
