FROM php:7.4-cli

# add a user for runtime
RUN echo Y | adduser runner

# copy pashmak interpreter binary
COPY ./pashmak-binary /bin/pashmak
RUN chmod +x /bin/pashmak
RUN pashmak -v

# copy src
COPY ./app /app
WORKDIR /app

CMD ["php", "-S", "0.0.0.0:80"]
