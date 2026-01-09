# Mini RPG – API Tavernier & Quêtes (DevSecOps)

## 1. Présentation du projet 

Ce projet est une application backend en Python exposant une API REST CRUD, accompagnée d’une interface web simple en HTML/CSS/JavaScript.

Le thème choisi est un mini RPG dans lequel un tavernier propose des quêtes à un aventurier.
Le joueur peut consulter les quêtes, en accepter une (une seule fois), la modifier, ou la refuser.

Le projet suit une démarche DevOps / DevSecOps simplifiée, mettant l’accent sur :

- la compréhension du cycle de vie d’une application
- la version du code
- la conteneurisation
- l’automatisation via CI/CD
- la documentation

## 2. Fonctionnement global

- Architecture simples
- Backend : Python + Flask
- Frontend : HTML / CSS / JavaScript
- Communication : API REST (JSON)
- Stockage : Base de donnée SQL
- Conteneurisation : Docker
- CI/CD : GitHub Actions

`Navigateur → HTML / JS → API Flask → Base de donnée SQL`

## 3. Fonctionnalitées principales 

### Gestion des quêtes (CRUD)

- Consultation des quêtes
- Création d’une quête
- Modification d’une quête
- Suppression d’une quête

## 4. Endpoints de l'API

### GET 
- `GET /quests` -> Pour récupérer les quêtes

### POST 
- `POST /quests` -> Pour créer une nouvelle quête 

### PUT 
- `PUT /quests/{id}` -> Pour modifier la quête 

### DELETE 
- `DELETE /quests/{id}` -> Pour supprimer la quête 

#### Toutes les données sont échangées au format ` JSON `

## 5. Base de données

La base SQL est exécutée dans un conteneur Docker, accessible depuis le conteneur Flask via le réseau Docker interne.

### Avantages

- Persistance des données entre les redémarrages (volumes Docker).
- Séparation claire entre la logique applicative (API) et le stockage (DB).
- Environnement reproductible sur n’importe quelle machine avec Docker et Docker Compose.
- Alignement avec les pratiques DevOps modernes (services isolés, config externalisée).
​
### Paramètres de connexion

- Les paramètres de connexion (host, port, nom de base, utilisateur, mot de passe) sont définis via des variables d’environnement.
- Docker Compose injecte ces variables dans les conteneurs, par exemple dans un fichier docker-compose.yml avec environment: pour les services.

### Exemple de variables (à modifier) :

- `DB_HOST=db` -> La localisation (ici docker)
- `DB_PORT=5432` -> Le port 
- `DB_NAME=rpg_quests` -> Le nom
- `DB_USER=quests_user` -> L'utilisateur
- `DB_PASSWORD=supersecret` -> Le mot de passe

Cela permet d’éviter de stocker des secrets en clair dans le code source.

## 6. Docker 

La conteneurisation permet d’exécuter l’API Flask, la base de données et éventuellement le frontend dans des conteneurs isolés, mais orchestrés ensemble avec Docker Compose.
​
### Objectifs

- Fournir un environnement de dev et de run identique pour tous (Dev/Intégration/Prod).
- Simplifier le lancement du projet : une seule commande (docker compose up) pour démarrer tous les services.
- Appliquer des bonnes pratiques DevSecOps dans les images (taille réduite, dépendances maîtrisées, moindre privilège).

### Organisation

- `Dockerfile` pour l’API Flask :
  - Image de base Python officielle (ici: python:3.9).
  - Installation des dépendances via requirements.txt
  - Utilisation d’un utilisateur non-root dans le conteneur.
  - Exposition du port (ici: 5000) et commande flask run.

- `docker-compose.yml` :
  - Service api (image buildée depuis le Dockerfile, env DB_*).
  - Service db (env de base et volume pour les données).


## 7. Github Action

GitHub Actions est utilisé pour automatiser les étapes clés du cycle de vie et nous l'avons utilisé ici principalement pour réaliser les tests sécurité.
​
### Rôle de la CI/CD

 - `CI (Continuous Integration)` :
    - Lancer les tests unitaires et/ou d’intégration à chaque push ou pull request.
    - Vérifier la qualité du code (formatage, lint).

- `CD (Continuous Delivery/Deployment)` :
    - Builder l’image Docker de l’API Flask.

## 8. Les failles

Grâce à bandit, nous avons reperé certaines failles que nous avons classé par sévérité : 

### HIGH

  - [CWE-94](https://cwe.mitre.org/data/definitions/94.html)
      - Il semble qu'une application Flask soit exécutée avec debug=True, ce qui expose le débogueur Werkzeug et permet   l'exécution de code arbitraire.

### MEDIUM

  - [CWE-605](https://cwe.mitre.org/data/definitions/605.html)
      - Liaison possible à toutes les interfaces. (host="0.0.0.0")
   
### LOW

  - [CWE-703](https://cwe.mitre.org/data/definitions/703.html)
      - Utilisation d'assertion détectée. Le code inclus sera supprimé lors de la compilation en bytecode optimisé.


## 9. Notice du jeu 
Notre jeu fonctionne de telle sorte : 

## Menu d'arrivée 

Lors du lancement du site, vous allez arriver sur une page "Création du personnage"
C'est ici qu'il va falloir que vous choisisiez votre pseudo et votre personnage.
Vous aurez le choix entre : 
  - Guerrier = PV élévés, attaque forte.
  - Mage = Sorts puissants, faibles défense.
  - Archer = Dégâts critiques élevés, rapide.

## Menu de jeu 
### Partie Gauche

C'est l'endroit où vous voyez votre personnage.
Vous pouvez ainsi savoir :
  - Votre pseudo
  - Votre niveau
  - Votre classe (Guerrier/Mage/Archer)
  - Votre or
  - Vos PV
  - Vos stats (ATK/DEF/CHANCE)
  - Votre barre d'XP
  - Votre inventaire

### Partie Centrale

Ici, vous pouvez interragir avec le menu de quêtes. 
(C'est ici qu'intervient le CRUD vu précédement)

Vous disposez de différents choix :
  - Voir une quête aléatoire
  - Accepter la quête
  - Modifier la quête
  - Créer une nouvelle quête
  - Supprimer 

Régles : 
  - Une seule quête à la fois.
  - Tu ne peux accepter qu'une seule fois la quête
  - Une nouvelle quête vaut 8xp
  - Vous pouvez supprimer une quête de la base de donnée
  - Vous gagnez +20 or à chaque niveau

Vous disposez également d'une boutique : 
  - Potion (10 or) = +40 PV
  - Kit de réparation (15 or) = +20PV et +1 DEF au prochain combat
  - Pierre magique (25 or) = Double XP pendant 5 min


### Partie Droite

Vous avez également la possibilité de réaliser un combat contre un monstre.
Il vous suffira de cliquer sur le bouton.
Attention ! Si le monstre vous tue, vous perdrez de l'or !




