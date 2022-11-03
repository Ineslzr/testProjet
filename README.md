# testProjet
[![CircleCI](https://img.shields.io/circleci/build/gh/Ineslzr/WorldTour/main?logo=CircleCi&style=flat-square)](https://app.circleci.com/pipelines/github/Ineslzr/WorldTour) [![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=Ineslzr_testProjet&metric=alert_status)](https://sonarcloud.io/dashboard?id=Ineslzr_testProjet) 

## Prérequis
Pyhton - 
NodeJS -
pip -
MAMP, Wamp ou XAMPP

## Installation
Récupérez le code source de l'application en utilisant la commande **git clone** ci-dessous ou en téléchargeant le zip.

```cmd
git clone git@github.com:Ineslzr/testProjet.git
```

Si vous ne parvenez pas à cloner le projet, vérifiez que vous avez bien généré votre clef ssh.

## Installation de la base de données

1. Lancez Mamp, Wamp ou Xampp et ouvrez PhpMyAdmin.

2. Dans l'onglet **Comptes utilisateurs**, créez un utilisateur "root" avec comme mot de passe "root" (s'il n'existe pas déjà).

3. Créez une base de données **worldtour** et y importer le fichier **wordltour.sql** trouvable dans le dossier **docs**. Vous devriez voir ensuite toutes les tables.

## Lancement du backend

Effectuez les commandes suivantes dans un terminale :

```cmd
cd backend\api
```

Activez l'environnement

```cmd
.\venv\Scripts\activate
```

Lancez le back

```cmd
cd backend
python run.py
```

Ouvrez ensuite un navigateur et taper l'URL suivante : **http://localhost:5000**

Vous devriez voir :

![lancement_back](docs/lancement_back.png)


## Lancement du frontend

Ouvrez un second terminale et tapez ces 2 commandes :

```cmd
cd web
npm start
```

Si tout se passe bien, le navigateur va s'ouvrir de lui même.

**Et voilà ! L'application devrait être lancée.**

