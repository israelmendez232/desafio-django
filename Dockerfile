# Base do container:
FROM python:3

# Definindo algumas variáveis para o ambiente:
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

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
RUN pip3 install django

# Rodando a aplicação:
RUN git clone 
CMD python3 manage.py runserver
