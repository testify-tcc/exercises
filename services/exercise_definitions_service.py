import os
import env

from typing import Dict, List, Set

from models.file_schema import FileSchema
from models.exercise_definition import ExerciseDefinition
from models.processed_file_schema import ProcessedFileSchema
from models.processed_exercise_definition import ProcessedExerciseDefinition
from services.definition_file_system_service import DefinitionFileSystemService

FILES_DIRECTORY_NAME = "files"

class ExerciseDefinitionsService():
  def __init__(self, definitionFileSystemService: DefinitionFileSystemService) -> None:
    self.definitionFileSystemService = definitionFileSystemService

  def processExerciseDefinitions(
    self,
    definitionsMap: Dict[str, ProcessedExerciseDefinition],
    definitionIds: Set[str],
    definitionPositions: Dict[str, int],
  ) -> Set[str]:
    exerciseDirs = self.getExerciseDirs()

    for exerciseDir in exerciseDirs:
      exerciseDirPath = f"{env.EXERCISES_PATH}/{exerciseDir}"

      exerciseDescription = self.definitionFileSystemService.getDescription(exerciseDirPath)
      exerciseDefinition = ExerciseDefinition(self.definitionFileSystemService.getDefinitionJson(exerciseDirPath))

      exerciseId = exerciseDefinition.id

      if exerciseId in definitionsMap:
        raise Exception('Exercise IDs must be unique')

      processedFileSchemasMap = self.processFileSchemasMap(
        exerciseDirPath,
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

  def getExerciseDirs(self):
    return next(os.walk(env.EXERCISES_PATH))[1]

  def processFileSchemasMap(
    self,
    exercisePath: str,
    fileSchemasMap: Dict[str, List[FileSchema]]
  ) -> Dict[str, List[ProcessedFileSchema]]:
    processedFileSchemasMap: Dict[str, List[ProcessedFileSchema]] = dict()

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
