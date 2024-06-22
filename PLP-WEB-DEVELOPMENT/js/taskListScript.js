//IIFE (immediately invoked function expression)
( ()=>{
    console.log("Hello Mr. World");
    //array list
    let taskListArray = [];
    //get HTML elements
    const form = document.getElementById("form");
    const ul  = document.getElementById("tasklist");
    const textData = document.getElementById("task-item");

    function addItemToDOM(itemId, task){//add item to document object model (html doc)
        const li = document.createElement("li");
        li.setAttribute("data-id", itemId)
        li.textContent = task;
        ul.appendChild(li);
    }

    function addItemToArray(itemId,task){
        taskListArray.push({itemId, task});
        console.log(taskListArray);
    }
    function removeItemFromDOM(id){
        var li = document.querySelector('[data-id="' + id + '"]');
        //remove list item
        ul.removeChild(li);
    }
    function remvoeItemFromArray(id){
        taskListArray = taskListArray.filter( (item) => item.itemId !== id);
        console.log(taskListArray);
    }
    //first event listener form
    //addEventListener("listen2event", functionNameRefrenceOnly)
    form.addEventListener("submit", (event) => {
        console.log("Submit button Clicked!");
        let time = event.timeStamp;
        event.preventDefault();
        console.log(time);
        let itemId =  String(Date.now());
        console.log(itemId);
        let task = textData.value;
        console.log(task);
        textData.value = "";//reset the input field
        addItemToDOM(itemId, task);
        addItemToArray(itemId, task);
    });
    //second event Listener ul(tasklist)
    ul.addEventListener("click", (event) =>{
        let id = event.target.getAttribute("data-id");
        if (!id){
            return null;
        }
        removeItemFromDOM(id);
        remvoeItemFromArray(id);
    } )


})();
