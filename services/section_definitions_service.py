import os
import env

from typing import Dict, List, Set, Union

from models.section_definition import SectionDefinition
from models.processed_section_definition import ProcessedSectionDefinition
from models.processed_exercise_definition import ProcessedExerciseDefinition
from services.definition_file_system_service import DefinitionFileSystemService


class SectionDefinitionsService():
  def __init__(self, definitionFileSystemService: DefinitionFileSystemService) -> None:
    self.definitionFileSystemService = definitionFileSystemService

  def processSectionDefinitions(
    self,
    definitionsMap: Dict[str, ProcessedSectionDefinition],
    definitionIds: Set[str],
    definitionPositions: Dict[str, int],
  ):
    sectionDirs = self.getSectionDirs()

    for sectionDir in sectionDirs:
      sectionDirPath = f"{env.SECTIONS_PATH}/{sectionDir}"

      sectionDescription = self.definitionFileSystemService.getDescription(sectionDirPath)
      sectionDefinition = SectionDefinition(self.definitionFileSystemService.getDefinitionJson(sectionDirPath))

      sectionId = sectionDefinition.id

      if sectionId in definitionsMap:
        raise Exception('Section IDs must be unique')

      processedExercises = self.getProcessedExercises(
        sectionDefinition.exerciseIds,
        definitionIds,
        definitionPositions,
        definitionsMap,
      )

      definitionIds.add(sectionId)
      definitionPositions[sectionId] = sectionDefinition.panelPosition
      definitionsMap[sectionId] = ProcessedSectionDefinition(
        sectionDefinition.id,
        sectionDefinition.panelLabel,
        sectionDescription,
        processedExercises,
      )

  def getSectionDirs(self):
    return next(os.walk(env.SECTIONS_PATH))[1]

  def getProcessedExercises(
    self,
    exerciseIds: List[str],
    definitionIds: Set[str],
    definitionPositions: Dict[str, int],
    definitionsMap: Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]],
  ) -> List[ProcessedExerciseDefinition]:
    processedExercises: List[ProcessedExerciseDefinition] = []

    for exerciseId in exerciseIds:
      if exerciseId not in definitionsMap:
        raise Exception('Section exercise IDs must exist')

      definitionIds.remove(exerciseId)
      processedExercises.append(definitionsMap[exerciseId])

    processedExercises.sort(key=lambda processedExercise: definitionPositions[processedExercise.id])

    return processedExercises
