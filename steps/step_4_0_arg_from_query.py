
from aiohttp import web


def create_app():
    routes = web.RouteTableDef()

    @routes.get("/hello/")
    async def hello(request: web.Request):
        # needless got to doc
        name = request.rel_url.query.get("name", "world")
        return web.Response(text=f"Hello, {name}")

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    app = create_app()
    client = await test_client(app)
    resp = await client.get("/hello/", params={"name": "world"})
    assert await resp.text() == "Hello, world"
