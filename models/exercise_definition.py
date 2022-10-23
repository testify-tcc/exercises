from typing import List, Dict, Union

from utils.constants import MAX_POSITION
from models.file_schema import FileSchema
from json_keys.exercise_definition_json_keys import ExerciseDefinitionJSONKeys


class ExerciseDefinition():
  id: str
  panelLabel: str
  panelPosition: int
  testEnvironments: List[str]
  fileSchemasMap: Dict[str, List[FileSchema]]
  testCommandsMap: Dict[str, str]
  description: Union[str, Dict[str, str]]
  solutionDescription: Union[str, Dict[str, str]]

  def __init__(self, exerciseDefinitionJson: Dict) -> None:
    self.id = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.ID]
    self.panelLabel = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.PANEL_LABEL]
    self.description = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.DESCRIPTION]
    self.panelPosition = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.PANEL_POSITION]
    self.testEnvironments = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.TEST_ENVIRONMENTS]
    self.testCommandsMap = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.TEST_COMMANDS_MAP]
    self.solutionDescription = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.SOLUTION_DESCRIPTION]
    self.fileSchemasMap = dict()

    for testEnvironment, fileSchemaJsons in exerciseDefinitionJson[ExerciseDefinitionJSONKeys.FILE_SCHEMAS_MAP].items():
      self.fileSchemasMap[testEnvironment] = [FileSchema(fileSchemaJson) for fileSchemaJson in fileSchemaJsons]

    if ExerciseDefinitionJSONKeys.PANEL_POSITION in exerciseDefinitionJson:
      self.panelPosition = exerciseDefinitionJson[ExerciseDefinitionJSONKeys.PANEL_POSITION]
    else:
      self.panelPosition = MAX_POSITION
  