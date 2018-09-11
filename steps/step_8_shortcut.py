import aiohug
from aiohttp import web
from marshmallow import fields


def create_app():
    routes = aiohug.RouteTableDef()

    @routes.get("/ping/")
    async def return_number():
        return 201, {"msg": "pong"}

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    client = await test_client(create_app())

    resp = await client.get(f"/ping/")
    assert resp.status == 201
    assert await resp.json() == {"msg": "pong"}
