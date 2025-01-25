import random



list_categorie = ["algorithme et logique","bases de donnes","programmation orientée objet","developpement web statique"]
databese ={
    "algorithme et logique":
                            {
                                "facile":
                                        {
                                            "Quel est le type de données de la valeur True ?":
                                                                                                {"bool":True , "int":False , "string":False} , 
                                            "Quelle instruction permet de sortir d'une boucle en Python ?":
                                                                                                {"exit":False , "break":True , "stop":False} , 
                                            "Quel est le résultat de 2 ** 3 en Python ?":
                                                                                                {"6":False , "8":True , "9":False} , 
                                            "Quel est l'équivalent de x = x + 1 en Python ?":
                                                                                                {"x++":False , "++x":False , "x += 1":True}
                                        },
                                "moyen":
                                        {
                                            "Que retourne la fonction suivante : len([1, [2, 3], 4]) ?":
                                                                                                {"3":True , "4":False , "5":False},
                                            "Quel algorithme est le plus efficace pour rechercher un élément dans une liste triée ?":
                                                                                                {"Recherche linéaire":False , "Recherche binaire":True , "Tri tapide":False},
                                            "Quelle structure de données utilise le principe FIFO ?":
                                                                                                {"Pile":False , "File":True , "Dictionnair":False}
                                        },
                                "difficile":
                                        {
                                            "Quelle boucle s'exécute au moins une fois, même si la condition est fausse ?":
                                                                                                {"for":False , "while":False , "do...while":True} ,
                                            "Quel algorithme est utilisé pour trier rapidement de grandes quantités de données?":
                                                                                                {"Tri à bulles":False , "Tri fusion":True , "Tri par insertion":False}
                                        }
                                        
                            },
    


    "bases de donnes":
                            {
                                "facile":
                                        {
                                            "Quelle commande SQL est utilisée pour ajouter des données dans une table ?":
                                                                                                {"INSERT ":True ,"UPDATE":False,"SELECT":False},
                                            "Quelle clé assure l'unicité des enregistrements dans une table ?":
                                                                                                {"Clé étrangère":False,"Clé primaire ":True,"Index":False},
                                            "Que signifie SQL ?":  
                                                                                                {"Structured Query Language ":True,"Simple Query Logic":False,"Sequential Query Language":False},
                                            "Quelle commande permet de récupérer toutes les données d'une table clients ?":
                                                                                                {"SELECT * FROM clients ":True,"GET * FROM clients":False,"SHOW * FROM clients":False},
                                            "Quel type de base de données utilise SQL ?":
                                                                                                {"NoSQL":False,"Relationnelle":True," Graphique":False}
                                        },
                                "moyen":
                                        {
                                            "Quelle commande supprime des données sans supprimer la structure de la table ?":
                                                                                                {"DROP":False,"DELETE":True,"TRUNCATE":False},
                                            "Quelle commande est utilisée pour modifier une table existante ?":
                                                                                                {"ALTER":True,"MODIFY":False,"CHANGE":False},
                                            "Quel est le rôle d'une clé étrangère ?":
                                                                                                {"Identifier de manière unique une ligne":False,"Lier deux tables":True,"Créer un index":False}
                                        },
                                "difficile":
                                        {
                                            "Quel type de jointure renvoie les enregistrements correspondants des deux tables":
                                                                                                {"LEFT JOIN":False," RIGHT JOIN":False,"INNER JOIN":True},
                                            "Que fait la commande DROP TABLE clients ?":
                                                                                                {"Supprime la table et ses données":True,"Supprime uniquement les données":False,"Vide la table":False}
                                        }
                            },



    "programmation orientée objet":
                            {
                                "facile":
                                        {
                                            "Quel mot-clé est utilisé pour créer une classe en Python ?":
                                                                                                {"object":False,"class":True,"def":False},
                                            "Qu'est-ce que l'héritage en POO ?":
                                                                                                {"La création d'une nouvelle classe sans attribut":False,"Une classe qui hérite les attributs et méthodes d'une autre":True,"Une copie exacte d'une classe":False},
                                            "Comment appelle-t-on une fonction définie dans une classe ?":
                                                                                                {"Méthode":True,"Fonction":False,"Procédure":False},
                                            "Quel est le rôle du constructeur dans une classe ?":
                                                                                                {"Détruire un objet":False,"Initialiser un objet":True,"Copier un objet":False}
                                        },
                                "moyen":
                                        {
                                            "Quel mot-clé est utilisé pour créer un objet à partir d'une classe ?":
                                                                                                {"create":False,"init":False,"new":True},
                                            "Quelle syntaxe permet d'accéder à un attribut privé d'une classe ?":
                                                                                                {"self.attribut":False,"self._attribut":True,"self.__attribut":False},
                                            "Que signifie l'encapsulation ?":
                                                                                                {"Regrouper les données et les méthodes dans une même classe":True,"Cacher les données uniquement":False,"Partager les données entre classes":False},
                                            "Quelle relation représente 'est un' entre deux classes ?":
                                                                                                {"Composition":False,"Association":False,"Héritage":True}
                                        },
                                "difficile":
                                        {   
                                            "Quel concept permet d'utiliser le même nom de méthode pour des comportements différents ?":
                                                                                                {"Encapsulation":False,"Polymorphisme":True,"Abstraction":False},
                                            "Quel est le concept qui consiste à cacher les détails d'implémentation ?":
                                                                                                {"Abstraction":True,"Héritage":False,"Polymorphisme":False}
                                        }
                            },
    "developpement web statique":
                            {
                                "facile":
                                        {
                                            "Quel langage est utilisé pour structurer une page web ?":
                                                                                                {"CSS":False,"HTML":True,"JavaScript":False},
                                            "Quel langage est utilisé pour styliser une page web ?":
                                                                                                {"HTML":False,"JavaScript":False,"CSS":True},
                                            "Quelle balise HTML permet d'insérer une image ?":
                                                                                                {"<img>":True,"<image>":False,"<pic>":False},
                                            "Quel attribut de la balise <a> définit le lien ?":
                                                                                                {"href":True,"link":False,"src":False},
                                            "Quelle propriété CSS change la couleur du texte ?":
                                                                                                {"color":True,"background-color":False,"text-color":False},
                                            "Quel est le rôle du fichier index.html ?":
                                                                                                {"Page d'erreur":False,"Page principale":True,"Feuille de style":False},
                                            "Quelle balise est utilisée pour les listes non ordonnées ?":
                                                                                                {"<ul>":True,"<ol>":False,"<li>":False},
                                            "Quel élément HTML permet de structurer un formulaire ?":
                                                                                                {"<input>":False,"<form>":True,"<textarea>":False}
                                            
                                            
                                        },
                                "moyen":
                                        {
                                            "Quel format d'image est le plus adapté pour des icônes ?":
                                                                                                {"PNG":True,"JPEG":False,"BMP":False},
                                            "Comment lier un fichier CSS à un fichier HTML ?":
                                                                                                {"<link rel='stylesheet' href='style.css'>":True,"<style src='style.css'>":False,"<css link='style.css'>":False}
                                                            
                                        }
                            }
            }

