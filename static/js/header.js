const barBtn = document.querySelector(".bar-btn");
//console.log(barBtn)
//Listen to click event
barBtn.addEventListener("click",function(e){
	//target the nav-menu
 const navMenu = document.querySelector(".nav-menu");

 const openMenu = document.querySelector(".open");

 navMenu.classList.add("open");
 e.target.classList.add("close");
 e.target.innerHTML = "&#10006";

 //close the nav-menu
 if(openMenu){
 navMenu.classList.remove("open");
 e.target.innerHTML = "&#9776";
 e.target.classList.remove("close");
 }

})