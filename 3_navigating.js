////////////////////////
////// Navigation //////
////////////////////////

// code folding TODO

// cmd + click navigating [VERY VERY USEULF]
console.log("hello world");
console.log(fib(10));

import { some_function } from './some_script.js';
console.log(some_function());

// go to symbol in editor [VERY VERY USEFUL]
// lets go to the fib symbol

// go to symbol in workspace [VERY VERY USEFUL]
// lets go to the some_function symbol

// go to line

// cursor undo? (TODO)





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

// find in file (cmd + f)

// find no capitalization

// find exact

// find regex

// find and replace

// find in workspace (cmd + shift + f)




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
