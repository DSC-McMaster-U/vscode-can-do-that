////////////////////////
////// Navigation //////
////////////////////////

// code folding
function foobar(start_val) {
  function foo(val) {
    for (i = 0; i < 10; i++) {
      val += i
      console.log(val)
    }
    return val
  }

  function bar(val) {
    if (val < 0) {
      return 0
    }
    return val
  }

  return bar(foo(start_val))
}
foobar(10)

// go to definition [cmd + click]
console.log("hello world");
console.log(fib(10));

import { some_function } from './some_script.js';
console.log(some_function());

// go to symbol in editor [cmd + shift + o]
// lets go to the fib symbol

// go to symbol in workspace [cmd + t]
// lets go to the some_function symbol

// go to line

// go back

// go forward



///////////////////////////////////////////////
////// Intellisense, Linting, Formatting //////
///////////////////////////////////////////////

// hover over definition for intellisense
console.log(fib(10));

// intellisense completions
console

// linting
// write code with syntax error here

// rename symbol
var sub = 10;
sub *= 2;
console.log(sub);
function subtract(a, b) {
  return a - b;
}
sub = subtract(10, 2);
console.log(sub);

// format document
const readline = require("readline");
const rl =         readline.createInterface({
   input: process.stdin,output: process.stdout,
});
rl.question   ( "what's your name? ", greeting );
function greeting(name) {
            console.log("hello " + name);       rl.close();
}



////////////////////
////// Search //////
////////////////////

// search in file (cmd + f)

// search no capitalization

// search exact

// search regex

// search and replace

// search in workspace (cmd + shift + f)




/**
 * Computes the nth fibonnaci number using a naive recursive approach.
 *
 * @param   {Number} n  The fibonacci number to compute.
 * @return  {Number}    The nth fibonacci number.
 */
function fib(n) {
  if (n == 0) return 0;
  else if (n == 1) return 1;
  else return fib(n - 1) + fib(n - 2);
}
