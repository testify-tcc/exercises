from enum import Enum


class SectionDefinitionJSONKeys(str, Enum):
  ID = 'id'
  PANEL_LABEL = 'panelLabel'
  PANEL_POSITION = 'panelPosition'
  EXERCISE_IDS = 'exercisesIds'
