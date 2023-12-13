FROM python:3.11.4-alpine
RUN apk add --update --no-cache netcat-openbsd
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
ENV HOST=db
ENV DT=postgres
ENV DB_PORT=5432
ENV SK=ikurawebapp
EXPOSE 5000
COPY app ./
RUN sed -i 's/\r$//g' entrypoint.sh && \
    chmod +x entrypoint.sh
# CMD ["waitress-serve", "--listen=*:5000", "app:app"]
ENTRYPOINT ["./entrypoint.sh"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
