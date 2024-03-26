#  coding: utf-8
import logging

import pytest
from django.contrib.auth.models import Group
from django.db.models.base import ModelBase
from django.test.client import Client
from django.urls import reverse

from core.models import User
from factories import AccessCodeFactory


lgr = logging.getLogger(__name__)


@pytest.mark.django_db
def test_can_list_all_access_codes(client: Client, django_user_model: ModelBase):
    codes = AccessCodeFactory.create_batch(size=5)
    
    group = Group.objects.filter(name="manage_access_codes").first()
    lgr.debug(type(django_user_model))
    ac_user = django_user_model.objects.create_user(username="ac_user", password="ac_user")
    ac_user.groups.add(group)
    
    client.force_login(ac_user)
    
    url = reverse("gen_access_codes")
    response = client.get(url)
    lgr.debug(response.data)
    assert response.status_code == 200
    assert len(response.data) == len(codes)
