FROM python:3
COPY . .

RUN chmod a+x run.sh

CMD ["./run.sh"]
