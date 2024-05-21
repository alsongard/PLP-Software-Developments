/*
add items to shopping cart
calculate totol price
calculat discounts


item for sale:
phone = 300
smart Tv = 220
Gaming console = 150

10% discount total price > 400
shopping cart = empty
addItem() name of item as parameter
    when called it checkes if an item exist in the system
    if not displays message we do not sell item else we sell item
calculateTotalPrice()
    iterates through the whole shopping cart and adds price of items
pay() method:
    payment amout as a parameter
    takes the total amount of items from calculateTotalPrice() method.
    price > 400 10%  discount

    if payment is >= totalPrice (no discount or with discount), 
        display message thanking the customer
    less payment:
        display message indicating payment is less
*/
shoppingList = {
    phone:300,
    smartTv:220,
    gaming_console:150
}
priceOfItems = [];
shoppingCart = [];
function addItem(...args){
    for (let i = 0; i < arguments.length; i++){
        nameItem = args[i];
        if (nameItem in shoppingList){
            console.log(`The item  is ${nameItem} is ${shoppingList[nameItem]} dollars`)
            priceOfItems.push(shoppingList[nameItem]);
            shoppingCart.push(nameItem);
        }
        else{
            console.log("We do not sell such an item.");
        }

    }
}
addItem("phone");
console.log(priceOfItems);
console.log(shoppingCart);
function calculateTotalPrice(){
    let totalPrice = 0;
    for(let i = 0; i < priceOfItems.length; i++){
        totalPrice += priceOfItems[i];
    }
    console.log(`The total price is ${totalPrice}`);
    return totalPrice;
}
let totalPrice = calculateTotalPrice();
function pay(payment){
    //check for discount
    if (totalPrice > 400){
        let totalPriceToPay = totalPrice * 0.9;
        console.log(totalPriceToPay);
        if(payment >= totalPriceToPay){
            console.log("Great, thankyou for buying at our shop");
            let balance = payment - totalPrice;
            console.log(`The balance is ${balance}`);
        }
        else{
            console.log("Price of item choosen exceeds the payment given")
        }
    }
    else{
        if(payment >= totalPrice){
            console.log("Great, thankyou for buying at our shop");
            let balance = payment - totalPrice;
            console.log(`The balance is ${balance}`);
        }
        else{
            console.log("Price of item choosen exceeds the payment given")
        }
    }
}
pay(400);