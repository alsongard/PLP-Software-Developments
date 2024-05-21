//for(condition){statements}
//print values from 0 to 10
//for loops are used when you know the number of times to perform a repitive tasks.
for (let i = 0; i <= 10; i++){
    console.log(`Value is ${i}`);//return 0 to 9 when i < 9 but 0 to 10 i <= 9
}
//in the above we used postfix meaning that i is still the same value and increases after
my_num = 1
console.log(`Using postfix ${my_num++}`);
console.log(my_num);

//reverse order
console.log("Display 1 to 10 in descending order");
for (let x = 10; x >= 1; x--){
    console.log(`Value is ${x}`);
}

console.log("values starting from 0 and incrementing by 3")
for (let x = 0; x <= 20; x+=3){//x = x + 3
    console.log(`Value is ${x}`);
}
//coins deal
let heads = 0;
let tails = 0;
for (x = 1; x <= 10; x++){
    if (Math.random() < 0.5){
        tails++;
    }
    else{
        heads++;
    }
}
console.log(`Number of heads is ${heads}`);
console.log(`Number of tails is ${tails}`);
