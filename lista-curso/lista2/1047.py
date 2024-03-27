hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

inicio_em_minutos = hora_inicio * 60 + minuto_inicio
fim_em_minutos = hora_fim * 60 + minuto_fim

if fim_em_minutos <= inicio_em_minutos:
    fim_em_minutos += 24 * 60

duracao_total_minutos = fim_em_minutos - inicio_em_minutos

horas = duracao_total_minutos // 60
minutos = duracao_total_minutos % 60

if horas == 24 and minutos == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")