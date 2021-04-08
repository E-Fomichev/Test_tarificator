import const

json_person = {
    "documents": {
        "id": {
            "date_of_birth": "1989-01-01",
            "first_name": "Челик",
            "gender": "male",
            "given_name": "Петр",
            "number": "123456",
            "second_name": "Петр",
            "series": "1234"
        },
        "license": {
            "issue_date": "2010-01-01",
            "number": "5640244242",
            "type": "russia2019"
        },
        "registration": {
            "authority_code": "644454",
            "city": "Санкт-Петербург",
            "country": "Россия",
            "date": "2015-01-01",
            "house": "546",
            "locality": "Санкт-Петербург",
            "region": "Ленинградская область",
            "street": "салова"
        },
        "type": "russia2020-08-26"
    },
    "source": "manual"
}

json_auto_details = {
    "year": 2015,
    "plate": {
        "value": "в666ор77",
        "type": "russia93"
    },
    "model": "A3",
    "make": "Audi"
}

json_ride = {
    "vehicle_id": const.vid,
    "points": [
        {
            "lon": "30.3126114",
            "lat": "59.8613777"
        },
        {
            "lon": "30.3326116",
            "lat": "59.852839"
        },
        {
            "lon": "30.3432981",
            "lat": "59.856495"
        }
    ]
}