# Lancer le projet en local

```sh
./start
```

OU

```sh
python ./manage.py runserver
```

# Lancer le docker

```sh
docker build -t django_ludo .
./start --docker
```

# Lancer les test

```sh
./manage.py test
```

# Lancer uniquement un test

```sh
./manage.py test testUnitaire.tests.TestDb.{nom_de_la_fonction}
```
