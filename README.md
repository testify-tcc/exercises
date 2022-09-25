# Testify

The Testify goal is to help developers learn about software testing in practice. We recommend using the platform along with Mauricio Aniche's book Effective Software Testing: A Developer's Guide, which is the base for the exercises.

# Server

This server holds the platform's exercise definitions. Its purpose is to define exercises in a easier and understandable way, so users can make suggestions via pull requests.

# Sections

A set of exercises. They have a brief description about the section and a list of exercises.

# Exercises

Exercises have in fact the code and test files, the environments they can run (e.g. javascript + jest) and also a brief description.

# Step by step to create an exercise definition

A directory must be created `/definitions/exercises/<exercise-directory-name>`.

## Types

### TestEnvironmentID

A TestEnvironmentID refers to an existent environment that's available to be used in the platform. You can check the available test environments on this [repository](https://github.com/testify-tcc/environments).

### ExerciseFileDefinition

#### Structure

##### Fields

| Field      | Type          | Description                                                                               |
| ---------- | ------------- | ----------------------------------------------------------------------------------------- |
| `fileName` | `String`      | Refers to a file defined in the same directory as the exercise definition.                |
| `type`     | `CODE / TEST` | The type `CODE` represents the file that will be tested and `TEST` the actual test files. |

##### Example

```json
{
  "fileName": "sum.js",
  "type": "CODE"
}
```

## Definition file

Inside the created directory you must add `definition.json` file.

### Fields

| Field                 | Type                                                    | Description                                                                                                                                                                                                                           |
| --------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                  | `ID`                                                    | This id must be unique between exercises and sections.                                                                                                                                                                                |
| `panelLabel`          | `String`                                                | Testify's interface exercises page has a panel on the left-hand side, where the user can select one. This is the label that will be rendered there. It's important this label to be unique too.                                       |
| `panelPosition`       | `Optional<Integer>`                                     | Position that this exercise will appear in the interface left-hand panel. If the exercise is part of a section, the value will be relative to the section exercises only. If not set, the section will be put in the latest position. |
| `testingEnvironments` | `Array<TestEnvironmentID>`                              | List of environments available for this exercise.                                                                                                                                                                                     |
| `fileSchemasMap`      | `Map<TestEnvironmentID, Array<ExerciseFileDefinition>>` | A map that defines exercises based on test environments.                                                                                                                                                                              |
| `testCommandsMap`     | `Map<TestEnvironmentID, String>`                        | A map that defines commands to run the exercise tests based on test environments.                                                                                                                                                     |

### Example

```json
{
  "id": "sample::sum",
  "panelLabel": "Sum",
  "panelPosition": 1,
  "testEnvironments": ["javascript-jest", "typescript-jest"],
  "fileSchemasMap": {
    "javascript-jest": [
      {
        "fileName": "sum.js",
        "type": "CODE"
      },
      {
        "fileName": "sum.test.js",
        "type": "TEST"
      }
    ],
    "typescript-jest": [
      {
        "fileName": "sum.ts",
        "type": "CODE"
      },
      {
        "fileName": "sum.test.ts",
        "type": "TEST"
      }
    ]
  },
  "testCommandsMap": {
    "javascript-jest": "jest",
    "typescript-jest": "jest"
  }
}
```

## Description

After creating the definition file, you should create a description (`description.md`). The description must be written in Markdown and it's mandatory, to create a better experience for the users.

# Step by step to create a section definition

A directory must be created `/definitions/sections/<section-directory-name>`. Please keep in mind that a section needs to have exercises.

## Definition file

Inside the created directory you must add `definition.json` file.

### Fields

| Fields          | Type                | Description                                                                                                                                                                                     |
| --------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`            | `ID`                | This id must be unique between exercises and sections.                                                                                                                                          |
| `panelLabel`    | `String`            | Testify's interface exercises page has a panel on the left-hand side, where the user can select one. This is the label that will be rendered there. It's important this label to be unique too. |
| `panelPosition` | `Optional<Integer>` | Position that this section will appear in the interface left-hand panel. If not set, the section will be put in the latest position.                                                            |
| `exerciseIds`   | `Array<ID>`         | List of IDs of exercises that will be part of this section                                                                                                                                      |

### Example

```json
{
  "id": "sample",
  "panelLabel": "Sample",
  "panelPosition": 1,
  "exercisesIds": ["sample::sum", "sample::subtract"]
}
```

## Description

After creating the definition file, you should create a description (`description.md`). The description must be written in Markdown and it's mandatory, to create a better experience for the users.
