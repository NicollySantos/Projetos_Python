
import time

user = 'Nicolly'
senha = '@1234'

user_input = input('Digite seu usuário: ')
senha_input = input('Digite sua senha: ')

if user_input == user and senha_input == senha:
    print('Acesso Liberado!')
    print('Por favor, aguarde...')
    time.sleep(5)
    print('Carregando...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Agora já pode acessar a sua conta! Mantenha-se conectado...')
elif user_input == user and senha_input != senha:
    print('Senha incorreta! Não pode acessar nosso sistema')
elif user_input != user and senha_input == senha:
    print('Usuário incorreto! Não pode acessar nosso sistema')
else:
    print('Você checar os dois campos incorretos para acessar nosso sistema!')