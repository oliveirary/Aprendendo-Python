times = ('FLAMENGO','SANTOS','PALMEIRAS','GRÊMIO','ATHLETICO','SÃO PAULO',
         'INTERNACIONAL','CORINTHIANS','FORTALEZA','GOIÁS','BAHIA',
         'VASCO','ATLÉTICO-MG','FLUMINENSE','BOTAFOGO','CEARÁ','CRUZEIRO',
         'CSA','CHAPECOENSE','AVAÍ')
print('-='*30)
print(f'Lista de times {times}')
print('-='*30)
print(f'Os 5 primeiros colocados:{times[:5]}')
print('-='*30)
print(f'Os 4 últimos colocados:{times[-4:]}')
print('-='*30)
print(f'Ordem alfabéticas:{sorted(times)}')
print('-='*30)
print(f'A Chapecoense está na {times.index("CHAPECOENSE")+1}ª posição')