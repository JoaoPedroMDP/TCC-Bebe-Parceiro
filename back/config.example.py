# Variáveis de configuração do sistema
import os


# DATABASE DATABASE DATABASE DATABASE DATABASE
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "bebeparceiro")
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")


# Tempo de vida do token de acesso
TOKEN_TTL_SECONDS = 60 * 60 * 3


# Habilita login no sistema
AUTH_ENABLED = True

MANAGE_REGISTRATIONS = "manage_registrations"
MANAGE_BENEFICIARIES = "manage_beneficiaries"
MANAGE_SWAPS = "manage_swaps"
MANAGE_APPOINTMENTS = "manage_appointments"
MANAGE_PROFESSIONALS = "manage_professionals"
MANAGE_ACCESS_CODES = "manage_access_codes"
MANAGE_VOLUNTEERS = "manage_volunteers"
# Grupos de permissões
GROUPS = [
    MANAGE_REGISTRATIONS, MANAGE_BENEFICIARIES, MANAGE_SWAPS,
    MANAGE_APPOINTMENTS, MANAGE_PROFESSIONALS, MANAGE_ACCESS_CODES,
    MANAGE_VOLUNTEERS
]


ROLE_BENEFICIARY = "role_beneficiary"
ROLE_VOLUNTEER = "role_volunteer"
ROLE_ADMIN = "role_admin"
# Cargos genéricos
ROLES = [ROLE_BENEFICIARY, ROLE_VOLUNTEER, ROLE_ADMIN]


# Ambiente
ENV = os.getenv("ENV", "prod")
