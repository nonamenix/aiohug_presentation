import aiohug
from aiohttp import web
from marshmallow import Schema, fields


def create_app():
    routes = aiohug.RouteTableDef()

    @routes.get("/hello/")
    async def hello():
        return web.json_response(data={"msg": "Hello, world"})

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    app = create_app()
    client = await test_client(app)
    resp = await client.get("/hello/")
    assert await resp.json() == {"msg": "Hello, world"}
