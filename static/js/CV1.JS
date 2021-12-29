function validityCheck(){
    let isBirthDateValid= document.getElementById(birthday).checkValidation() 
    let Bdate = " "
    if(isBirthDateValid){
        Bdate= "Yay,valid date!"
    }
    else{
        Bdate="Not valid, please try again"
    }
}

function greet (name){
console.log("Hello" + name + ":)");


}