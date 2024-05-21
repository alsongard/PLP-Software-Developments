console.log(10 - 7);
console.log(`The square of 3 is ${3**2}`);
console.log(`The division of 3 by 2 is ${3/2}`); //returns a decimal number 1.5
console.log(`The division of 10 by 3 is ${10 % 3}`); //returns a decimal number 1.55

//prefix and postfix in incrementing numbers
//prefix:>
let my_num = 3;
let answer = ++my_num;
console.log(answer);//in prefix the operator increments the value and returns it
//postfix
let my_num1 = 5;
console.log(my_num1++);//the value is still five 
console.log(my_num1);//  the value has been incremented to six

//for subtraction|decrement in 
//prefix(before)
let my_num2 = 10;
console.log(--my_num2);
//postfix(after)
let my_num3 = 20;
console.log(my_num3--);//will return 20
console.log(my_num3);//will return 19