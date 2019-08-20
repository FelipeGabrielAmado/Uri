A = int(input())
coelho = int(0)
rato = int(0)
sapo = int(0)

for x in range(1, A+1):
  teste = input().split()
  qt, cob = teste
  if (cob == 'C'):
    coelho+= int(qt)
  elif (cob == 'R'):
    rato+= int(qt)
  if (cob == 'S'):
    sapo+= int(qt)

total = coelho + rato + sapo

print("Total: %d cobaias" %total)
print("Total de coelhos: %d" %coelho)
print("Total de ratos: %d" %rato)
print("Total de sapos: %d" %sapo)
print('Percentual de coelhos: %.2f' %float(((100*coelho)/total)),'%')
print('Percentual de ratos: %.2f' %float(((100*rato)/total)),'%')
print('Percentual de sapos: %.2f' %float(((100*sapo)/total)),'%')