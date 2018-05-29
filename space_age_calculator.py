def print_header():
    print('----------------------------------------')
    print('         SPACE AGE CALCULATOR')
    print('----------------------------------------')


def calculate_age_on_earth(age):
    return int(age/31557600)


print_header()

age = int(input('Enter your age in seconds: '))
print(calculate_age_on_earth(age))
