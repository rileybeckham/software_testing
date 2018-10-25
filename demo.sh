#!/usr/bin/env bash

# This script demonstrates using the shunting_yard module as a command line
# application to convert infix expressions to postfix. It could also serve as
# the basis for a simple set of manual (or automated, with a bit of effort)
# functional tests.

function demo() {
    local infix="$1"
    local postfix=$(python3 -m shunting_yard "$infix")
    echo "Infix:   $infix"
    echo "Postfix: $postfix"
}

demo "1 + 2"
demo "2 + 3 * 5"
demo "4 * 6 + 8"
demo "(1 + 2) * 4"
