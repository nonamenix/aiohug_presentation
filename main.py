from aiohttp import web


async def hello(request):
    # unnecessary `request` object
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes([web.get("/", hello)])
web.run_app(app)

# Let's test it
