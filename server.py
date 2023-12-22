import grpc
import asyncio
from proto.build import avatarex_pb2, avatarex_pb2_grpc
import dotenv
import os
from methods import form, profile, signin, signup, signout, webhook_event, webhook_activate, webhook_deactivate

dotenv.load_dotenv()
host = os.getenv("HOST")


class AvatarexServicer(avatarex_pb2_grpc.AvatarexServiceServicer):
    async def Signup(self, request, context):
        return signup.execute(request)

    async def Signin(self, request, context):
        return signin.execute(request)

    async def Profile(self, request, context):
        return profile.execute(request)

    async def Signout(self, request, context):
        return signout.execute(request)

    async def Form(self, request, context):
        return form.execute(request)

    async def WebhookActivate(self, request, context):
        return webhook_activate.execute(request)

    async def WebhookDeactivate(self, request, context):
        return webhook_deactivate.execute(request)

    async def WebhookEvent(self, request, context):
        return webhook_event.execute(request)


async def serve():
    server = grpc.aio.server()
    avatarex_pb2_grpc.add_AvatarexServiceServicer_to_server(AvatarexServicer(), server)
    server.add_insecure_port(host)
    await server.start()
    print("Server started. Listening on port 50051.")
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        await server.stop(0)


if __name__ == "__main__":
    asyncio.run(serve())
