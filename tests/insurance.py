import const
import json_data
import requests


def test_get_poffers_parking():
    """Расчет стоимости парковки"""

    objects = []
    dop_url = 'parking'
    params = {'vid': const.vid, 'lifetime': '60', 'type': 'garage', 'lat': '11.1', 'lon': '12.2'}
    headers = {'Authorization': const.token}

    req = requests.get(const.base_url + const.poffers + const.uid + '/' + dop_url,
                       headers=headers,
                       params=params)
    objects.append(req)
    data = req.json()

    assert 200 == req.status_code
    # print(req.json())
    # print(objects)
    print(str(data[0]['policy']['cost']['value']))


def test_get_poffers_package():
    """Расчет стоимости пакета км"""

    objects = []
    dop_url = 'package'
    params = {'vid': const.vid, 'dist': '100', 'dist_units': 'km', 'shared': 'true'}
    headers = {'Authorization': const.token}

    req = requests.get(const.base_url + const.poffers + const.uid + '/' + dop_url,
                       headers=headers,
                       params=params)
    objects.append(req)
    data = req.json()

    assert 200 == req.status_code
    # print(req.json())
    # print(objects)
    print(str(data[0]['policy']['cost']['value']))

def test_post_poffers_ride():
    """Расчет стоимости поездки"""

    objects = []
    dop_url = 'ride'
    headers = {'Authorization': const.token, 'Content-Type': 'application/json'}

    json = json_data.json_ride
    req = requests.post(const.base_url + const.poffers + const.uid + '/' + dop_url,
                        headers=headers,
                        json=json)
    objects.append(req)
    data = req.json()

    assert 200 == req.status_code
    # print(req.json())
    # print(objects)
    print(str(data[0]['policy']['cost']['value']))
