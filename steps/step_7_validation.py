import aiohug
from aiohttp import web
from marshmallow import fields


def create_app():
    routes = aiohug.RouteTableDef()

    @routes.get("/number/{number}/")
    async def return_number(number: fields.Int()):
        return {"number": number}

    app = web.Application()
    app.add_routes(routes)

    return app


async def test_app(test_client):
    client = await test_client(create_app())

    number = "not-a-valid-integer"
    resp = await client.get(f"/number/{number}/")
    assert resp.status == 409
    assert await resp.json() == {
        "data": {"number": ["Not a valid integer."]},
        "status": "error",
    }
