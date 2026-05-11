def print_info(data, indent=0):
    for key, value in data.items():
        print('  ' * indent + f"{key}: ", end="")
        if isinstance(value, dict):
            print()
            print_info(value, indent + 1)
        else:
            print(value)

person_info = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345"
    },
    "contact": {
        "email": "john.doe@example.com",
        "phone": {
            "home": "555-1234",
            "work": "555-5678"
        }
    }
}

print_info(person_info)