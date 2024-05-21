//arrays in javascript are similar to those in python
/* 
use of indexing
.pop() to remove the lasst element in an array
.push()
.unshift() used to add an item at the front of the array
.shift() remove an item from an array
.indexOf() return the index position of an element if found in array, if not returns -1 
.length : to get the size of an array property
*/

let birds = ["owl", "Eagle", "Parrot", "Falcon"];
console.log(typeof(birds));//returns an object
//to check if it's an array use the following:
console.log(Array.isArray(birds));//return true 

//indexing in arrays
console.log("The birds array");
console.log(birds);
console.log(`the index 0 in the array birds is ${birds[0]}`);
//arrays are mutable
birds[2] = "Vulture";
console.log("Replacing the value at index 2 now birds");
console.log(birds);
//push()
birds.push("Sparrow");
console.log("After adding sparrow bird in birds return :");
console.log(birds);
//pop()
console.log(`Before removing ${birds}`);
birds.pop();
console.log(`After using pop  ${birds}`);
//unshift() add fist index
birds.unshift("Sparrow");
console.log(birds);
//shift() //remove first item
birds.shift(birds);
console.log()
//indexOf() return index of given argument
console.log(birds.indexOf("Eagle"));


//Exercise 4:
colors = ["red", "green", "blue"];
console.log(colors);
//adding black to last index
colors.push("black");
console.log(colors);
//remove red
colors.shift();
console.log(colors);
//swap position of green and blue
colors[0] = colors[1];
colors[1] = "green";
console.log("After swapping :")
console.log(colors);
//add the color 'yellow' on the first index of the array,
colors.unshift("yellow");
console.log(colors);