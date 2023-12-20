#  coding: utf-8

def default_beneficiary_data(marital_status_id: int, city_id: int, access_code: str):
    return {
        "name": "TCCB",
        "birth_date": "2023-01-01",
        "child_count": 3,
        "email": "TCCB@email.com",
        "has_disablement": True,
        "marital_status_id": marital_status_id,
        "monthly_familiar_income": 1234,
        "password": "123456",
        "phone": "4495263859",
        "city_id": city_id,
        "access_code": access_code,
        "socialProgram": [],
        "children": [
            {
                "name": "João ",
                "birth_date": "2023-01-01",
                "sex": "Masculino"
            },
            {
                "name": "Maria",
                "birth_date": "2023-02-02",
                "sex": "Feminino"
            }
        ]
    }
