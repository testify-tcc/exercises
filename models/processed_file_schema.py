from typing import Dict
from models.file_schema_type import FileSchemaType


class ProcessedFileSchema():
  fileName: str
  initialContent: str
  type: FileSchemaType

  def __init__(self, fileName: str, initialContent: str, type: FileSchemaType) -> None:
    self.type = type
    self.fileName = fileName
    self.initialContent = initialContent

  def toJson(self) -> Dict:
    return {
      'type': self.type,
      'fileName': self.fileName,
      'initialContent': self.initialContent,
    }
