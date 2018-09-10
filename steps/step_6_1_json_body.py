import aiohug
from aiohttp import web


def create_app():
    routes = aiohug.RouteTableDef()

    @routes.get("/hello/")
    async def hello():
        return {"msg": "Hello, world"}

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    app = create_app()
    client = await test_client(app)
    resp = await client.get("/hello/")
    assert await resp.json() == {"msg": "Hello, world"}
