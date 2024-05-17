#  coding: utf-8
from typing import List

from core.cqrs.commands.user_commands import CreateUserCommand, PatchUserCommand, DeleteUserCommand
from core.cqrs.queries.user_queries import ListUserQuery, GetUserQuery
from core.models import User
from core.repositories.user_repository import UserRepository
from core.services import CrudService


class UserService(CrudService):
    @classmethod
    def create(cls, command: CreateUserCommand) -> User:
        data = command.to_dict()
        data["username"] = data["phone"]

        new_state = UserRepository.create(data)
        return new_state

    @classmethod
    def patch(cls, command: PatchUserCommand) -> User:
        data = command.to_dict()
        if data.get("phone"):
            data["username"] = data["phone"]

        password = data.get("password")
        user: User = UserRepository.patch(data)
        if password:
            user.set_password(password)
            user.save()

        return user

    @classmethod
    def filter(cls, query: ListUserQuery) -> List[User]:
        return UserRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetUserQuery) -> User:
        return UserRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteUserCommand) -> bool:
        return UserRepository.delete(command.id)
