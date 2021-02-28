Projet réalisé par Margaux Lenne, Noëmie Le Roux (et Manon Coulombe pour le projet blog)

# Level_up_Programmation orientée objet

Le but de cette semaine était de découvrir ou approfondir les notions suivantes :

# Concepts 
- Encapsulation
- Abstraction
- Héritage
- Polymorphisme
- Classe vs. Instance

# Éléments de programmation
- Classe
- This / Self
- Constructeur
- Méthode
- Attribut / propriété / membre
- Interface

# Appliquer => création d'un “Low-Tech Blog”, un blog qui se consulte dans la console uniquement

- Faire en sorte que chaque utilisateur puisse être représenté avec le bon niveau de droits et donc les bonnes permissions :
-> Une admin peut lire, écrire et supprimer
-> Une rédactrice peut lire et écrire
-> Une visiteuse peut lire uniquement

- Modification de la fonction get_user pour que le code du menu affiche les bons choix en fonction de l’utilisateur connecté.
- La variable globale articles définie au-dessus de la fonction display_article est destinée à être alimentée des articles qui seront écrits par l'administratrice ou la rédactrice.

- Création d'une classe Article qui vous permettra de stocker ces saisies, et de stocker une liste d’articles dans articles. 

- Ajout d'une classe "Comment"
- Affichage des commentaires associés à la suite de l’article en cours de lecture
- À la fin de display_article, un menu à deux choix (“Commenter”, “Retour”) qui permet de rentrer un nouveau commentaire pour l’article en cours de lecture ou de revenir à la liste des articles. 
- Le commentaire est associé à son auteur 🙂
