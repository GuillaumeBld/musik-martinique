FROM python:3.12-alpine
WORKDIR /app
COPY server.py .
COPY site ./site
VOLUME /data
ENV PATTERNS_FILE=/data/patterns.json PORT=80
EXPOSE 80
CMD ["python3", "server.py"]
