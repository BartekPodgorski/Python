import json
import datetime
# Prosze o wpisanie sciezki do pliku
with open("C:/Users/user/Desktop/Python_Main/Python/obiekt/Rekrut/persons.json", encoding="UTF-8") as file:
    persons = json.load(file)


# oczyszczanie telefonu


def prepare_phone(tel):
    alphanumeric = ""
    for char in tel:
        if char.isnumeric():
            alphanumeric += char

    return alphanumeric


for person in persons['results']:
    person["phone"] = prepare_phone(person["phone"])

# usuwanie picture
for person in persons['results']:
    del person['picture']
# data


def day_left_birthday(date):
    birth = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    today = datetime.date.today()
    try:
        if(today.month == birth.month and today.day >= birth.day or today.month > birth.month):
            nextBirthdayYear = today.year + 1
        else:
            nextBirthdayYear = today.year
        nextBirthday = datetime.date(nextBirthdayYear, birth.month, birth.day)
        diff = nextBirthday - today
        return diff.days
    except ValueError:  # Przypadek na 29.02
        birthDayLeap = 1
        birthMonthLeap = 3
        nextBirthdayLeap = datetime.date(
            today.year + 1, birthMonthLeap, birthDayLeap)
        diffLeap = nextBirthdayLeap - today
        return diffLeap.days


for person in persons['results']:
    date = person['dob']['date']
    toBirthday = day_left_birthday(date)
    temporaryDict = {"Days_to_birthday": toBirthday}
    person.update(temporaryDict)
