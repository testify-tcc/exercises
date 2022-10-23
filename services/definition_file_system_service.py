import json

from typing import Dict

DEFINITION_FILE_NAME = "definition.json"
DESCRIPTIONS_DIR_NAME = "descriptions"
SOLUTION_DESCRIPTIONS_DIR_NAME = "solutions"
SECTION_DESCRIPTION_FILE_NAME = "description.md"

class DefinitionFileSystemService():
  def getSectionDescription(self, definitionDirPath: str) -> str:
    descriptionFile = open(f"{definitionDirPath}/{SECTION_DESCRIPTION_FILE_NAME}")
    description = descriptionFile.read()
    descriptionFile.close()
    return description

  def getExerciseDescription(self, definitionDirPath: str, descriptionFileName: str) -> str:
    descriptionFile = open(f"{definitionDirPath}/{DESCRIPTIONS_DIR_NAME}/{descriptionFileName}")
    description = descriptionFile.read()
    descriptionFile.close()
    return description

  def getDefinitionJson(self, definitionDirPath: str) -> Dict:
    definitionFile = open(f"{definitionDirPath}/{DEFINITION_FILE_NAME}")
    definitionJson = json.load(definitionFile)
    definitionFile.close()
    return definitionJson

  def getExerciseSolutionDescription(self, definitionDirPath: str, solutionDescriptionFileName: str) -> str:
    solutionDescriptionFile = open(f"{definitionDirPath}/{SOLUTION_DESCRIPTIONS_DIR_NAME}/{solutionDescriptionFileName}")
    solutionDescription = solutionDescriptionFile.read()
    solutionDescriptionFile.close()
    return solutionDescription
