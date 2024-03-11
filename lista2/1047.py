HoraInicial, MinutosInicial, HorasFinais, MinutosFinais = map(int, input().split())

if (HoraInicial < HorasFinais and MinutosInicial < MinutosFinais) or (HoraInicial == HorasFinais and MinutosInicial > MinutosFinais):
    DuracaoHoras = HoraInicial - HorasFinais
    DuracaoMinutos = MinutosInicial - MinutosFinais
elif (HoraInicial > HorasFinais and MinutosInicial > MinutosFinais or (HoraInicial > HorasFinais and MinutosInicial < MinutosFinais)):
    DuracaoHoras = 24 - HoraInicial + HorasFinais
    DuracaoMinutos = 60 - MinutosInicial + MinutosFinais
else:
    DuracaoHoras = 24
    DuracaoMinutos = 0

print(f"O JOGO DUROU {DuracaoHoras} HORA(S) E {DuracaoMinutos} MINUTO(S)")