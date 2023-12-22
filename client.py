import asyncio

import grpc
from proto.build import avatarex_pb2, avatarex_pb2_grpc
import os
import dotenv

dotenv.load_dotenv()
host = os.getenv('HOST')


async def run():
    async with grpc.aio.insecure_channel(host) as channel:
        client = avatarex_pb2_grpc.AvatarexServiceStub(channel)

        # Пример использования метода Signup
        signup_request = avatarex_pb2.SignupRequest(email="test@test.ru", account_id=12121212)
        response = await client.Signup(signup_request)
        print(f"Signup Response: {response}")

        # Далее аналогично для других методов...

if __name__ == "__main__":
    asyncio.run(run())
