
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

/* Make it redirect somehow */