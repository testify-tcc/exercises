import env
import json

from typing import Dict, List, Union

from models.processed_exercise_definition import ProcessedExerciseDefinition
from models.processed_section_definition import ProcessedSectionDefinition

class DefinitionsJSONService():
  def readDefinitions(self) -> Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]]:
    exercisesJsonFile = open(env.EXERCISES_JSON_FILE_PATH, "r")
    exercisesJson = json.load(exercisesJsonFile)
    exercisesJsonFile.close()
    return exercisesJson

  def writeDefinitions(
    self,
    definitionsMap: dict[str, ProcessedExerciseDefinition | ProcessedSectionDefinition],
    definitionsList: List[ProcessedExerciseDefinition | ProcessedSectionDefinition]
  ):
    jsonDefinitionsObject = self.getJsonDefinitionObject(definitionsMap, definitionsList);

    with open(env.EXERCISES_JSON_FILE_PATH, "w") as exercisesJsonFile:
      json.dump(jsonDefinitionsObject, exercisesJsonFile)

  def getJsonDefinitionObject(
    self,
    definitionsMap: dict[str, ProcessedExerciseDefinition | ProcessedSectionDefinition],
    definitionsList: List[ProcessedExerciseDefinition | ProcessedSectionDefinition]
  ) -> Dict:
    return {
      'map': self.convertDefinitionsMapToJson(definitionsMap),
      'list': self.convertDefinitionsListToJson(definitionsList)
    }

  def convertDefinitionsMapToJson(
    self,
    definitionsMap: dict[str, ProcessedExerciseDefinition | ProcessedSectionDefinition]
  ) -> Dict:
    jsonDefinitionMap = {}

    for testEnvironment, definition in definitionsMap.items():
      jsonDefinitionMap[testEnvironment] = definition.toJson()

    return jsonDefinitionMap

  def convertDefinitionsListToJson(
    self,
    definitionsList: List[ProcessedExerciseDefinition | ProcessedSectionDefinition]
  ) -> Dict:
    return [definition.toJson() for definition in definitionsList]
