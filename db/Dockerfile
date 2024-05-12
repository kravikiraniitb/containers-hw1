FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD password
ENV MYSQL_DATABASE mydatabase
ENV MYSQL_USER user
ENV MYSQL_PASSWORD password
ADD schema.sql /docker-entrypoint-initdb.d
