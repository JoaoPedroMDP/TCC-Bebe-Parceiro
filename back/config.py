# Variáveis de configuração do sistema
import os


# DATABASE DATABASE DATABASE DATABASE DATABASE
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "osemp231")
DB_NAME = os.getenv("DB_NAME", "bebeparceiro")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")


# Tempo de vida do token de acesso
TOKEN_TTL_SECONDS = 60 * 60 * 3


# Habilita login no sistema
AUTH_ENABLED = True

# Estados civis
SINGLE = 'Solteiro'
MARRIED = 'Casado'
DIVORCED = 'Divorciado'
WIDOW = 'Viúvo'
MARITAL_STATUSES = [SINGLE, MARRIED, DIVORCED, WIDOW]

# Programas sociais
CRAS = 'CRAS'
MINHA_CASA_MINHA_VIDA = "Minha Casa Minha Vida"
CADASTRO_EMPREGO = 'Cadastro de Emprego'
BOLSA_FAMILIA = 'Bolsa Família'
CARTAO_ALIMENTACAO = 'Cartão alimentação'
SOCIAL_PROGRAMS = [CRAS, MINHA_CASA_MINHA_VIDA, CADASTRO_EMPREGO, BOLSA_FAMILIA, CARTAO_ALIMENTACAO]

# Status de um agendamento
PENDING = 'Pendente'
APPROVED = 'Aprovado'
REJECTED = 'Reprovado'
CANCELED = 'Cancelado'
FINISHED = 'Encerrado'
STATUSES = [PENDING, APPROVED, REJECTED, CANCELED, FINISHED]

# Grupos de permissões
MANAGE_REGISTRATIONS = "manage_registrations"
MANAGE_BENEFICIARIES = "manage_beneficiaries"
MANAGE_SWAPS = "manage_swaps"
MANAGE_APPOINTMENTS = "manage_appointments"
MANAGE_PROFESSIONALS = "manage_professionals"
MANAGE_ACCESS_CODES = "manage_access_codes"
MANAGE_VOLUNTEERS = "manage_volunteers"
MANAGE_ADDRESSES = "manage_addresses"
MANAGE_MARITAL_STATUSES = "manage_marital_statuses"
MANAGE_SOCIAL_PROGRAMS = "manage_social_programs"
MANAGE_SPECIALITIES = "manage_specialities"
MANAGE_EVALUATIONS = "manage_evaluations"
MANAGE_CAMPAIGNS = "manage_campaigns"
MANAGE_SIZES = "manage_sizes"

GROUPS = [
    MANAGE_REGISTRATIONS, MANAGE_BENEFICIARIES, MANAGE_SWAPS, MANAGE_APPOINTMENTS,
    MANAGE_PROFESSIONALS, MANAGE_ACCESS_CODES, MANAGE_VOLUNTEERS, MANAGE_ADDRESSES,
    MANAGE_MARITAL_STATUSES, MANAGE_SOCIAL_PROGRAMS, MANAGE_SPECIALITIES, MANAGE_EVALUATIONS,
    MANAGE_CAMPAIGNS, MANAGE_SIZES
]


# Cargos genéricos
ROLE_PENDING_BENEFICIARY = "role_pending_beneficiary"
ROLE_BENEFICIARY = "role_beneficiary"
ROLE_VOLUNTEER = "role_volunteer"
ROLES = [ROLE_BENEFICIARY, ROLE_VOLUNTEER, ROLE_PENDING_BENEFICIARY]


# Ambiente
ENV = os.getenv("ENV", "dev")

try:
    from config_local import *  # @UnusedWildImport
except ImportError:
    pass

