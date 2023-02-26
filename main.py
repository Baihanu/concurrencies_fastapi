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
    moeda = f'{de}-{para}'

    link = f'https://economia.awesomeapi.com.br/last/{moeda}'
    requisicao = requests.get(link)
    fk_result = requisicao.json()[f'{de}{para}']

    resultado = {
        'Compra': fk_result['bid'],
        'Venda': fk_result['ask'],
        'Ultima Atualizacao': fk_result['create_date'],
        'Minima': fk_result['low'],
        'Maxima': fk_result['high'],
        'Variacao': fk_result['varBid'],
        'Porcentagem de Variacao': fk_result['pctChange'],
        f'Valor em {de}': quantia,
        f'Valor em {para}': (quantia*float(fk_result['bid']))
    }

    return {f'Cotacao de {de} para {para}': resultado}
