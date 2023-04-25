FROM python

RUN mkdir /todo
COPY protobufs/ /service/protobufs/
COPY todo/ /service/todo/
WORKDIR /service/todo

EXPOSE 50051
ENTRYPOINT [ "python", "todoservice.py" ]