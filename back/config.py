# Variáveis de configuração do sistema
import os


# DATABASE DATABASE DATABASE DATABASE DATABASE
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
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
MANAGE_REGISTRATIONS = "Cadastros"
MANAGE_BENEFICIARIES = "Beneficiárias"
MANAGE_SWAPS = "Trocas"
MANAGE_APPOINTMENTS = "Agendamentos"
MANAGE_PROFESSIONALS = "Profissionais"
MANAGE_ACCESS_CODES = "Códigos de acesso"
MANAGE_VOLUNTEERS = "Voluntárias"
MANAGE_ADDRESSES = "Endereços"
MANAGE_MARITAL_STATUSES = "Estados Civis"
MANAGE_SOCIAL_PROGRAMS = "Benefícios Sociais"
MANAGE_SPECIALITIES = "Especialidades"
MANAGE_EVALUATIONS = "Admissões"
MANAGE_SIZES = "Tamanhos"
MANAGE_CAMPAIGNS = "Campanhas"
MANAGE_REPORTS = "Relatórios"

GROUPS = [
    MANAGE_REGISTRATIONS, MANAGE_BENEFICIARIES, MANAGE_SWAPS, MANAGE_APPOINTMENTS,
    MANAGE_PROFESSIONALS, MANAGE_ACCESS_CODES, MANAGE_VOLUNTEERS, MANAGE_ADDRESSES,
    MANAGE_MARITAL_STATUSES, MANAGE_SOCIAL_PROGRAMS, MANAGE_SPECIALITIES, MANAGE_EVALUATIONS,
    MANAGE_CAMPAIGNS, MANAGE_SIZES, MANAGE_REPORTS
]


# Tamanhos
CLOTH_TYPE = "Roupa"
SHOE_TYPE = "Sapato"

P = "P"
M = "M"
G = "G"
ONE_YEAR = "1 ano"
TWO_YEARS = "2 anos"

SHOE_SIZES = [i for i in range(13, 23)]
CLOTH_SIZES = [P, M, G, ONE_YEAR, TWO_YEARS]

# Ambiente
PROD = 'production'
DEV = 'development'

ENV = os.getenv("ENV", DEV)

try:
    from config_local import *  # @UnusedWildImport
except ImportError:
    pass

