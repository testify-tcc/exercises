from ctypes import Union
from curses import panel
from typing import Dict, List

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

  def toJson(self) -> Dict:
    return {
      'id': self.id,
      'exercises': [exercise.toJson() for exercise in self.exercises],
      'panelLabel': self.panelLabel,
      'description': self.description,
      'type': self.type
    }
