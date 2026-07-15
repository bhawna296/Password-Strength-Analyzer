const password=document.querySelector("input");
const strengthBar=document.getElementById("strength-bar");
const strengthText=document.getElementById("strength-text");

password.addEventListener("input",()=>{

    let score=0;

    if(password.value.length>=8)
        score+=20;
    if(/[a-z]/.test(password.value))
        score+=20;
    if(/[A-Z]/.test(password.value))
        score+=20;
    if(/[0-9]/.test(password.value))
        score+=20;
    if(/[!@#$%^&*]/.test(password.value))
        score+=20;

    strengthBar.value=score;
    strengthText.innerHTML="Strength : " + getStrengthText(score) + " (" + score + "/100)";
});

function getStrengthText(score) {
    if(score<40)
        return "Weak";
    else if(score<60)
        return "Medium";
    else if(score<80)
        return "Strong";
    else
        return "Very Strong";
}