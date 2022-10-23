from typing import Dict, List

from models.definition_type import DefinitionType
from models.processed_file_schema import ProcessedFileSchema


class ProcessedExerciseDefinition():
  id: str
  panelLabel: str
  type: DefinitionType
  testEnvironments: List[str]
  descriptionsMap: Dict[str, str]
  solutionDescriptionsMap: Dict[str, str]
  testCommandsMap: Dict[str, str]
  fileSchemasMap: Dict[str, List[ProcessedFileSchema]]

  def __init__(
    self,
    id: str,
    panelLabel: str,
    descriptionsMap: Dict[str, str],
    solutionDescriptionsMap: Dict[str, str],
    testEnvironments: List[str],
    fileSchemasMap: Dict[str, List[ProcessedFileSchema]],
    testCommandsMap: Dict[str, str]
  ) -> None:
    self.id = id
    self.panelLabel = panelLabel
    self.descriptionsMap = descriptionsMap
    self.solutionDescriptionsMap = solutionDescriptionsMap
    self.testEnvironments = testEnvironments
    self.fileSchemasMap = fileSchemasMap
    self.testCommandsMap = testCommandsMap
    self.type = DefinitionType.EXERCISE

  def toJson(self) -> Dict:
    jsonFileSchemas = {}

    for testEnvironment, fileSchemas in self.fileSchemasMap.items():
      jsonFileSchemas[testEnvironment] = [fileSchema.toJson() for fileSchema in fileSchemas]

    return {
      'id': self.id,
      'panelLabel': self.panelLabel,
      'descriptionsMap': self.descriptionsMap,
      'solutionDescriptionsMap': self.solutionDescriptionsMap,
      'testEnvironments': self.testEnvironments,
      'fileSchemasMap': jsonFileSchemas,
      'testCommandsMap': self.testCommandsMap,
      'type': self.type.value
    }
