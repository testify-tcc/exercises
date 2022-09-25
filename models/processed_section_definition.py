from ctypes import Union
from curses import panel
from typing import List

from models.definition_type import DefinitionType
from models.processed_exercise_definition import ProcessedExerciseDefinition


class ProcessedSectionDefinition():
  id: str
  panelLabel: str
  description: str
  type: DefinitionType
  exercises: List[ProcessedExerciseDefinition]

  def __init__(
    self,
    id: str,
    panelLabel: str,
    description: str,
    exercises: List[ProcessedExerciseDefinition]
  ) -> None:
    self.id = id
    self.exercises = exercises
    self.panelLabel = panelLabel
    self.description = description
    self.type = DefinitionType.SECTION
