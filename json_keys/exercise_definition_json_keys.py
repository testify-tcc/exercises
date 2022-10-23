from enum import Enum


class ExerciseDefinitionJSONKeys(str, Enum):
  ID = 'id'
  PANEL_LABEL = 'panelLabel'
  DESCRIPTION = 'description'
  PANEL_POSITION = 'panelPosition'
  SOLUTION_DESCRIPTION = 'solution'
  TEST_ENVIRONMENTS = 'testEnvironments'
  TEST_COMMANDS_MAP = 'testCommandsMap'
  FILE_SCHEMAS_MAP = 'fileSchemasMap'
