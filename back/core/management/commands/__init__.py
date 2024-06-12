#  coding: utf-8


from datetime import datetime
from random import randint, sample
from zoneinfo import ZoneInfo

from config import APPROVED, CLOTH_SIZES, FINISHED, MARITAL_STATUSES, PENDING, SHOE_SIZES, SOCIAL_PROGRAMS

ms_count = len(MARITAL_STATUSES)
sp_count = len(SOCIAL_PROGRAMS)
cs_count = len(CLOTH_SIZES)
ss_count = len(SHOE_SIZES)

ADMIN_DATA = {
    "first_name": "Isabela Dancini",
    "email": "isa.dancini@email.com",
    "username": "10000000000",
    "phone": "10000000000",
    "password": "admin"
}

BENEFICIARIES = [
    # PENDENTES PENDENTES PENDENTES PENDENTES PENDENTES
    # PENDENTES PENDENTES PENDENTES PENDENTES PENDENTES
    {
        "user": {
            "first_name": "Ana Clara Pereira Santos",
            "email": "ana.clara@email.com",
            "username": "00000000000",
            "phone": "00000000000",
            "password": "anaclara",
        },
        "birth_date": datetime(year=2000, month=2, day=2, tzinfo=ZoneInfo('UTC')),
        "child_count": 1,
        "monthly_familiar_income": 1000.00,
        "has_disablement": False,
        "approved": False,
        "city": "maringa",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Maria Clara",
                "birth_date": datetime(year=2023, month=11, day=11, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ]
    },
        {
        "user": {
            "first_name": "Joana Souza Oliveira Lima",
            "email": "joana.souza@email.com",
            "username": "00000000001",
            "phone": "00000000001",
            "password": "joanasouza",
        },
        "birth_date": datetime(year=2005, month=6, day=10, tzinfo=ZoneInfo('UTC')),
        "child_count": 2,
        "monthly_familiar_income": 1200.00,
        "has_disablement": False,
        "approved": False,
        "city": "sarandi",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Lucas Souza",
                "birth_date": datetime(year=2024, month=8, day=25, tzinfo=ZoneInfo('UTC')),
                "sex": "M"
            },
            {
                "name": "Beatriz Souza",
                "birth_date": datetime(year=2024, month=8, day=25, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ]
    },
    {
        "user": {
            "first_name": "Maria Oliveira Martins Kaur",
            "email": "maria.oliveira@email.com",
            "username": "00000000002",
            "phone": "00000000002",
            "password": "mariaoliveira",
        },
        "birth_date": datetime(year=1995, month=12, day=5, tzinfo=ZoneInfo('UTC')),
        "child_count": 1,
        "monthly_familiar_income": 800.00,
        "has_disablement": True,
        "approved": False,
        "city": "maringa",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Ana Oliveira",
                "birth_date": datetime(year=2022, month=12, day=10, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ]
    },
    # APROVADAS APROVADAS APROVADAS APROVADAS APROVADAS
    # APROVADAS APROVADAS APROVADAS APROVADAS APROVADAS
    {
        "user": {
            "first_name": "Carla Ferreira Almeida Müller",
            "email": "carla.ferreira@email.com",
            "username": "00000000003",
            "phone": "00000000003",
            "password": "carlaferreira",
        },
        "birth_date": datetime(year=2000, month=11, day=20, tzinfo=ZoneInfo('UTC')),
        "child_count": 3,
        "monthly_familiar_income": 1500.00,
        "has_disablement": False,
        "approved": True,
        "city": "umuarama",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Gabriel Ferreira",
                "birth_date": datetime(year=2012, month=9, day=5, tzinfo=ZoneInfo('UTC')),
                "sex": "M"
            },
            {
                "name": "Laura Ferreira",
                "birth_date": datetime(year=2017, month=2, day=28, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            },
            {
                "name": "Pedro Ferreira",
                "birth_date": datetime(year=2023, month=10, day=15, tzinfo=ZoneInfo('UTC')),
                "sex": "M"
            }
        ]
    },
    {
        "user": {
            "first_name": "Fernanda Costa Pereira",
            "email": "fernanda.costa@email.com",
            "username": "00000000004",
            "phone": "00000000004",
            "password": "fernandacosta",
        },
        "birth_date": datetime(year=1998, month=3, day=14, tzinfo=ZoneInfo('UTC')),
        "child_count": 1,
        "monthly_familiar_income": 900.00,
        "has_disablement": True,
        "approved": True,
        "city": "iguatemi",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Sofia Costa",
                "birth_date": datetime(year=2023, month=3, day=18, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ]
    },
    {
        "user": {
            "first_name": "Gabriela Santos Johansson",
            "email": "gabriela.santos@email.com",
            "username": "00000000005",
            "phone": "00000000005",
            "password": "gabrielasantos",
        },
        "birth_date": datetime(year=1990, month=7, day=25, tzinfo=ZoneInfo('UTC')),
        "child_count": 3,
        "monthly_familiar_income": 1500.00,
        "has_disablement": False,
        "approved": True,
        "city": "umuarama",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Lara Santos",
                "birth_date": datetime(year=2010, month=5, day=12, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            },
            {
                "name": "Matheus Santos",
                "birth_date": datetime(year=2022, month=9, day=20, tzinfo=ZoneInfo('UTC')),
                "sex": "M"
            },
            {
                "name": "Julia Santos",
                "birth_date": datetime(year=2024, month=2, day=28, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ]
    },
    {
        "user": {
            "first_name": "Mariana Kim Oliveira",
            "email": "mariana.oliveira@email.com",
            "username": "00000000006",
            "phone": "00000000006",
            "password": "marianaoliveira",
        },
        "birth_date": datetime(year=1985, month=4, day=18, tzinfo=ZoneInfo('UTC')),
        "child_count": 2,
        "monthly_familiar_income": 2000.00,
        "has_disablement": True,
        "approved": True,
        "city": "sarandi",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Pedro Oliveira",
                "birth_date": datetime(year=2010, month=10, day=5, tzinfo=ZoneInfo('UTC')),
                "sex": "M"
            },
            {
                "name": "Camila Oliveira",
                "birth_date": datetime(year=2024, month=12, day=25, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ]
    },
    {
        "user": {
            "first_name": "Carolina Lima Nguyen",
            "email": "carolina.lima@email.com",
            "username": "00000000007",
            "phone": "00000000007",
            "password": "carolinalima",
        },
        "birth_date": datetime(year=2001, month=9, day=10, tzinfo=ZoneInfo('UTC')),
        "child_count": 1,
        "monthly_familiar_income": 1200.00,
        "has_disablement": False,
        "approved": True,
        "city": "iguatemi",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Isabela Lima",
                "birth_date": datetime(year=2023, month=8, day=8, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ]
    }
]


