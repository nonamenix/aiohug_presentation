from aiohttp import web


def create_app():
    routes = web.RouteTableDef()

    @routes.get("/")
    async def hello(request):
        return web.Response(text="Hello, world")

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    app = create_app()
    client = await test_client(app)
    resp = await client.get("/")
    assert await resp.text() == "Hello, world"
