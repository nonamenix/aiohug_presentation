ws = aiohug.WSHandler()


@ws("hello")  # match message by `type` field
async def hello(name: str, greeting: str = "Hi"):
    """ Just send {"type": "hello", "name": "Lucy", "greeting": "Hi"} """
    return {"text", f"{greeting}, {name}"}


app = create_app()
app.add_routes([web.get('/ws', ws)])

# Schemas
# Base types to swagger schema
