//functions
//to declare a function use the keyword function functionName() {}
function greet(){
    console.log("Hello world welcome to JavaScript functions.");
}
greet();

//parameters
function greetings(name, weather){
    console.log(`Hello there ${name}.`);
    console.log(`It's a ${weather} day.`);
}
greetings("alson","rainy");


//defualt parameters
function sayMe(name="jack"){
    console.log(`His name is ${name}`);
}
//incase no argument is given to the sayMe() function or undefined is given jack is printed, these is called the default value
sayMe();
sayMe(undefined);
sayMe("gard");//given a parameter

//arrangement of the non-default and default parameters
//non-default value came before the default value
function teacherComment(comment, name="Obama"){
    console.log(`Mr. ${name} recommended ${comment} about the student.`);
}
teacherComment("greatly");

//the default value came before the non-default value

function studentGrade(name="James", grade){
    console.log(`${name} average grade is ${grade}.`);
}
studentGrade("A");
//in these case the default value must be passed either as undefined or another stringName

//null = setting an intentional empty value
//undefined = default empty value

function defaultValuesCheck(name="John"){
    console.log(name);
}
defaultValuesCheck(undefined);//using undefined(default value will print John while null result in null(intentional))

//return statement
//the return statement is used to return the result of a function when called
function sum(a, b){
    return a + b;
}
let mysum = sum(10, 12);
console.log(`the sum of 10 and 12 is ${mysum}`);

function checkAge(age){
    if (age >= 20){
        return `You are a valid participant`;
    }
    else if(age  < 15){
        return `Not a valid participant`;
    }
}
console.log(checkAge(5));

//rest parameter it is used to defined a infinite(uncertain) number of elements
function printArguments(...args){
    console.log(args);
}
printArguments("a",1,"b",2,"c",3);
//remember that the ...args keyword should be placed as the last argument.

//arrow functions
//an arrow function is similar function however it adds concise
//always assign an arrow function to a variable and you can later call it by using variableName()
//e.g
let myGreet = (new_name="Sarah")=>{
    console.log(`The new student name is ${new_name}`);
}
myGreet();


//single line and multiline functions

//single line arrow function
const mySum = (num)=> num + 10;
const justPrint = mySum(10)
console.log(justPrint);

//a function with no return value
const noReturn  = ()=> console.log("Hello world, This function has no return value");
noReturn();

//argument keyword in functions
function letSee(){
    console.log(arguments);
}
letSee("hello ", "porshe", 1, 2);
//keyword arguments refers to all the arguments passed on to the function
//these does not apply for the arrow function
// const printArgs = ()=>console.log(arguments);
// printArgs(1, 2, 3);

/*
exercise 7:
Exercise #7
Write a function named calculateSquare() that's used to calculate the area and perimeter of a square shape.
The function accepts one parameter: the side of the square.
The formula to calculate the area is side * side, and the formula to calculate the perimeter is 4 * side.
The output shows the size of the size, the area, and the perimeter as follows:
The square side is 8
*/

function calculateSquare(length){
    let area = length * length;
    let perimeter = length * 4;
    console.log(`The length of the square is ${length} and it's perimeter is ${perimeter} and it's area is ${area}`);
}
calculateSquare(10);