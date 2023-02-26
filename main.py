import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/cotacao")
def cotacao(de: str, para:str, quantia:float):
    """
    Função para pegar e fazer cotação das seguintes combinações de moedas
    USD-BRL,  USD-EUR,  BRL-USD,  BRL-EUR,  EUR-USD,  EUR-BRL,
    BTC-USD,  BTC-BRL,  BTC-EUR,  ETH-USD,  ETH-BRL,  ETH-EUR,
    """
    outras_cotacoes = [
    'ETH-EUR', # Parece que essa comparação pela API do Awesome está errada
    'USD-BTC',
    'BRL-BTC',
    'EUR-BTC',
    'ETH-BTC',
    'USD-ETH',
    'BRL-ETH',
    'EUR-ETH',
    'BTC-ETH',
    ]

    moeda = f'{de}-{para}'
    if moeda in outras_cotacoes:
        return cotacoes_moeda_para_BTC_ETH(de, para, quantia)

    link = f'https://economia.awesomeapi.com.br/last/{moeda}'
    requisicao = requests.get(link)
    fk_result = requisicao.json()[f'{de}{para}']

    resultado = {
        'Ultima Atualizacao': fk_result['create_date'],
        f'Valor em {de}': quantia,
        f'Valor em {para}': (quantia*float(fk_result['bid']))
    }

    return {f'Cotacao de {de} para {para}': resultado}

def cotacoes_moeda_para_BTC_ETH(de:str, para:str, quantia:float):
    """
    Essa função auxilia em casos de pesquisa de cotação de "Moeda" para BTC/ETH, pois a apiawesome não tem implementado.
    """
    link = f'https://economia.awesomeapi.com.br/last/{para}-USD'
    requisicao = requests.get(link)
    fk_result = requisicao.json()[f'{para}USD']

    if 'USD' == de:

        resultado = {
        'Ultima Atualizacao': fk_result['create_date'],
        f'Valor em {de}': quantia,
        f'Valor em {para}': (quantia/float(fk_result['bid']))
    }
    
    else:
        link_2 = f'https://economia.awesomeapi.com.br/last/{de}-USD'
        requisicao_2 = requests.get(link_2)
        fk_result_2 = requisicao_2.json()[f'{de}USD']

        valor = float(fk_result_2['bid'])/float(fk_result['bid'])

        resultado = {
        'Ultima Atualizacao': fk_result['create_date'],
        f'Valor em {de}': quantia,
        f'Valor em {para}': (quantia*valor)
    }
    
    return {f'Cotacao de {de} para {para}': resultado}
