from datetime import datetime

def print_header():
    print('----------------------------------------')
    print('         SPACE AGE CALCULATOR')
    print('----------------------------------------')


def calculate_rough_age_in_seconds(date):
    rough_age = (datetime.now() - date)
    return rough_age.total_seconds()


def calculate_age_on_earth(age):
    return age/31557600


def calculate_age_on_mercury(age):
    return int(calculate_age_on_earth(age)*0.2408467)


def calculate_age_on_venus(age):
    return int(calculate_age_on_earth(age)*0.61519726)


def calculate_age_on_mars (age):
    return int(calculate_age_on_earth(age)*1.8808158)


def calculate_age_on_jupiter(age):
    return int(calculate_age_on_earth(age)*11.862615)


def calculate_age_on_saturn(age):
    return int(calculate_age_on_earth(age)*29.447498)


def calculate_age_on_uranus(age):
    return int(calculate_age_on_earth(age)*84.016846)


def calculate_age_on_neptune(age):
    return int(calculate_age_on_earth(age)*164.79132)


def calculate_age_on_pluto(age):
    return int(calculate_age_on_earth(age)*248.00)


#------------------
# Program Start
#------------------

print_header()

age = int(input('Enter your age in seconds (if you don\'t know, like a normal person, enter 0): '))

if (age is 0):
    bday = input('Enter your birthday for a rough calculation (format:DD-MM-YYYY): ')
    bday = bday.split('-')
    age = calculate_rough_age_in_seconds(datetime(int(bday[2]), int(bday[1]), int(bday[0])))
print('Do you want your age on: ')
print('1. Earth')
print('2. Mercury')
print('3. Venus')
print('4. Mars')
print('5. Jupiter')
print('6. Saturn')
print('7. Uranus')
print('8. Neptune')
print('9. Pluto')
response = input('Please enter the corresponding number: ')

if response is '1': print(int(calculate_age_on_earth(age)))
if response is '2': print(calculate_age_on_mercury(age))
if response is '3': print(calculate_age_on_venus(age))
if response is '4': print(calculate_age_on_mars(age))
if response is '5': print(calculate_age_on_jupiter(age))
if response is '6': print(calculate_age_on_saturn(age))
if response is '7': print(calculate_age_on_uranus(age))
if response is '8': print(calculate_age_on_neptune(age))
if response is '9': print(calculate_age_on_pluto(age))
