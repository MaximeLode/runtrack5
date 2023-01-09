def afficher_tapis(n):
  for i in range(n+1):
    ligne = ""
    for j in range(n+1):
      if i == j:
        ligne += "X"
      else:
        ligne += "."
    print(ligne)
afficher_tapis(4)