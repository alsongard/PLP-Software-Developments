//object are key : value pairs which are used to hold data about an item
let myBook = {
    title:"Nathanshallah",
    author:"Jordan Steven",
    price:3000
}

//accessing values either using dot notation or brackets
console.log(myBook.title);
console.log(myBook["author"]);

//to add a new property to an object
myBook.publisher = "CodeWithGard";
myBook.year = 2024;

console.log(myBook);

//modify properties of an object use either dot or bracket notation
myBook.year = 2010;
myBook["title"] = "JavaScript Programming";
console.log(myBook);

//deleting properties of an object, use the delete keyword followed by the property
delete myBook["price"];
console.log(myBook);

//check property in object exist use in keyword
console.log("title" in myBook);//returns true
console.log("price" in myBook);//prints false

//function can also be included in an object
let person = {
    firstName:"Tonal",
    secondName: "Alson",
    age:234,
    school:"Zetech Uni",
    describe:function (){
        console.log(`${this.firstName} studies in ${this.school}`);
    }
}
person.describe()
