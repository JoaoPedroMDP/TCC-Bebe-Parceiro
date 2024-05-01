#  coding: utf-8
from core.cqrs import Validator, Field, Command
from core.repositories.campaign_repository import CampaignRepository

# TODO: Validar se funciona
def check_for_duplicity(data: dict):
    conflicts = CampaignRepository.filter(name=data['name'])
    if len(conflicts) > 0:
        raise AssertionError(f"Campanha com o nome '{data['name']}' já cadastrada")


class CreateCampaignCommand(Command):
    fields = [
        Field("name", "string", True),
        Field("start_date", "string", True),
        Field("end_date", "string", True),
        Field("description", "string", True),
        Field("external_link", "string", False),
    ]

    def __init__(self, name: str, start_date: str, end_date: str, description: str, external_link: str = None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.external_link = external_link

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'CreateCampaignCommand':
        data = Validator.validate_and_extract(CreateCampaignCommand.fields, args)
        check_for_duplicity(data)
        return CreateCampaignCommand(**data)


class PatchCampaignCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x)),
        Field("name", "string", False),
        Field("start_date", "string", False),
        Field("end_date", "string", False),
        Field("description", "string", False),
        Field("external_link", "string", False)
    ]

    def __init__(self, id: int, name: str = None, start_date: str = None, end_date: str = None,
                 description: str = None, external_link: str = None):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.external_link = external_link


    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'PatchCampaignCommand':
        data = Validator.validate_and_extract(PatchCampaignCommand.fields, args)
        check_for_duplicity(data)
        return PatchCampaignCommand(**data)


class DeleteCampaignCommand(Command):
    fields = [
        Field("id", "integer", True, formatter=lambda x: int(x))
    ]

    def __init__(self, id: int):
        self.id = id

    @staticmethod
    @Validator.validates
    def from_dict(args: dict) -> 'DeleteCampaignCommand':
        data = Validator.validate_and_extract(DeleteCampaignCommand.fields, args)
        return DeleteCampaignCommand(**data)
