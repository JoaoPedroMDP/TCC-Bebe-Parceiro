#  coding: utf-8
from datetime import timedelta
import logging
from typing import List

from config import MANAGE_EVALUATIONS
from core.cqrs.commands.user_commands import CreateUserCommand, PatchUserCommand
from core.cqrs.commands.volunteer_commands import CreateVolunteerCommand, PatchVolunteerCommand, \
    DeleteVolunteerCommand
from core.cqrs.queries.volunteer_queries import GetVolunteerQuery, GetVolunteersReportQuery, ListVolunteerQuery
from core.models import Volunteer
from core.repositories.city_repository import CityRepository
from core.repositories.volunteer_repository import VolunteerRepository
from core.services import CrudService
from core.services.user_service import UserService

lgr = logging.getLogger(__name__)


class VolunteerService(CrudService):
    @classmethod
    def create(cls, command: CreateVolunteerCommand) -> Volunteer:
        # Verifica se a cidade passada é válida
        city = CityRepository.get(command.city_id)
        new_user = UserService.create(CreateUserCommand.from_dict(command.to_dict()))

        try:
            new_volunteer = Volunteer()
            new_volunteer = VolunteerRepository.fill(command.to_dict(), new_volunteer)
            new_volunteer.user = new_user
            new_volunteer.city = city

            # Para cada group_id passado, atribui o cargo
            for g_id in command.group_ids:
                new_volunteer.user.groups.add(g_id)

            new_volunteer.save()
        except Exception as e:
            new_user.delete()
            raise e

        return new_volunteer

    @classmethod
    def patch(cls, command: PatchVolunteerCommand) -> Volunteer:
        volunteer: Volunteer = VolunteerRepository.get(command.id)

        # Para cada group_id passado, remove o cargo atual e atribui um novo
        volunteer.user.groups.clear()
        for g_id in command.group_ids:
            volunteer.user.groups.add(g_id)

        if command.user_data:
            user_command = PatchUserCommand.from_dict({
                **command.user_data,
                'id': volunteer.user.id
            })
            UserService.patch(user_command)
        return VolunteerRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListVolunteerQuery) -> List[Volunteer]:
        if query.group_ids:
            return VolunteerRepository.filter(user__groups__id__in=query.group_ids)

        return VolunteerRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetVolunteerQuery) -> Volunteer:
        return VolunteerRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteVolunteerCommand) -> bool:
        return VolunteerRepository.delete(command.id)

    @classmethod
    def get_evaluators(cls) -> List[Volunteer]:
        return VolunteerRepository.filter(user__groups__name=MANAGE_EVALUATIONS)

    @classmethod
    def get_reports(cls, query: GetVolunteersReportQuery):
        filters = {}
        if query.start_date:
            filters['created_at__gte'] = query.start_date
        
        if query.end_date:
            filters['created_at__lte'] = query.end_date + timedelta(days=1)

        return VolunteerRepository.filter(**filters)