SWAP_BENEFICIARIES = [
    {
        "user": {
            "first_name": "Sophia Muller Santos Pinheiro",
            "email": "sophia.muller@email.com",
            "username": "00000000008",
            "phone": "00000000008",
            "password": "sophiamuller",
        },
        "birth_date": datetime(year=1999, month=9, day=27, tzinfo=ZoneInfo('UTC')),
        "child_count": 2,
        "monthly_familiar_income": 1640.00,
        "has_disablement": True,
        "approved": True,
        "city": "maringa",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Pedro Muller Santos",
                "birth_date": datetime(year=2010, month=10, day=5, tzinfo=ZoneInfo('UTC')),
                "sex": "M"
            },
            {
                "name": "Camila Muller Pinheiro",
                "birth_date": datetime(year=2023, month=8, day=10, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ],
        "swap_data": {
            "cloth_size": CLOTH_SIZES[randint(0, cs_count - 1)],
            "description": "Camiseta de manga longa para o inverno",
            "status": PENDING,
        }
    },
        {
        "user": {
            "first_name": "Clara Dubois da Silva",
            "email": "clara.dubois@email.com",
            "username": "00000000011",
            "phone": "00000000011",
            "password": "claradubois",
        },
        "birth_date": datetime(year=2004, month=3, day=12, tzinfo=ZoneInfo('UTC')),
        "child_count": 1,
        "monthly_familiar_income": 0.00,
        "has_disablement": False,
        "approved": True,
        "city": "iguatemi",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Renata Dubois Costa",
                "birth_date": datetime(year=2024, month=2, day=22, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ],
        "swap_data": {
            "cloth_size": CLOTH_SIZES[randint(0, cs_count - 1)],
            "status": PENDING,
        }
    },
    {
        "user": {
            "first_name": "Andrea Yamamoto Santos Rodrigues",
            "email": "andrea.yamamoto@email.com",
            "username": "00000000009",
            "phone": "00000000009",
            "password": "andreayamamoto",
        },
        "birth_date": datetime(year=1993, month=5, day=7, tzinfo=ZoneInfo('UTC')),
        "child_count": 1,
        "monthly_familiar_income": 2536.00,
        "has_disablement": False,
        "approved": True,
        "city": "sarandi",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Rosa Yamamoto Santos",
                "birth_date": datetime(year=2023, month=7, day=11, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ],
        "swap_data": {
            "cloth_size": CLOTH_SIZES[randint(0, cs_count - 1)],
            "shoe_size": SHOE_SIZES[randint(0, ss_count - 1)],
            "description": "Blusa para o inverno e sapatinhos pra sair",
            "status": APPROVED,
        }
    },
    {
        "user": {
            "first_name": "Gabriela Dubois Costa Silva",
            "email": "gabriela.dubois@email.com",
            "username": "00000000010",
            "phone": "00000000010",
            "password": "gabrieladubois",
        },
        "birth_date": datetime(year=2006, month=7, day=7, tzinfo=ZoneInfo('UTC')),
        "child_count": 1,
        "monthly_familiar_income": 2536.00,
        "has_disablement": False,
        "approved": True,
        "city": "sarandi",
        "marital_status": MARITAL_STATUSES[randint(0, ms_count - 1)],
        "social_programs": sample(SOCIAL_PROGRAMS, randint(1, sp_count)),
        "children_data": [
            {
                "name": "Valentina Dubois Costa",
                "birth_date": datetime(year=2024, month=1, day=15, tzinfo=ZoneInfo('UTC')),
                "sex": "F"
            }
        ],
        "swap_data": {
            "cloth_size": CLOTH_SIZES[randint(0, cs_count - 1)],
            "shoe_size": SHOE_SIZES[randint(0, ss_count - 1)],
            "description": "Com 3 meses já perdeu quase todas as roupinhas!! Precisamos de roupinhas para ir à igreja",
            "status": FINISHED,
        }
    },
]
