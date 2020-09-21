// DOM Elements
const navList = document.getElementsByClassName('nav-list');
const navBtn = document.getElementsByClassName('nav-btn');


// Hide the nav list if scripts are on
navList[0].style.display = 'none';



// Add Even Listener to Nav-Btn that toggles display properties
navBtn[0].addEventListener("click", function () {
    if (navList[0].style.display == 'none') {
        navList[0].style.display = 'block';
    } else {
        navList[0].style.display = 'none';
    }
});





// console.log(navList);