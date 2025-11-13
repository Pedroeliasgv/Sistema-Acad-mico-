FROM python:3.12-slim

# Evita buffering de logs
ENV PYTHONUNBUFFERED 1

# Atualiza pacotes e instala dependências do sistema
RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get clean

# Cria diretório da app
WORKDIR /app

# Copia requirements
COPY requirements.txt /app/

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . /app/

# Expõe porta interna
EXPOSE 8000

# Comando padrão
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
