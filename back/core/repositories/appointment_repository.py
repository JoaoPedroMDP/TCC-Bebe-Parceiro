#  coding: utf-8
from core.models import Appointment
from core.repositories import Repository


class AppointmentRepository(Repository):
    model = Appointment
