import json

from typing import Dict

DEFINITION_FILE_NAME = "definition.json"
DESCRIPTION_FILE_NAME = "description.md"

class DefinitionFileSystemService():
  def getDescription(self, definitionDirPath: str) -> str:
    descriptionFile = open(f"{definitionDirPath}/{DESCRIPTION_FILE_NAME}")
    description = descriptionFile.read()
    descriptionFile.close()
    return description

  def getDefinitionJson(self, definitionDirPath: str) -> Dict:
    definitionFile = open(f"{definitionDirPath}/{DEFINITION_FILE_NAME}")
    definitionJson = json.load(definitionFile)
    definitionFile.close()
    return definitionJson
