import os
import django

# Configura o Django para usar as configurações do projeto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "livraria.settings")
django.setup()

from biblioteca.models import Autor, Genero, Livro
from restaurante.models import Especialidades

# Limpa os dados antigos (opcional)
Livro.objects.all().delete()
Autor.objects.all().delete()
Genero.objects.all().delete()
Especialidades.objects.all().delete()

# Criar gêneros reais
generos = [
    "Ficção Científica",
    "Romance",
    "Não-Ficção",
    "Fantasia",
    "História",
    "Biografia"
]
generos_objs = []
for nome in generos:
    g = Genero.objects.create(nome=nome)
    generos_objs.append(g)

# Criar autores reais
autores = [
    "Isaac Asimov",
    "Jane Austen",
    "Yuval Noah Harari",
    "J.K. Rowling",
    "Walter Isaacson",
    "George R. R. Martin"
]
autores_objs = []
for nome in autores:
    a = Autor.objects.create(nome=nome)
    autores_objs.append(a)

# Criar livros reais vinculando autores e gêneros
livros = [
    {
        "titulo": "Fundação",
        "autor": autores_objs[0],
        "genero": generos_objs[0],
        "ano_publicacao": 1951,
        "sinopse": "Uma saga épica sobre o futuro da humanidade e o colapso da galáxia.",
    },
    {
        "titulo": "Orgulho e Preconceito",
        "autor": autores_objs[1],
        "genero": generos_objs[1],
        "ano_publicacao": 1813,
        "sinopse": "Um romance clássico sobre amor e sociedade inglesa do século XIX.",
    },
    {
        "titulo": "Sapiens: Uma Breve História da Humanidade",
        "autor": autores_objs[2],
        "genero": generos_objs[2],
        "ano_publicacao": 2011,
        "sinopse": "Um olhar sobre a história da espécie humana desde os primórdios até hoje.",
    },
    {
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": autores_objs[3],
        "genero": generos_objs[3],
        "ano_publicacao": 1997,
        "sinopse": "O começo da jornada do jovem bruxo Harry Potter na escola de magia de Hogwarts.",
    },
    {
        "titulo": "Steve Jobs",
        "autor": autores_objs[4],
        "genero": generos_objs[5],
        "ano_publicacao": 2011,
        "sinopse": "Biografia do visionário cofundador da Apple, Steve Jobs.",
    },
    {
        "titulo": "As Crônicas de Gelo e Fogo",
        "autor": autores_objs[5],
        "genero": generos_objs[3],
        "ano_publicacao": 1996,
        "sinopse": "Uma série épica de fantasia medieval cheia de intrigas e guerras.",
    }
]

for livro in livros:
    Livro.objects.create(
        titulo=livro["titulo"],
        autor=livro["autor"],
        genero=livro["genero"],
        ano_publicacao=livro["ano_publicacao"],
        sinopse=livro["sinopse"]
    )


especialidades = [
    {
        "titulo": "reservas",
        "descricao": "Rua Ali Perto, 89 - Barra da Tijuca - Rio de Janeiro/RJ\n\nTerças a Domingos\n19h ás 23h",
        "tipo": "reserva"
    },
    {
        "titulo": "personal chef",
        "descricao": "Desde jantares íntimos até celebrações especiais, nosso personal chef proporcionará uma experiência culinária exclusiva e sob medida.",
        "tipo": "cardapio"
    },
    {
        "titulo": "jantar temático",
        "descricao": "Uma experiência gastronômica temática, cuidadosamente personalizada de acordo com suas preferências.",
        "tipo": "cardapio"
    },
    {
        "titulo": "buffet",
        "descricao": "De acordo com suas preferências, voce terá uma experiência gastronômica que surpreenderá e encantará seus convidados.",
        "tipo": "cardapio"
    },
      
]

for especialidade in especialidades:
    Especialidades.objects.create(
        titulo=especialidade["titulo"],
        descricao=especialidade["descricao"],
        tipo=especialidade["tipo"],
    )

print("Banco de dados povoado com dados reais com sucesso!")
