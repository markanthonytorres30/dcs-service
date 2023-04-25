FROM python

RUN mkdir /todo
COPY protobufs/ /service/protobufs/
COPY todo/ /service/todo/
WORKDIR /service/todo
ADD wait-for-mysql.sh /tmp/
ADD wait_for_mysql.py /tmp/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/todoservice.proto
RUN python -m pip install -r mysql_requirement.txt

EXPOSE 50051
ENTRYPOINT [ "python", "todoservice.py" ]