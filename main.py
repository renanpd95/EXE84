import os

n = 1
cont = 0
while (n > 0):
  a = float(input("Digite a altura: "))
  b = float(input("Digite a base: "))
  ang = b * a
  print(f"Área do retangulo:{ang:.2f}")
  if(ang > 5000):
    cont = cont + 1
  conti = str(input("Deseja continuar: (S/N)"))
  if (conti == "S" or conti == "SIM" or conti == "sim" or conti == "s" or conti == "Sim" or conti == "yes" or conti == "YES"):
    n = 1
    os.system('clear')
  else:
    n=0
    os.system('clear')
    print("Programa finalizado")


    
