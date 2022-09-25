from typing import Dict, List, Set, Union

from models.processed_section_definition import ProcessedSectionDefinition
from models.processed_exercise_definition import ProcessedExerciseDefinition
from services.section_definitions_service import SectionDefinitionsService
from services.exercise_definitions_service import ExerciseDefinitionsService

FILES_DIRECTORY_NAME = "files"
DEFINITION_FILE_NAME = "definition.json"
DESCRIPTION_FILE_NAME = "description.md"

class DefinitionService():
  def __init__(
    self,
    exerciseDefinitionsService: ExerciseDefinitionsService,
    sectionDefinitionsService: SectionDefinitionsService,
  ) -> None:
    self.exerciseDefinitionsService = exerciseDefinitionsService
    self.sectionDefinitionsService = sectionDefinitionsService

  def processDefinitions(self) -> Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]]:
    definitionIds: Set[str] = set()
    definitionPositions: Dict[str, int] = dict()
    definitionsMap: Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]] = dict()
    
    self.exerciseDefinitionsService.processExerciseDefinitions(
      definitionsMap,
      definitionIds,
      definitionPositions
    )

    self.sectionDefinitionsService.processSectionDefinitions(
      definitionsMap,
      definitionIds,
      definitionPositions
    )

    definitions = self.getDefinitionList(
      definitionIds,
      definitionPositions,
      definitionsMap
    )
    
    return {
      'map': definitionsMap,
      'list': definitions
    }

  def getDefinitionList(
    self,
    definitionIds: Set[str],
    definitionPositions: Dict[str, int],
    definitionsMap: Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]],
  ) -> List[Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]]:
    definitions = [definitionsMap[definitionId] for definitionId in definitionIds]
    definitions.sort(key=lambda definition: definitionPositions[definition.id])
    return definitions
