import aiohug
from aiohttp import web


def create_app():
    routes = aiohug.RouteTableDef()

    @routes.get("/hello/")
    async def hello(name, count=1):
        return web.Response(text=f"Hello, {name}\n" * count)

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    app = create_app()
    client = await test_client(app)
    resp = await client.get("/hello/", params={"name": "world", "count": 5})
    assert await resp.text() == ("Hello, world\n" * 5)
