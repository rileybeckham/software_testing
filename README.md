# Shunting-yard Algorithm

This repository contains a simple Python 3 module that implements the
well-known shunting-yard algorithm. This algorithm allows the conversion of a
mathematical expression written using the familiar infix notation into an
equivalent expression written in postfix notation. You can find out more
about this algorithm from the sources below.

  * https://en.wikipedia.org/wiki/Shunting-yard_algorithm
  * http://www.oxfordmathcenter.com/drupal7/node/628

The module, found in `shunting_yard.py` contains a function called
`infixToPostfix`, which implements the basic algorithm, along with a number
of helper functions. I suggest testing each helper function in isolation
since they are written so as not to depend upon one another.

I have included a script called `demo.sh` that provides several small manual
functional test cases and demonstrates how to run the module as a command
line program. This is purely for those who may be interested (and for my own
testing). You don't need to worry about functional testing and you shouldn't
make any changes to the module code.

## Evaluation

I will execute the script called `runtests.sh` to run your unit tests. I have
populated this file with a command that should be sufficient. However, if you
find that you'd like me to run your tests using a different command, simply
modify the script accordingly.

Run the script like this: `./runtests.sh`.

By default, any files that match the pattern `test*.py` where `*` is a
wildcard meaning "anything", will be searched for tests. I have added a
single test for the `tokenize` function as an example to get you started.

I will make several modifications to the module code to introduce bugs in
different functions. Your tests should "catch" these bugs. In other words, if
I add a bug in a given function, one or more of your tests for that function
should fail when I run the tests afterward.

## Unit test Readme

I made a unit test for every function in the shunting_yeard file, and I just 
made them in the file you used tor testing the tokenize funcion, so just by 
running ./runtests.sh will run them all. For functions that have multiple outcomes 
that I deamed would influence other funcions were tested to make sure they would not
 only produce True when it was true but also False when it should be. There is one failure 
and that is becuase the isNumber funcion is not equipped to deal with decimals and
I passed it both an integer and a decimal. Everyother test I made passed. 
