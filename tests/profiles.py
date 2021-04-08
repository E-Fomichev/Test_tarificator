import requests
import const
import json_data


def profiles_prepare():
    """Изменение данных пользователя"""

    objects = []
    headers = {'Authorization': const.token}
    options = 'requests/'
    options_2 = '/prepare'
    json = json_data.json_person

    req = requests.post(const.base_url + const.profiles + options + const.uid + options_2,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)

def profiles_accept_prepared():
    """подтверждение изменений"""

    objects = []
    headers = {'Authorization': const.token}
    options = 'requests/'
    options_2 = '/accept_prepared'
    json = json_data.json_person

    req = requests.post(const.base_url + const.profiles + options + const.uid + options_2,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)