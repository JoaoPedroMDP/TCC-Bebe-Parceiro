#  coding: utf-8
from django.urls import reverse


def create_access_code(client, prefix: str = "TES"):
    url = reverse('gen_access_codes')
    data = {'prefix': prefix}
    response = client.post(url, data=data)
    return response
