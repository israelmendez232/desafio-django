# Desafio Django

###### [link para o projeto](#)

Desafio em Django para construção de uma área do aluno e registro de materiais. Projeto é dividido em duas partes:

### Layout

Os designs e fronts da página foram usados os templates gratuitos do **Bootstrap** presentes em `Examples` deles, [acessível aqui](https://getbootstrap.com/docs/4.3/examples/). Foi realizado poucas alterações, para agilizar na entrega do teste também.

### Administrador

Foi usado o próprio painel de administração do **Django** para gerenciar os cursos, inserir apostilas e os demais. Sendo dividido em três etapas:

1. **Cursos**: com campo de título, descrição e imagem;

2. **Aula**: título, apostilas associadas, cursos que é conectado e número da aula; 

3. **Apostila**: título, número da aula e o arquivo em pdf.

Lembrando um curso pode ter `n` aulas e uma aula pode ter `n` apostilas. 

---

## Como Executar

Para ativar o projeto é necessário as seguintes especificações:

- Docker para instalar e rodar ambiente;

- Uso de Python 3.7.

Segue os **passos**:

1. Instalar o ambiente ao acionar o arquivo `Dockerfile`que fica na pasta inicial;

2. Ao fazer isso, você também instalará as dependências necessárias para o projeto (que é apenas a biblioteca de Django);

3. Para rodar o site, execute: `python manage.py runserver`


