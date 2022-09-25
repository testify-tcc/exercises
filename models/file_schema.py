from typing import Dict
from models.file_schema_type import FileSchemaType


class FileSchema():
  fileName: str
  type: FileSchemaType

  def __init__(self, fileSchemaJson: Dict) -> None:
    self.fileName = fileSchemaJson['fileName']
    self.type = FileSchemaType(fileSchemaJson['type'])

