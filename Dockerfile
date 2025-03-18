# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Definir o diretório de trabalho dentro do container
WORKDIR /app


RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o container
COPY . .

# Comando para rodar o aplicativo
CMD ["python", "main.py"]