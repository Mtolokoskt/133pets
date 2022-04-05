import pytest   # motor / engine
import requests  # biblioteca para comunicar com APIs

base_url = 'https://petstore.swagger.io/v2'     # endereço da API
headers = {'Content-Type': 'application/json'}  # os dados serão no formato json


def testar_incluir_user():
    # 1 - Configura
    # 1.1 Dados de entrada: virão do user1.json
    # 1.2 Resultado Esperado
    status_code_esperado = 200
    code_esperado = 200
    tipo_user_esperado = 'unknown'
    message_esperada = '17041994'

    # Executa
    resultado_obtido = requests.post(
        url=base_url + '/user',
        data=open('C:\\Users\\Bruno\\PycharmProjects\\133pets\\vendors\\json\\user1.json', 'rb'),
        headers=headers
        )

    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()     # extrai o json da respose e guarda na variavel
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == tipo_user_esperado
    assert corpo_da_resposta['message'] == message_esperada



def testar_consultar_user():
    # 1 - Configura
    # 1.1 Dados de entrada
    # 1.2 Resultados Esperados
    status_code_esperado = 200
    id_esperado = 17041994
    username_esperado = "BrunoFaria"
    fisrt_name_esperado = "Bruno"
    last_name_esperado = "Faria"
    email_esperado = "brunoluizb@hotmail.com"
    password_esperado = "Trocar@123"
    phone_esperado = "169999999999"
    user_status_esperado = 1

    # 2 - Executa
    resultado_obtido = requests.get(
        url=base_url + '/user/BrunoFaria',
        headers=headers
        )

    # 3 - Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['firstName'] == fisrt_name_esperado
    assert corpo_da_resposta['lastName'] == last_name_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['password'] == password_esperado
    assert corpo_da_resposta['phone'] == phone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado



def testar_alterar_user():
    # 1 - Configura
    # 1.1 Dados de entrada: virão do user1.json
    # 1.2 Resultados Esperados
    status_code_esperado = 200
    code_esperado = 200
    tipo_user_esperado = 'unknown'
    message_esperada = '17041994'

    # 2 - Executa
    resultado_obtido = requests.put(
        url=base_url + '/user/BrunoFaria',
        data=open('C:\\Users\\Bruno\\PycharmProjects\\133pets\\vendors\\json\\user2.json', 'rb'),
        headers=headers
    )

    # 3 - Valida
    corpo_da_resposta = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == tipo_user_esperado
    assert corpo_da_resposta['message'] == message_esperada



def testar_delete_user():
    # 1 - Configura
    # 1.1 Dados de entrada
    # 1.2 Resultados Esperados
    status_code_esperado = 200
    code_esperado = 200
    tipo_user_esperado = 'unknown'
    message_esperada = 'FariaBruno'

    # Executa
    resultado_obtido = requests.delete(
        url=base_url + '/user/FariaBruno',
        headers=headers
    )

    # 3 - Valida
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == tipo_user_esperado
    assert corpo_da_resposta['message'] == message_esperada