def parcours_semaine(nombre_marches, hauteur_marche):
 aller = nombre_marches * hauteur_marche / 100
 retour = aller
 parcours_total = aller + retour
 parcours_par_jour = parcours_total * 5
 parcours_par_semaine = parcours_par_jour * 7
 print("Pour {0} marches de {1} cm, le gardien parcourt {2:.2f} m par semaine.".format(nombre_marches, hauteur_marche, parcours_par_semaine))
parcours_semaine(10, 5)