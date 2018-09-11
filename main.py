import uuid

import aiohug
from aiohug.swagger.handlers import routes as swagger_routes
from aiohug import swagger
from aiohttp import web
from marshmallow import Schema, fields

routes = aiohug.RouteTableDef()


class RequestSchema(Schema):
    nickname = fields.String()
    first_name = fields.String()
    age = fields.Int()


class ResponseSchema(RequestSchema):
    id = fields.UUID()


@swagger.spec(tags=['user'])
@swagger.response(201, schema=ResponseSchema, description="User creation")
@swagger.response(409,  description="Conflict")
@routes.post("/users/")
async def create_user(body: RequestSchema) -> ResponseSchema:
    """
    http --json POST  http://localhost:8080/users/ nickname=test

    :param body:
    :return:
    """
    body["id"] = str(uuid.uuid4())
    return 201, body


@swagger.spec(tags=['user'], response_codes=[404])
@swagger.response(200, schema=ResponseSchema)
@routes.get("/users/{uuid}/")
async def get_user(uuid: fields.UUID(), version: fields.Int() = 1) -> ResponseSchema:
    return {
        "id": str(uuid),
        "nickname": "random",
        "first_name": "random",
        "age": 15,
        "version": version
    }


app = web.Application()
app.add_routes(routes)
app.add_routes(swagger_routes)

if __name__ == "__main__":
    web.run_app(app)
