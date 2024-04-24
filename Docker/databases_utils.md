# Utilidades para Bancos em Containers

Esta seção visa documentar alguns comandos úteis para tarefas do dia-a-dia com banco de dados em containers.

## Criando Containers para Bancos

Os comandos a seguir são para criação de containers de banco de dados com volumes facilmente identificados (para backups)

### MySQL

1. Criar o volume da dados para ser utilizado (e realizar backup)
``` bash
$ docker volume create database_mysql
```

2. Criação do Container MySQL, linkando ao volume
``` bash
$ docker run -p 3306:3306 \
    --name mysql_dockerzinho \
    -v database_mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=admin \
    -d mysql:5.6 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci
```

### PostgreSQL

1. Criar o volume da dados para ser utilizado (e realizar backup)
``` bash
$ docker volume create database_postgres
```

2. Criação do Container PostgreSQL, linkando ao volume
``` bash
$ docker run -p 5435:5432 \
     --name postgres_dockerzinho \
     -v database_postgres:/var/lib/postgresql/data \
     -e POSTGRES_PASSWORD=admin \
     -d postgres
```
3. Criação do PGadmin para conectar no banco
``` bash
$ docker volume create database_pgadmin
$ docker run -p 5050:80 \
     --name pgadmin_dockerzinho \
     -v database_pgadmin:/var/lib/pgadmin \
     --env PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org \
     --env PGADMIN_DEFAULT_PASSWORD=admin
     -d dpage/pgadmin4
```


## Dump de Bases

Os comandos a seguir são voltados para criar dumps de bases e restaurar os mesmos de dentro dos containers.

### MySQL

Para cria um dump das bases:
``` bash
$ docker exec mysql_dockerzinho sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /home/{{user}}/mysql-databases.sql
```

Para restaurar um dump de bases:
``` bash
$ docker exec -i mysql_dockerzinho sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < /home/{{user}}/mysql-databases.sql
```

### PostgreSQL

Para cria um dump de uma base:
``` bash
docker exec -i postgres_dockerzinho /bin/bash -c "PGPASSWORD=admin pg_dump --username postgres {{database_name}}" >  /home/{{user}}/{{database_name}}_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```

Para restaurar um dump de uma base:
``` bash
docker exec -i postgres_dockerzinho /bin/bash -c "PGPASSWORD=admin psql --username postgres {{database_name}}" < /home/{{user}}/{{database_name}}_XXXXXXX.sql
```

Para cria um dump de todas as bases:
``` bash
docker exec -t postgres_dockerzinho pg_dumpall -c -U postgres > dump_$(date +"%Y-%m-%d_%H_%M_%S").sql
```
*Nota:* para reduzir espaço posso utilizar:
``` bash
docker exec -t postgres_dockerzinho pg_dumpall -c -U postgres | gzip > ./dump_$(date +"%Y-%m-%d_%H_%M_%S").gz
```

Para restaurar um dump de todas as bases:
``` bash
cat dump_XXXXXXX.sql | docker exec -i postgres_dockerzinho psql -U postgres
```
*Nota:* Para restaurar um dump de todas as bases (compactadas):
``` bash
gunzip < dump_XXXXXXX.gz | docker exec -i postgres_dockerzinho psql -U postgres
```
