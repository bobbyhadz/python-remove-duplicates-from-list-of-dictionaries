# Remove duplicates from a List of Dictionaries in Python

list_of_dictionaries = [
    {'id': 1, 'site': 'bobbyhadz.com'},
    {'id': 2, 'site': 'google.com'},
    {'id': 1, 'site': 'bobbyhadz.com'},
]

result = list(
    {
        dictionary['id']: dictionary
        for dictionary in list_of_dictionaries
    }.values()
)

# 👇️ [{'id': 1, 'site': 'bobbyhadz.com'}, {'id': 2, 'site': 'google.com'}]
print(result)