# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import logging
import math
import time

import grpc

import todoservice_pb2
import todoservice_pb2_grpc
import crud, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()

def map_todos(result):
    response =  todoservice_pb2.TodoResponse()

    if result == None:
        return response 
        
    response.id = result.id
    response.task = result.task
    response.done = result.done
    response.deleted = result.deleted

    return response


class TodoServiceServicer(todoservice_pb2_grpc.TodoServiceServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        """Define db connection here"""
        #self.db = get_db()

    def GetTodos(self, request, context):
        db = next(get_db())
        todolist = crud.get_todo_list(db, request)
        print(f"GetTodos was invoked.")
        if todolist is None:
            print("No result")
            return None
        else:
            print("Has result")
            for todo in todolist:
                output = map_todos(todo)
                print(output.task)
                yield output

        db.close()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todoservice_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoServiceServicer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
