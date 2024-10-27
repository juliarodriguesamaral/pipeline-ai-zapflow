## Configuração de ambiente

**1. Criar ambiente virtual**
   ``` 
   python -m venv .venv
   ```
    
**2. Ativar o ambiente virtual**
```
 .venv\Scripts\Activate
 ```

**3. Instalar dependências**
```
pip install -r requirements.txt
``` 
**3.1 Caso haja problemas na instalação do streamlit, use o binário pré compilado abaixo**
```
pip install --only-binary=:all: streamlit
```
    

## Rodar com Docker

**1. Criar a imagem Docker**
```
docker build -t pipeline-ai:1.0 .
``` 
    
**2. Criar e executar o container**
```
docker run -d -p 8501:8501 --name streamlit-container -v "C:\Documents\Workspace\pipeline-ai:/app" pipeline-ai:1.0
``` 
    
**3. Acessar a aplicação**

Abra no navegador: [http://localhost:8501](http://localhost:8501)

## Dockerfile.populate_db 

Este Dockerfile tem como objetivo criar e executar um container Docker que populará a tabela `sales` no banco de dados. Ele utiliza um script Python que gera 10.000 registros aleatórios de vendas, usando a biblioteca `Faker` para dados fictícios.

### Passos para Executar

**1. Criar a imagem Docker**

No terminal, execute o seguinte comando para construir a imagem a partir do `Dockerfile.populate_db`:

```sh
docker build -f Dockerfile.populate_db -t populate-db .
```

**2. Criar e executar o container**

Depois que a imagem for criada, execute o comando abaixo para iniciar o container e popular a tabela:

```sh
docker run --name populate-sales-table --network="host" populate-db
```


## Acessar MkDocs - Documentação do projeto

### Localmente
**1. Rodar MkDocs**
```
mkdocs serve
```

**2. Acessar mkdocs**
Abra no navegador: [http://localhost:8000](http://localhost:8000)

### Através do github
Abra no navegador: [https://juliarodriguesamaral.github.io/pipeline-ai-zapflow/](https://juliarodriguesamaral.github.io/pipeline-ai-zapflow/)