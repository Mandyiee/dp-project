
let mainBox = document.querySelector('.viewed__dp')
let showBox = document.querySelector('.button__create')
let backDrop = document.querySelector('.backdrop')
let displayUls = document.querySelectorAll('.displayUL')
let mainAsides = document.querySelectorAll('.mainaside')
let chevys = document.querySelectorAll('.chevy')

showBox.addEventListener('click',()=>{
    mainBox.classList.add('mainbox')
    backDrop.classList.add('backdropFilter')
    
})
backDrop.addEventListener('click',()=>{
    mainBox.classList.remove('mainbox')
    backDrop.classList.remove('backdropFilter')
    
})

displayUls.forEach(displayUl=>{
    displayUl.addEventListener('click',()=>{
       mainAsides.forEach(mainAside =>{
        mainAside.classList.toggle('aside1')
        chevys.forEach(chevy =>{
            chevy.classList.toggle('chevy1')
        })
       })
    })
})


// show userinformation
const loggedIn = document.querySelector('.logged__in')
let logged = document.querySelector('.logged__out')
console.log(logged)
console.log(loggedIn)

loggedIn.addEventListener('mouseover',()=>{
    logged.classList.add('no_display')
})
loggedIn.addEventListener('mouseout',()=>{
    logged.classList.remove('no_display')
})

// progressbar
let uplaod = document.getElementById('uploaded')
let progess = document.getElementById('progress')
let load = 0;
let process = '';

uplaod.oninput = ({target})=>{
    // let filename =uplaod.files[0].name;
    // let extension = filename.split('.').pop();
    // let filesize = uplaod.files[0].size
    let file = target.files[0]
    if(file){
        let filename = file.name
        uploadFile(filename)
    }
}
function uploadFile(name){
    let xhr = newX
}