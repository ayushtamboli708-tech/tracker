
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

print(person)

if 'skills' in person:
    mid=person.get('skills')
    print(mid[(len(mid)-1)//2])
    if 'Python' in person.get('skills'):
        print("Python is in the skills list")