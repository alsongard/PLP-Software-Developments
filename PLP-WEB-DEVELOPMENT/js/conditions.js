//if statement
//if else statement
//if else if statement
//switch statement

let balance = 7000;
console.log(balance);
if (balance > 5000){
    console.log("You can for a vacation with that money.");
}
//above code will run since the balance is greater thatn 5000

//if(condition) else statement
//else statement is  run only when the if is not run
balance = 3000
console.log(balance);

if (balance > 5000){
    console.log("You can for a vacation with that money.");
}
else{
    console.log("You cannot travel with that money")
}

//else if 
balance = 4000
//travel to dubai is 6000 above
//travel to mombase is 3000 above
console.log(balance);
if (balance >= 6000){
    console.log("Hurray!! You can travel to Dubai");
}
else if(balance  >= 3000){
    console.log("Hurray!! You can travel to Mombase")
}
else{
    console.log("You cannot travel anyware. Stay at Home!!!")
}

//switch case statement
let age = 24
console.log(`His age is ${age}`);
switch(age){
    case 10:
        console.log(`To young for aritificial intelligence ${age}`);
        break;
    case 15:
        console.log(`Avarage age for artificial intelligence ${age}`);
        break;
    case 20:
        console.log(`Good age for these artificial intelligence ${age}`);
        break;
    case 24:
        console.log(`Nice age for computer science, artificial intelligence, cyber security, web development and alx ${age}`);
        break;
    default:
        console.log("No age found in the system.")
}