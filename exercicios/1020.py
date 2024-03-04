dias = int(input())
ano = dias // 365
dias = dias % 365
mes = dias // 30
dia = dias % 30
print(
    f"{ano} ano(s)"
    f"{mes} mes(es)"
    f"{dia} dia(s)"
)