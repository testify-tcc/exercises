from typing import List, Dict

from models.file_schema import FileSchema


class ExerciseDefinition():
  id: str
  panelLabel: str
  testEnvironments: List[str]
  fileSchemasMap: Dict[str, List[FileSchema]]
  testCommandsMap: Dict[str, str]

  def __init__(self, definitionJson: Dict) -> None:
    self.id = definitionJson['id']
    self.panelLabel = definitionJson['panelLabel']
    self.testEnvironments = definitionJson['testEnvironments']
    self.testCommandsMap = definitionJson['testCommandsMap']
    self.fileSchemasMap = dict()

    for testEnvironment, fileSchemaJsons in definitionJson['fileSchemasMap'].items():
      self.fileSchemasMap[testEnvironment] = [FileSchema(fileSchemaJson) for fileSchemaJson in fileSchemaJsons]
  