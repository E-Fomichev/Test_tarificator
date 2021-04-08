import requests
import const
import json_data

def car_change():
    """Отправить/отредактировать информацию об автомобиле"""

    objects = []
    headers = {'Authorization': const.token}
    options = '/own/'
    json = json_data.json_auto_details

    req = requests.post(const.base_url + const.vehicles + const.uid + options + const.vid,
                        headers=headers,
                        json=json)
    objects.append(req)

    assert 201 == req.status_code
    print(req.json())
    print(objects)