def max(mot):
   maxi = 0 
   for i in range(0,len(mot)):
        if mot(i).isupper() == True:
         maxi == maxi + 1

def min(mot):
   mini = 0 
   for i in range(0,len(mot)):
        if mot(i).islower() == True:
         mini == mini+ 1

def alpha(mot):
   al = 0 
   for i in range(0,len(mot)):
        if mot(i).isalpha() == False:
         alpha ==alpha + 1

def chaine_max(mot):
   maxi = 0
   for i in range(0,len(mot)):
    if mot(i).isupper() == True: 
      while mot(i).isupper() == True:
         maxi =maxi + 1
         break
      
def chaine_min(mot):
   mini = 0
   for i in range(0,len(mot)):
    if mot(i).islower() == True: 
      while mot(i).islower() == True:
         mini =mini+ 1
         break
      
def score(mot):
   length = len(mot)
   sm = len(mot)*4+( length - max )*2+(length - min)*3+(alpha*5)
   sf = chaine_max*2+chaine_min*2


def resultat(mot):
   if score(mot) < 20:
      return ("le mot de passe est trés faible")
   elif score(mot) >= 20 and score(mot) < 40:
      return ("le mot de passe est faible")
   elif score(mot) >= 40 and score(mot) < 80:
      return ("le mot de passe est fort")
   else:
      return ("le mot de passe est trés fort")
   

mot = input("enter le mot de passe \n")
resultat(mot)


