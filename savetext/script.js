
function slideanimation() {
    document.getElementById("body_id").className = "slide";
}

function changepagedelay() {
    setTimeout(changepage, 1000);
}

function changepage() {
    window.location.href = "library";
}

var varbutton = document.getElementById("buttonid");
varbutton.addEventListener("click", slideanimation);
varbutton.addEventListener("click", changepagedelay);

var el = document.getElementById("containerid2");
el.addEventListener("click", containeranimation2);

function containeranimation2() {
    document.getElementById("containerid2").classList.add("x");
    document.getElementById("flipperid2").classList.add("x");
}