import math
#Challenge1
prenom=input("ENTRER VOTRE PRENOM: ")
age= input ('ENTRER VOTRE AGE: ')
print(f'BONJOUR, VOTRE prenom:{prenom}, Entrer votre age: {age}')


#Challenge2

nom=input("ENTRER VOTRE NOM: ")
salaire_horaire=float(input("ENTRER VOTRE SALAIRE: "))
nb_heure=float(input("Entrer le nombre d'heure que tu as travaillees:"))

if int(nb_heure) > 40:
    salaire_horaire2=float(salaire_horaire)*1.5
    salaire_total=salaire_horaire*40+salaire_horaire2*(nb_heure)-40

else:
    salaire_total=salaire_horaire*nb_heure

print(f'Bonjours {nom}, votre salaire est {salaire_total}')

#Challenge 3:
try:
    nom=input("ENTRER VOTRE NOM: ")
    salaire_horaire=float(input("ENTRER VOTRE SALAIRE: "))
    nb_heure=float(input("Entrer le nombre d'heure que tu as travaillees:"))

    if int(nb_heure) > 40:
        salaire_horaire2=float(salaire_horaire)*1.5
        salaire_total=salaire_horaire*40+salaire_horaire2*(nb_heure)-40

    else:
        salaire_total=salaire_horaire*nb_heure

    print(f'Bonjours {nom}, votre salaire est {salaire_total}')

except ValueError:
    print("Une erreur a ete detectee!")

#Challenge4
n1= float(input("Entrer un nombre:"))
n2= float(input("Entrer un nombre:"))

if n1*n2>0:
    print("le produit est positif")
elif n1*n2==0:
    print("le produit est nul")
else:
    print("le produit est negatif")

#challenge5:

n= float(input("Entrer un nombre:"))
somme=0
i=1
while i<=n:
    somme+=i
    i+=1
print("la somme est: ", somme)

#Challenge6:

chaine=input("Entrer une chaine de caractere: ")
chaine_inversee=''
i=len(chaine)-1
while i>=0:
    chaine_inversee+=chaine[i]
    i -= 1
print ("la chaine inversee est: ", chaine_inversee)

#challenge7
x1= float(input("entrer x1: "))
x2= float(input("entrer x2: "))
y1= float(input("entrer y1: "))
y2= float(input("entrer y2: "))
distance= math.sqrt( (x2 - x1)**2 + ((y2 -y1)**2) )
print("la distance entre les 2 points est: ", distance)





