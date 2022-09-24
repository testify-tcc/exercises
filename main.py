from bootstrap import bootstrap

app = bootstrap()

@app.get("/")
def getExercises():
    return None
    