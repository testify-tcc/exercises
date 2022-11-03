# Test-driven development

A technique that boils down to writing tests before writing the code that is tested by them.

## Technique

### Step 1: Think about the requirements and derive tests

The first is to think about the requirements of the program you want to implement. From it you can derive a bunch of tests (e.g. simple, corner and specific cases). List all the tests you could derive.

### Step 2: Select the simplest test you derived

Select the simplest test from the list you've built and write a test based on it. If you run the test it'll most probably fail or not even be compiled, as the functionality is not implemented yet, but that's expected.

### Step 3: Make the test pass

Implement as much production code as needed to make the test you've implemented pass, but nothing more than that.

### Step 4: Stop and reflect

Stop and reflect on what you've done so far. Verify whether it's needed to refactor the production code or improve the test cases

### Step 5: Repeat

After you've done all the first four steps, you might need to repeat all of them if you think it's necessary. That's what TDD is about, by taking babysteps you will reach to a complete and funcional implementation.

But keep in mind that once you're becoming more expert on this technique you may not need to do all these steps for each simple case you thought at the beginning. Also, you can think on more complex test cases in the first step.

## Advantages of using TDD

* Focus on requirements: you implement only what's needed to make the program pass the test
* Control over the pace of writing production code: if you are confident you can start by writing complex tests, but in case you aren't you can start by writing simple tests until you understand the complexity of the requirements
* Quick feedback: every change in the production code will be tested after implemented
* Testable code: after you implement the needed features, you'll already have unit tests for them
* Feedback about design: if the way you've designed a method or class has been creating difficulties when creating tests for it, perhaps you should redesign it.
