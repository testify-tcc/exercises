from bootstrap import bootstrap
from dependency_container import definitionsService

app = bootstrap()

@app.get("/")
def getExercises():
  return definitionsService.processDefinitions()
    