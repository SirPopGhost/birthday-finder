import json
import datetime
from send_sms import send_sms


def read_from_file(input_file):
    with open(input_file) as file:
        data_file = file.read()
        json_file = json.loads(data_file)
        return json_file


def birthday_match(current_day, birth_file):
    bday_list = []
    for comparing in birth_file:
        if current_day == comparing.get("birthdate"):
            bday_match_name = comparing.get("name")
            bday_phone = comparing.get("phone_number")
            name_phone_set = [bday_match_name, bday_phone]
            bday_list.append(name_phone_set)
    return bday_list

def main():
    birth_dates = "/Users/OwnerSri/storage/birthday-finder/db/datafile_birthdays.json"
    birth_file = read_from_file(birth_dates)
    current_time = datetime.datetime.now()
    print(birth_file)
    month = str(current_time.month)
    day = str(current_time.day)
    current_day = month + "-" + day
    a = birthday_match(current_day, birth_file)
    send_sms(a)


main()

"""
Import a different file to a different directory."
"""
