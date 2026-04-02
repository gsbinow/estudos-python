admin = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]

email = input('Por favor, insira seu emgail:').lower() . strip()

if email in admin:
    print('Acesso liberado! Bem-vindo ao painel de controle')
else:
    print('Acesso negado. VocÊ não tem permissão de administrador')