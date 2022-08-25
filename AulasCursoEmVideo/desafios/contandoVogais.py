palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
vogais = 'a', 'e', 'i', 'o', 'u'

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end=' ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra.lower(), end=' ')