#partie algo_logique
def choix_categorie_niveau(databese,choix_niveau,choix_num_question,list_categorie,choix):
    
        #déclarée dictionair question:
        algo_question = databese[list_categorie[choix-1]][choix_niveau]
        
        #déclarée liste de question:
        list_question = []
        for key in algo_question.keys():#Remplissage liste de question
            list_question.append(key)
        
        #fonction générale:
        def body(choix_num_question):
           
                score = 0
                i = 0
                x = (random.sample(list_question , k=choix_num_question))  
                for list in x:
                    
                    i += 1
                    print(f"\n{i}) {list}:")
                    repense = algo_question[list]
                    
                    y = 0
                    #déclarée liste reponse:
                    list_repense = []
                    for key in repense.keys():
                        list_repense.append(key)
                        y += 1
                        print(f"{y}) {key}.")
                    
                    #verifier nombre votre réponse est valide:
                    while True:
                        try:
                            num_votre_reponse = int(input(f"\nenterz votre reponse (1 - 2 - 3):"))
                            if num_votre_reponse in [1 , 2 , 3]:
                                break 
                            else:
                                print("\nvotre choix invalide!")
                        except ValueError:
                            print("votre choix invalide! entrez un chiffre entier.")
                    
                    #Vérifiez la réponse corecte ou incorecte:
                    if repense[list_repense[num_votre_reponse-1]] == True:
                        score += 1
                        print(f"\nvotre reponse {list_repense[num_votre_reponse-1]} corecte.")  
                    else:
                        print(f"\nvotre reponse {list_repense[num_votre_reponse-1]} incorecte.")
                        
                print(f"\nvotre score est:{score}")
                
