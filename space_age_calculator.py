def print_header():
    print('----------------------------------------')
    print('         SPACE AGE CALCULATOR')
    print('----------------------------------------')


def calculate_age_on_earth(age):
    return int(age/31557600)

def calculate_age_on_mercury(age):
    return int(calculate_age_on_earth(age)*0.2408467)

# Program Start

print_header()

age = int(input('Enter your age in seconds: '))

print('Do you want your age on: ')
print('1. Earth')
print('2. Mercury')
response = input('Please enter the corresponding number: ')

if response is '1': print(calculate_age_on_earth(age))
if response is '2': print(calculate_age_on_mercury(age))
