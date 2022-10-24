# Specification Based Testing

A methodology uses the software requirements as testing input. When the software is implemented, this should be the first technique used on testing. In this case, the implementation is less important than the requirements. This technique can be divided in 7 steps, keep in mind that these steps are not necessarily sequential but iterative, you can go back and forth between them when needed.

## Step 1: Understand the requirement

Get an overall idea of what is going to be tested. Verify things like the inputs, output, types, corner cases etc.

## Step 2: Explore the program

This step is important when the program wasn't written by yourself. So you basically perform a bunch of tests to understand the software behavior and check if it meets your expectations.

## Step 3: Explore possible inputs and outputs, and identify partitions

 This step can be quite hard and you may need to come back here some times. So there're three steps to help you on this:

- Analyze each variable individually and define possible values for each one
- Check the relation between each input variable
- Explore the types of outputs

## Step 4: Identify the boundaries

Analyze the boundaries of all the partitions devised in the step 3.

## Step 5: Devise tests based on partitions and boundaries

Once you've identified the partitions, it's possible that you'd need to define hundreds of tests. Thus it's better to reduce the number of combinations.

## Step 6: Automate the test cases

Basically on this step you need to actually write the code to test you program. Normally we use library or frameworks to help us on this step.

## Step 7: Augment the test suit with creativity and experience

Perform final checks. Although we've used a technique to write tests, it's good to rely on experience and try to test even more cases.
