FROM python:slim
LABEL org.opencontainers.image.authors="bbouazi@yahoo.fr"
# Copie le fichier Python dans l'image
WORKDIR /usr/app/src
COPY main.py /usr/app/src/
RUN chmod +x  /usr/app/src/main.py
# Expose le port 6000 pour la communication
EXPOSE 6000
# Lance le script Python au démarrage du conteneur
CMD ["python3", "/main.py"]
