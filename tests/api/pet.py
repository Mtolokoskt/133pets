import csv
import pytest   # motor / engine
import requests  # biblioteca para comunicar com APIs

base_url = 'https://petstore.swagger.io/v2'     # endereço da API
headers = {'Content-Type': 'application/json'}  # os dados serão no formato json

def testar_incluir_pet():
# Configura
  # Dados de entrada: virão do pet1.json
  # Resultado Esperado
    status_code_esperado = 200
    nome_pet_esperado = 'Lord'
    tag_esperada = 'Vacinado'

# Executa
    resultado_obtido = requests.post(
        url=base_url + '/pet',
        data=open('C:\\Users\\Bruno\\PycharmProjects\\133pets\\vendors\\json\\pet1.json', 'rb'),
        headers=headers
        )
# Valida

    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()     # extrai o json da respose e guarda na variavel
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada



def testar_consultar_pet():
    # 1 - Configura
    # 1.1 Dados de entrada
    pet_id = 17041994
    # 1.2 Resultados Esperados
    status_code_esperado = 200
    nome_pet_esperado = 'Lord'
    tag_esperada = 'Vacinado'

    # 2 - Executa
    resultado_obtido = requests.get(
        url=base_url + '/pet/17041994',
        headers=headers
        )

    # 3 - Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada



def testar_alterar_pet():
    # 1 - Configura
    # 1.1 Dados de entrada: virão do pet2.json

    # 1.2 Resultados Esperados
    status_code_esperado = 200
    nome_pet_esperado = 'Duck'
    status_esperada = 'Solded'

    # 2 - Executa
    resultado_obtido = requests.put(
        url=f'{base_url}/pet',
        data=open('C:\\Users\\Bruno\\PycharmProjects\\133pets\\vendors\\json\\pet2.json', 'rb'),
        headers=headers
    )

    # 3 - Valida
    corpo_da_resposta = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['status'] == status_esperada



def testar_delete_pet():
    # 1 - Configura
    # 1.1 Dados de entrada
    pet_id = 17041994

    # 1.2 Resultados Esperados
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = str(pet_id)

    # Executa
    resultado_obtido = requests.delete(
        url=base_url + '/pet/17041994',
        headers=headers
    )

    # 3 - Valida
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'C:\\Users\\Bruno\\PycharmProjects\\133pets\\vendors\\csv\\pets_positivo.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=',') # caracter delimitador
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


@pytest.mark.parametrize('pet_id,category_id,category_name,name,tags_id,tags_name,status,status_code', ler_dados_csv())
def testar_incluir_pet_json_dinamico(pet_id,category_id,category_name,name,tags_id,tags_name,status,status_code):
    # 1 - Configura
    # 1.1 Dados de entrada
    # Utilizara o arquivo pets_positivo.csv

    # 1.2 Resultados Esperados
    #Utilizará o arquivo pets_positivo.csv

    # 1.3 - Extra - Montar o json dinamicamente a partir do csv
    corpo_json = '{'
    corpo_json += f'  "id": {pet_id},'
    corpo_json += '   "category": {'
    corpo_json += f'  "id": {category_id},'
    corpo_json += f'  "name": "{category_name}"'
    corpo_json += '},'
    corpo_json += f'  "name": "{name}",'
    corpo_json += '   "photoUrls": ['
    corpo_json += '   "string"'
    corpo_json += '],'
    corpo_json += '   "tags": ['
    corpo_json += '{'
    corpo_json += f'  "id": {tags_id},'
    corpo_json += f'  "name": "{tags_name}"'
    corpo_json += '}'
    corpo_json += '],'
    corpo_json += f'  "status": "{status}"'
    corpo_json += '}'

    print(corpo_json)

    # 2 - Executa
    resultado_obtido = requests.post(
        url=base_url + '/pet',
        data=corpo_json,
        headers=headers
    )


    # 3 - Valida
    assert resultado_obtido.status_code ==  int(status_code)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert corpo_da_resposta['id'] == int(pet_id)
    assert corpo_da_resposta['category']['id'] == int(category_id)
    assert corpo_da_resposta['category']['name'] == category_name
    assert corpo_da_resposta['name'] == name
    assert corpo_da_resposta['tags'][0]['id'] == int(tags_id)
    assert corpo_da_resposta['tags'][0]['name'] == tags_name
    assert corpo_da_resposta['status'] == status
