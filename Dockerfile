# Base do container:
FROM python:3

# Definindo algumas variáveis para o ambiente:
ENV PYTHONUNBUFFERED 1

# Criando o diretório
RUN mkdir /desafioDjango
WORKDIR /desafioDjango
ADD . /desafioDjango/

# Porta para acessar:
ENV PORT=8888

# Instalando dependências do sistema:
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Instalando bibliotecas:
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

# Servindo o estático:
RUN python manage.py collectstatic --noinput

# Rodando a aplicação:
EXPOSE 8000
CMD ["/start.sh"]
