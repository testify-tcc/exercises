from typing import Dict, List


class SectionDefinition():
  id: str
  panelLabel: str
  exerciseIds: List[str]

  def __init__(self, sectionDefinitionJson: Dict) -> None:
    self.id = sectionDefinitionJson['id']
    self.panelLabel = sectionDefinitionJson['panelLabel']
    self.exerciseIds = sectionDefinitionJson['exercisesIds']
