# Designing Contracts

Contracts establish what the class requires as pre-conditions, post-conditions and what invariants always hold for the class.

## Pre-conditions and post-conditions

Pre-conditions are basically conditions that need to be satisfied for the method to run properly. Post-conditions are what the method guarantees as outcomes.

### Strong and weak pre- and post-conditions

Sometimes accepting values that don't satisfy the pre-conditions as inputs can be an advantage for some projects. In that case the program would handle these values and not throw errors. We call it a weaker pre-condition. The advantage of using such is that is easier to use the class on other parts of the project, because the callers wouldn't need to handle exceptions.

The same can happen for post-conditions. Weaker post-conditions allow methods to return values that don't satisfy the conditions, instead of throwing exceptions. That way, it'd be the caller's job to handle the erroneous values returned.

## Invariants

An invariant is a condition that holds before and after a method's execution.
