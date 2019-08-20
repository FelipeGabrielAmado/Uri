dias = int(input())

qtanos = int(dias/365)
qtmeses = int((dias % 365)/ 30)
qtdias = int((dias % 365)% 30)

print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(qtanos, qtmeses, qtdias))