import aiohug
from aiohttp import web


def create_app():
    routes = aiohug.RouteTableDef()

    @routes.get("/hello/{name}")
    async def hello(name):
        return web.Response(text=f"Hello, {name}")

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    app = create_app()
    client = await test_client(app)
    resp = await client.get("/hello/world")
    assert await resp.text() == "Hello, world"
