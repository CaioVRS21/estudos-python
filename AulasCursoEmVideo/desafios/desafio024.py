cidade = input('Sua cidade começa ou não com a palavra Santo? Descubra agora! Digite o nome da sua cidade: ').strip()

print('A cidade {}, começa com Santo? {}'.format(cidade, cidade[:5].upper() == 'SANTO'))
