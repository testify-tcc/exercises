from enum import Enum
from typing import Dict, List

from utils.constants import MAX_POSITION
from json_keys.section_definition_json_keys import SectionDefinitionJSONKeys


class SectionDefinition():
  id: str
  panelPosition: int
  panelLabel: str
  exerciseIds: List[str]

  def __init__(self, sectionDefinitionJson: Dict) -> None:
    self.id = sectionDefinitionJson[SectionDefinitionJSONKeys.ID]
    self.panelLabel = sectionDefinitionJson[SectionDefinitionJSONKeys.PANEL_LABEL]
    self.exerciseIds = sectionDefinitionJson[SectionDefinitionJSONKeys.EXERCISE_IDS]

    if SectionDefinitionJSONKeys.PANEL_POSITION in sectionDefinitionJson:
      self.panelPosition = sectionDefinitionJson[SectionDefinitionJSONKeys.PANEL_POSITION]
    else:
      self.panelPosition = MAX_POSITION
