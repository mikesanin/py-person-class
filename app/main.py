from typing import List, Optional


class Person:
    people: dict[str, "Person"] = {}


    def __init__(
        self,
        name: str,
        age: int,
        spouse: Optional["Person"] = None
    ) -> None:
        self.name: str = name
        self.age: int = age
        self.spouse: Optional["Person"] = spouse
        Person.people[name] = self


def create_person_list(people: List[dict]) -> List[Person]:
    person_list: List[Person] = []

    for person_data in people:
        name: str = person_data["name"]
        age: int = person_data["age"]
        spouse_name: str = (person_data.get("wife")
                            if "wife" in person_data
                            else person_data.get("husband"))

        spouse: Optional[Person] = Person.people.get(spouse_name)

        person: Person = Person(name, age, spouse)
        person_list.append(person)

        if spouse:
            if "wife" in person_data:
                person.wife = spouse
            else:
                person.husband = spouse

    return person_list
