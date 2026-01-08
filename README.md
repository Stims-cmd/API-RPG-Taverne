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

### Règles de gestion

- Une seule quête peut être active à la fois
- 

### L'organisation du jeu :

- 

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

​



