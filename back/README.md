# Back-end Bebê Parceiro

## User
O telefone de uma pessoa é considerado como seu username. Logo, quando a pessoa troca 
de telefone, ela troca de username.

## Rotas de filtragem
Não é possível filtrar um model a partir de um campo de um model relacionado. Por exemplo, não é possível
filtrar as beneficiadas pelo email delas, visto que email é um campo de 'User'

## Comandos do Django
`python manage.py mfresh`: Limpa todos os dados do BD
`python manage.py seed`: Popula o Banco de Dados com dados básicos
`python manage.py seed --test`: Popula o Banco de Dados com dados para testar o projeto (possui uma voluntária pra cada permissão, algumas beneficiadas)
