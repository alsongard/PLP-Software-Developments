//using logical operators such as AND && and || OR
let fruit = "banana";
if (fruit === "orange" || fruit === "banana"){
    console.log("continue eating healthy fruits");
}

//perform above operation using switch case statement
switch (fruit){
    case ("banana"):
    case ("orange"):
        console.log("You are eating healthy");
        break;
    default:
        console.log("Not eating healthy");
}

/*
Exercise #5

A primary school is giving different rewards based on the student's grade:

    Students that got an A will get a Chocolate
    Students that got a B will get a Cookie
    Students that got a C will get a Candy
    For any other value, print "No reward to give.
*/
grade = "A";
switch(grade){
    case ("B"):
        console.log("You got a B which is good");
        break;
    case ("C"):
        console.log("You got a C which is pass");
        break;
    case ("D"):
        console.log("You got a D which is pass");
        break;
    case ("A"):
        console.log("You got a A which is great");
        break;
    default:
        console.log("You Failed!!!")
}