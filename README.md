### Configuração de ambiente

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
    

### Rodar com Docker

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