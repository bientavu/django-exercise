# Introduction

Vous développez le système de suivi des ventes de la multinationale ACME. Cette entreprise vend des articles auxquels sont associés les informations suivantes :
* Code unique de l’article (3 lettres + 3 chiffres, par ex. ABC123)
* Catégorie (plusieurs articles peuvent avoir la même catégorie)
* Nom
* Coût de fabrication

Les informations suivantes sont également enregistrées pour chaque vente (une vente concerne un seul article à la fois) :
* Date de la vente (jour)
* Auteur de la saisie
* Article
* Quantité
* Prix de vente unitaire

Les prix sont exprimés dans une unité arbitraire (pas de notion de devise à gérer).

# Consignes

Vous devez implémenter une API REST, uniquement accessible à des utilisateurs authentifiés, permettant les opérations suivantes :
* Ajout d’un article
* Ajout d’une vente
* Modification / suppression d’une vente, uniquement possible par l’utilisateur qui l’a créée
* Liste (paginée par 25 éléments) des ventes (date, catégorie article, code article, nom article, quantité, prix de vente unitaire, prix de vente total)
* Bonus : liste agrégée des ventes (paginée par 25 éléments également) par article avec catégorie associée, totaux des prix de vente, pourcentage de marge, date de la dernière vente, ordonnée par totaux des prix de vente décroissants.

Les opérations CRUD sur les articles/ventes doivent également être possibles depuis l'admin de Django, sans notion particulière de permissions.

# Pour démarrer

Le dépôt contient un projet Django prêt à être utilisé pour réaliser l'exercice (il s'agit d'une version simplifiée de la structure de nos projets internes). Pour démarrer :
* Cloner/forker ce dépôt.
* Créer un environnement virtuel Python 3.
* Installer les dépendances avec `pip install -r requirements.txt`.
* Effectuer les migrations initiales (`./manage.py makemigrations && ./manage.py migrate`).

À noter :
* Écrivez le code de l'exercice comme vous écririez du code de production.
* L'écriture de tests automatisés est laissée à votre discrétion, leur utilité/nécessité fera l'objet d'une discussion lors de la revue de votre exercice.
* Un modèle pour les utilisateurs existe déjà (`users.User`) et peut être utilisé.
* L'utilisation de `djangorestframework` et `dj-rest-auth` est encouragée mais pas obligatoire.

# Soumettre votre solution

Merci de nous envoyer un lien vers votre solution par email.
