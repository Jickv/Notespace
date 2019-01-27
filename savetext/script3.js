function changepage() {
    window.location.replace("/library/");
}

var bbutton = document.getElementById("backbutton");
bbutton.addEventListener("click", changepage);

var container1 = document.getElementById("containerid");
container1.addEventListener("click", containeranimation);

function containeranimation() {
    document.getElementById("containerid").classList.add("x");
    document.getElementById("flipperid").classList.add("x");
}
/* when container is clicked, turn on x for flipper and container */