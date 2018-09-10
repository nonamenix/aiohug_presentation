import aiohug
from aiohttp import web
from marshmallow import Schema, fields


def create_app():
    routes = aiohug.RouteTableDef()

    class RequestSchema(Schema):
        name = fields.Str()
        count = fields.Int()

    @routes.get("/hello/")
    async def hello(body: RequestSchema):
        return web.Response(text=f"Hello, {body['name']}\n" * body["count"])

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    app = create_app()
    client = await test_client(app)
    resp = await client.get("/hello/", json={"name": "world", "count": 5})
    assert await resp.text() == ("Hello, world\n" * 5)
