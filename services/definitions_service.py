import env
import os
import json

from typing import Dict, List, Set, Union

from models.exercise_definition import ExerciseDefinition
from models.file_schema import FileSchema
from models.processed_exercise_definition import ProcessedExerciseDefinition
from models.processed_file_schema import ProcessedFileSchema
from models.processed_section_definition import ProcessedSectionDefinition
from models.section_definition import SectionDefinition

FILES_DIRECTORY_NAME = "files"
DEFINITION_FILE_NAME = "definition.json"
DESCRIPTION_FILE_NAME = "description.md"

class DefinitionService():
  def processDefinitions(self) -> Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]]:
    definitionIds: Set[str] = set()
    definitionPositions: Dict[str, int] = dict()
    definitionsMap: Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]] = dict()
    
    self.processExerciseDefinitions(definitionsMap, definitionIds, definitionPositions)
    self.processSectionDefinitions(definitionsMap, definitionIds, definitionPositions)

    definitions = self.getDefinitionList(definitionIds, definitionPositions, definitionsMap)
    
    return {
      'map': definitionsMap,
      'list': definitions
    }

  def processExerciseDefinitions(
    self,
    definitionsMap: Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]],
    definitionIds: Set[str],
    definitionPositions: Dict[str, int],
  ) -> Set[str]:
    exerciseDirs = self.getExerciseDirs()

    for exerciseDir in exerciseDirs:
      exercisePath = f"{env.EXERCISES_PATH}/{exerciseDir}"

      descriptionFile = open(f"{exercisePath}/{DESCRIPTION_FILE_NAME}")
      definitionFile = open(f"{exercisePath}/{DEFINITION_FILE_NAME}")
      
      exerciseDescription = descriptionFile.read()
      exerciseDefinition = ExerciseDefinition(json.load(definitionFile))
      exerciseId = exerciseDefinition.id

      if exerciseId in definitionsMap:
        raise Exception('Exercise IDs must be unique')

      processedFileSchemasMap = self.processFileSchemasMap(
        exercisePath,
        exerciseDefinition.fileSchemasMap
      )

      definitionIds.add(exerciseId)
      definitionPositions[exerciseId] = exerciseDefinition.panelPosition
      definitionsMap[exerciseId] = ProcessedExerciseDefinition(
        exerciseId,
        exerciseDefinition.panelLabel,
        exerciseDescription,
        exerciseDefinition.testEnvironments,
        processedFileSchemasMap,
        exerciseDefinition.testCommandsMap,
      )

      descriptionFile.close()
      definitionFile.close()

  def getExerciseDirs(self):
    return next(os.walk(env.EXERCISES_PATH))[1]

  def processFileSchemasMap(
    self,
    exercisePath: str,
    fileSchemasMap: Dict[str, List[FileSchema]]
  ) -> Dict[str, List[ProcessedFileSchema]]:
    processedFileSchemasMap = dict()

    for testEnvironment, fileSchemas in fileSchemasMap.items():
      processedFileSchemas = []

      for fileSchema in fileSchemas:
        exerciseFile = open(f"{exercisePath}/{FILES_DIRECTORY_NAME}/{fileSchema.fileName}")

        exerciseFileContent = exerciseFile.read()

        processedFileSchemas.append(
          ProcessedFileSchema(
            fileSchema.fileName,
            exerciseFileContent,
            fileSchema.type,
          )
        )

        exerciseFile.close()

      processedFileSchemasMap[testEnvironment] = processedFileSchemas
    
    return processedFileSchemasMap

  def processSectionDefinitions(
    self,
    definitionsMap: Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]],
    definitionIds: Set[str],
    definitionPositions: Dict[str, int],
  ):
    sectionDirs = self.getSectionDirs()

    for sectionDir in sectionDirs:
      sectionPath = f"{env.SECTIONS_PATH}/{sectionDir}"

      descriptionFile = open(f"{sectionPath}/{DESCRIPTION_FILE_NAME}")
      definitionFile = open(f"{sectionPath}/{DEFINITION_FILE_NAME}")

      sectionDescription = descriptionFile.read()
      sectionDefinition = SectionDefinition(json.load(definitionFile))

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

      descriptionFile.close()
      definitionFile.close()

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

  def getDefinitionList(
    self,
    definitionIds: Set[str],
    definitionPositions: Dict[str, int],
    definitionsMap: Dict[str, Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]],
  ) -> List[Union[ProcessedExerciseDefinition, ProcessedSectionDefinition]]:
    definitions = [definitionsMap[definitionId] for definitionId in definitionIds]
    definitions.sort(key=lambda definition: definitionPositions[definition.id])
    return definitions
