
// accesing div here
let div = document.getElementById("num");

// variable holding id of the 2 buttons
let add = document.getElementById("hindustan");
let sub = document.getElementById("afganistan");


// variable number 0
let number = 0;


// adding action to the buttons
add.addEventListener("click", () => {
    ++number;
    div.innerHTML = number;
})

sub.addEventListener("click", () => {
    if (number > 0){
        --number;
        div.innerHTML = number;
    }
    else {
        div.innerHTML = 0;
    }
})