#partie des question disponible:       
        if len(list_question) >= choix_num_question:
            body(choix_num_question)
        
        
#partie des question pas disponible:           
        elif len(list_question) < choix_num_question:
            print(f"\nLe nombre des question disponibles est:{len(list_question)}")
            body(len(list_question))
            
            
            
            
# Partie déclarer les niveau et nombre des questions         
def choixs(choix,list_categorie):
    
    while True:
        choix_niveau = input("\nentrez votre niveau(facile/moyen/difficile):")
        if choix_niveau == "facile" or choix_niveau == "moyen" or choix_niveau == "difficile":
            break
        else:
            print("choix invalid!")
            
    while True:
        try:
            choix_num_question = int(input("\nentrez le nombre des question:"))
            if choix_num_question > 0:
                break
            
            elif choix_num_question <=0 :
                print("\nvotre choix invalide! entrez un nombre positive.")

        except ValueError:
            print("\nvotre choix invalide! entrez un chiffre entier.")
            
    verifier_niveau_existant = databese[list_categorie[choix-1]]
    
    if choix_niveau in verifier_niveau_existant.keys()    :
        choix_categorie_niveau(databese,choix_niveau,choix_num_question,list_categorie,choix)
    else:
        print(f"Désolé cette niveau '{choix_niveau}' pas disponible")
    


#menu
print("--- bienvenneu a notre programme ---")
print("""
\nDescription du projet : Programme de questions à choix multiples (QCM)
Ce programme est un système de questions à choix multiples (QCM) conçu pour aider les utilisateurs à tester leurs connaissances dans divers domaines. Le programme propose différents niveaux de difficulté et permet à l'utilisateur de choisir la catégorie et le nombre de questions auxquelles il souhaite répondre.

Comment utiliser le programme :
Lancer le programme : Lorsque vous démarrez le programme, une liste de catégories apparaîtra. L'utilisateur doit choisir la catégorie à partir de laquelle il souhaite répondre aux questions.

Choisir la catégorie :

Catégorie 1 : "Algorithmes et logique".
Catégorie 2 : "Bases de données".
Catégorie 3 : "Programmation orientée objet (POO)".
Catégorie 4 : "Développement web statique".
Entrez le numéro de la catégorie (1, 2, 3 ou 4) selon votre choix.

Choisir le niveau : Après avoir choisi la catégorie, vous serez invité à définir le niveau de difficulté :

"facile".
"moyen".
"difficile".
Entrez le niveau souhaité (par exemple : facile).

Définir le nombre de questions : Entrez le nombre de questions auxquelles vous souhaitez répondre. Si le nombre total de questions dépasse le nombre disponible dans le niveau choisi, le nombre disponible sera défini automatiquement.

Répondre aux questions :

Chaque question sera affichée avec trois options de réponse (1, 2, 3).
Entrez le numéro de la réponse correcte (par exemple : 1 ou 2 ou 3).
Vous serez informé si votre réponse est correcte ou incorrecte.
Afficher les résultats : Après avoir répondu à toutes les questions, le programme affichera le score final (le nombre de réponses correctes).

Quitter le programme : Si vous souhaitez quitter le programme, choisissez l'option numéro (5) dans le menu principal.
""")

while True:
    try:
        print("\n1) Entrez le chiffre 1 pour categorie Algorithmes et Logique.")
        print("2) Entrez le chiffre 2 pour categorie Bases de Données.")
        print("3) Entrez le chiffre 3 pour categorie Programmation Orientée Objet (POO) ")
        print("4) Entrez le chiffre 4 pour categorie developpement web statique.")
        print("5) Entrez le chiffre 5 pour quitter le programme.")
    
        choix = int(input("\nEntrez votre choix:"))
        if choix==1:
            choixs(choix,list_categorie)
            
        elif choix==2:     
            choixs(choix,list_categorie)
            
        elif choix==3:   
            choixs(choix,list_categorie)
                        
        elif choix==4:
            choixs(choix,list_categorie) 
                       
        elif choix==5:
            print("Merci d'avoir utilisé le programme. Au revoir!")
            break
        
        else:
            print("\nchoix invalid!")
        
    except ValueError:
        print("\nvotre choix invalide! entrez un chiffre entier.")
    
   
