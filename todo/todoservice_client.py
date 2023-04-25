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
import asyncio

import grpc
import todoservice_pb2
import todoservice_pb2_grpc

    
# Performs an unary call
async def get_todo_list(stub: todoservice_pb2_grpc.TodoServiceStub,
                                request: todoservice_pb2.TodoRequest) -> None:
    try:
        async for todo in stub.GetTodos(request):
            if not todo:
                print("Server returned incomplete feature")
                return

            print(f"Student List request called.")
            print(todo.task)
    except Exception as e:
        print(e)


async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = todoservice_pb2_grpc.TodoServiceStub(channel)
        print("-------------- GetTodoList --------------")
        await get_todo_list(stub, todoservice_pb2.TodoRequest(request=""))



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(main())
