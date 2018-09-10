from unittest.mock import MagicMock

import aiohug
from aiohttp import web
from aiohug.directives import directive


@directive
def redis(request):
    return request.app["redis"]


def create_app():
    routes = aiohug.RouteTableDef()

    @routes.get("/get-from-redis")
    async def return_number(redis):
        return {"value": redis.get("value")}

    app = web.Application()
    _redis = MagicMock(get=lambda name: 5)

    app["redis"] = _redis
    app.add_routes(routes)

    return app


async def test_cast_error(test_client):
    client = await test_client(create_app())

    resp = await client.get("/get-from-redis")
    assert await resp.json() == {"value": 5}
