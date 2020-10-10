FROM python:3.6-buster

# install depends


# install pyinstaller
RUN pip3 install pyinstaller

# compile program
RUN mkdir /tmp/pashmak-src
WORKDIR /tmp/pashmak-src
RUN wget https://github.com/parsampsh/pashmak/archive/v1.4.zip -O src.zip
RUN unzip src.zip
WORKDIR /tmp/pashmak-src/pashmak-1.4
RUN git init
RUN make all
RUN make
RUN cp ./dist/pashmak /pashmak

FROM php:7.4-cli

# add a user for runtime
RUN echo Y | adduser runner

# copy pashmak interpreter binary
COPY --from=0 /pashmak /bin/pashmak
RUN chmod +x /bin/pashmak

# copy src
COPY ./app /app
WORKDIR /app

CMD ["php", "-S", "0.0.0.0:80"]
