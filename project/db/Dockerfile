FROM postgres:12-alpine


# Extends postgres image adding create.sql commands on init
ADD create.sql /docker-entrypoint-initdb.d
