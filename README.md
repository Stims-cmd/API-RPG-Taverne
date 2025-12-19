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
- Une quête acceptée devient "active"
- Une quête peut être modifiée une seule fois

### La récompense :

- A une valeur de base
- Ne peut jamais dépasser 2 × la récompense de départ
- Est randomisée lors de la modification

## 4. Endpoints de l'API

### GET 
- `GET /quests` -> Pour récupérer les quêtes

### POST 
- `POST /quests` -> Pour créer une nouvelle quête 

### PATCH 
- `PATCH /quests/{id}` -> Pour modifier la quête 

### DELETE 
- `DELETE /quests/{id}` -> Pour supprimer la quête 

#### Toutes les données sont échangées au format ` JSON `

## 5. Base de données

La base de données utilisée est une base SQL, exécutée dans un conteneur Docker.

Ce choix permet :

- La persistance des données entre les redémarrages
- Une séparation claire entre l’application et le stockage
- Une exécution reproductible sur n’importe quelle machine
- Une cohérence avec les pratiques DevOps modernes

Les paramètres de connexion à la base (nom, utilisateur, mot de passe) sont :

- Définis via des variables d’environnement

- Injectés par Docker Compose

- Jamais stockés en clair dans le code
