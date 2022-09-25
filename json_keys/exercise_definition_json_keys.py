from enum import Enum


class ExerciseDefinitionJSONKeys(str, Enum):
  ID = 'id'
  PANEL_LABEL = 'panelLabel'
  PANEL_POSITION = 'panelPosition'
  TEST_ENVIRONMENTS = 'testEnvironments'
  TEST_COMMANDS_MAP = 'testCommandsMap'
  FILE_SCHEMAS_MAP = 'fileSchemasMap'
