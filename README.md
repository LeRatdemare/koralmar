# koralmar
[Site internet](https://nlufuluabo.pythonanywhere.com/) de la chorale de l'Ecole Nationale Supérieure de Cognitique

## Travailler en local

### Pré-requis

* Avoir la version 3.9 de python --> commande `python --version` dans un terminal pour voir la version
* Avoir [MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.4.0&os=windows&cpu=x86_64&pkg=msi&m=icam) installé sur sa machine --> Saisir "MariaDB" dans sa barre de recherche pour savoir si le logiciel est installé

### Lancer l'application locale

0) S'assurer d'avoir déjà configuré l'environnement (Tuto en dessous)
1) Ouvrir un terminal bash et se déplacer dans le dossier racine du projet (celui où se trouve le fichier 'README.md')
2) \[terminal\] Activer l'environnement de travail --> `source env/Script/activate`
3) \[terminal\] Se déplacer dans le dossier du fichier 'manage.py' --> `cd koralmar/`
4) \[terminal\] Lancer l'application --> `python manage.py runserver`
5) Saisir le lien de la console (normalment 'http://127.0.0.1:8000/') dans un navigateur

### Configuration de l'environnement (1ère fois seulement)

1) \[terminal\] Lancer un terminal et se placer dans le dossier souhaité avec la commande `cd`
2) \[terminal\] Récupérer le dépôt en entrant la commande `git clone "https://github.com/LeRatdemare/koralmar.git"`
3) \[terminal\] Se déplacer dans le dossier avec la commande `cd koralmar`
4) \[terminal\] Créer un environnement virtuel avec `python3.9 -m venv env`
5) \[terminal\] Activer l'environnement virtuel avec `source env/Scripts/activate`
6) \[terminal\] Télécharger toutes les dépendances du projet avec `pip install -r requierements.txt`
7) \[MySQL Client\] Se connecter sur le terminal "MySQL client" (disponible si MariaDB est installé) ou créer un identifiant et un mot de passe si besoin. **!!! BIEN LES ENREGISTRER !!!**
8) \[MySQL Client\] Créer une base de donnée MySQL en étant connecté avec la commande `create database koralmar_db;`
9) \[MySQL Client\] Changer la DB active avec la commande `use 'db_name';`
10) \[MySQL Client\] Créer un utilisateur en local pour la DB avec la commande `CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';`
11) \[MySQL Client\] Accorder tous les privilèges sur la DB à l'utilisateur créé avec la commande `GRANT ALL PRIVILEGES ON database_name.\* TO 'user'@'localhost';`

**Enfin ! L'application est presque prête !**

12) Depuis le dossier racine (celui où se trouvent les fichiers 'requirements.txt' et 'README.md' entre autres), aller dans 'koralmar/' puis encore 'koralmar/' et créer le fichier dbinfos.py contenant :
```
host = "localhost"
port = 3306
user = "user"
password = "password"
db_name = "database_name"
```
13) \[terminal\] Appliquer les migrations à la base de donnée ainsi créée avec la commande `python manage.py migrate` (**Remarque :** Il faut être dans le dossier où se trouve le fichier 'manage.py' ou l'un de ses sous-dossiers pour que la commande soit reconnue)
14) \[terminal\] Vous pouvez désormais lancer le serveur avec la commande `python manage.py runserver`

**Le site est lancé !**

15) Saisir le lien de la console (normalment 'http://127.0.0.1:8000/') dans un navigateur

### Lancer l'application locale

1) Ouvrir un terminal bash et se déplacer dans le dossier racine du projet (celui où se trouve le fichier 'README.md')
2) \[terminal\] Activer l'environnement de travail --> `source env/Script/activate`
3) \[terminal\] Se déplacer dans le dossier du fichier 'manage.py' --> `cd koralmar/`
4) \[terminal\] Lancer l'application --> `python manage.py runserver`
5) Saisir le lien de la console (normalment 'http://127.0.0.1:8000/') dans un navigateur