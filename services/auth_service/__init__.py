from main import app


@app.post("/api/user/signup")
async def user_signup():
    return {"abc": "123"}
