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


# Grupos de permissões
GROUPS = [
    "manage_registrations", "manage_beneficiaries", "manage_swaps",
    "manage_appointments", "manage_professionals", "manage_access_codes",
    "manage_volunteers"
]