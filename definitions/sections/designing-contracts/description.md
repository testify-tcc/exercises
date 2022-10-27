# Designing Contracts

Contracts establish what the class requires as pre-conditions, post-conditions and what invariants always hold for the class.

## Pre-conditions and post-conditions

Pre-conditions are basically conditions that need to be satisfied for the method to run properly. Post-conditions are what the method guarantees as outcomes.

### Strong and weak pre- and post-conditions

Sometimes accepting values that don't satisfy the pre-conditions as inputs can be an advantage for some projects. In that case the program would handle these values and not throw errors. We call it a weaker pre-condition. The advantage of using such is that is easier to use the class on other parts of the project, because the callers wouldn't need to handle exceptions.

The same can happen for post-conditions. Weaker post-conditions allow methods to return values that don't satisfy the conditions, instead of throwing exceptions. That way, it'd be the caller's job to handle the erroneous values returned.

## Invariants

An invariant is a condition that holds before and after a method's execution.

## Changing contracts

If you've already implemented a method that follows a specific contract and for some reason you decide to change it the first thing you want to do is take a look on the method's users (classes or methods that use the implemented method). You need to do that because they might break with these changes.

We have some rules that can help you:

- Changing a pre-condition to a stronger and more restrictive might break the users, because they might use values as inputs that are not part of this restrictive condition. On the other hand, changing it to a weaker and less restrictive will not break the contract with the clients, because they already handle using more restrictive inputs.
- Changing a post-condition to a weaker and less restrictive might break the users, because they might not expect receiving values out of the scope of the old contract. On the other hand, changing it to a stronger and more restrictive will not break the contract with the clients, because they already deal with the less restrictive outputs.

It's recommended to apply the Liskov Substitution Principle to avoid these type of situations of changing contracts and breaking clients.

### Inheritance rules

If you have a class T and its subclass S:

- The pre-conditions of the subclass S must have equal or weaker pre-conditions of the base class T
- The post-conditions of the subclass S must have equal or stronger post-conditions of the base class T

## Validation

Validation ensures that bad input coming from users doesn't get into the system. It validates the user input and normally returns a message explaining what's wrong.

It's important to understand that defining contracts doesn't remove the need for validation. Both validation and contracts should be done. Normally you do just one to avoid repetition, but sometimes both are needed.
