i = 0;
while (i < 6){
    console.log(`Value  is ${i}`);
    i++;
}

//coins toss
let isHeads = false;
flips = 0;
while(!isHeads){
    flips++;
    isHeads = Math.random() <  0.5;
}
console.log(`The number of times the coins is tossed it landed in heads is ${flips}`);

//Exercise 6
//half a pryamid of striks
let a = 0;
while (a < 6){
    console.log("*" * 2);
    a++;
}