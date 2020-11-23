FROM python:3.9-buster

# install pyinstaller
RUN pip3 install pyinstaller

# compile program
RUN mkdir /tmp/pashmak-src
WORKDIR /tmp/pashmak-src
RUN git clone https://github.com/parsampsh/pashmak.git src
WORKDIR /tmp/pashmak-src/src
RUN git branch installation $(git describe --abbrev=0)
RUN git checkout installation
RUN make all
RUN make
RUN cp ./dist/pashmak /pashmak

FROM php:7.4-apache-buster

# add a user for runtime
RUN echo Y | adduser runner

# copy pashmak interpreter binary
COPY --from=0 /pashmak /bin/pashmak
RUN chmod +x /bin/pashmak

# config apache
RUN echo 'export APACHE_RUN_USER=runner' >> /etc/apache2/envvars
RUN echo 'export APACHE_RUN_GROUP=runner' >> /etc/apache2/envvars

# copy src
COPY ./app /var/www/html
WORKDIR /var/www/html
