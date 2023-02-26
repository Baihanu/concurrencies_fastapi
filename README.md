# concurrencies_fastapi
Implementação de API para cotação com FastAPI

Esse projeto utiliza as seguintes libs:
 - [FastAPI](https://fastapi.tiangolo.com/) é um framework Web Python moderno, de alto desempenho e com baterias inclusas, perfeita para criar RESTful APIs.

 - [Requests](https://requests.readthedocs.io/en/latest/) é uma biblioteca HTTP para a linguagem de programação Python. O objetivo do projeto é tornar as solicitações HTTP mais simples e mais fáceis de usar.

## Para Usar/Desenvolver:

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9.
3. Ative o virtualenv.
4. Instale as dependências.
5. Levante o servidor.
6. Acesse a documentação da aplicação.
7. Acesse o Endpoint de cotação conforme exemplo.

### Ambientes Linux:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/cotacao?de=BRL&para=USD&quantia=9
```
### Ambientes Windows:
```
Set-ExecutionPolicy Unrestricted -Scope Process
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/cotacao?de=BRL&para=USD&quantia=9
```

### Rodando com Docker:
```
docker build -t concurrencies-fastapi .
docker run --rm --name concurrencies_fastapi --publish 8000:8000 concurrencies-fastapi
```