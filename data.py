import requests


my_params = {
    'amount':10,
    
    'type': 'boolean'   
}


response = requests.get('https://opentdb.com/api.php', params=my_params)
response.raise_for_status()


question_data = response.json()['results']



# type hint


def  police_check(age: int)-> bool:
    if age > 19:
        can_drive = True

    else:
        can_drive = False

    return can_drive



if police_check(12):
    print("he can pass")