////// Navigation //////

// cmd + click navigating
console.log("hello world")
console.log(fib(10))

// go to symbol in editor [VERY VERY USEFUL]

// go to symbol in workspace [VERY VERY USEFUL]

// go to line

// cursor undo: go to previous cursor position



////// Intellisense, Linting, Formatting //////

// hover over definition for intellisense

/**
 * Computes the nth fibonnaci number using a naive recursive approach.
 * 
 * @param   {Number} n  The fibonacci number to compute.
 * @return  {Number}    The nth fibonacci number.
 */
function fib(n) {
    if (n <= 1)
        return 1
    return fib(n - 1) + fib(n - 2)
}
console.log(fib(10))


// intellisense completions
console


// linting
console.log(fib(10, 20, 40))


// refactor name
var sub = 10
sub *= 2
console.log(sub)

function subtract(a, b) {
    return a - b
}

sub = subtract(10, 2)
console.log(sub)


// format document
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("what's your name? ",          greeting);

function greeting(name) {console.log("hello "  +   name); 
rl.close()};



////// Search //////

// search in file (cmd + f)

// search no capitalization

// search exact

// search regex

// search and replace

// search in workspace (cmd + shift + f)




// view markdown preview
