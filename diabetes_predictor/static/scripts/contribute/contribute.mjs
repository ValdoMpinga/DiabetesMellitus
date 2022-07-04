import { nextDiv, previousDiv, outputContributionDiv } from "../handlers/divHandler.mjs";
import { handlePrematureSubmit } from "../handlers/formHandler.mjs";
import { getCookie } from "../handlers/cookieHandler.mjs";
import { JSONParser } from "../handlers/jsonHandler.mjs";

const progress = document.getElementById("progress");// Form completation progress bar

//Variables that validate if a form section as select boxes have been filled to increment progress value on the progress bar
let ageVerifier = 0
let waistVerifier = 0
let pillsVerifier = 0
let fruitsVerifier = 0
let diabeticFamilyVerifier = 0
let smokeVerifier = 0
let sugarVerifier = 0
let glicemyLevelVerifier = 0
let glicemyValueVerifier = 0
let isGirlVerifier = 0
let diabetesVerifier = 0
let weightVerifier = 0
let heightVerifier = 0
let physicalExerciseVerifier = 0
let fatVerifier = 0

//Handles the form final output div
outputContributionDiv()

//All progess functions increment to the total progress when a form element is selected
function ageProgress()
{
    if (ageVerifier == 0)
    {
        progress.value += 6
        ageVerifier = 1
    }
}

function waistProgress()
{
    if (waistVerifier == 0)
    {
        progress.value += 6
        waistVerifier = 1
    }
}

function pillsProgress()
{
    if (pillsVerifier == 0)
    {
        progress.value += 6
        pillsVerifier = 1
    }
}

function fruitsProgress()
{
    if (fruitsVerifier == 0)
    {
        progress.value += 6
        fruitsVerifier = 1
    }
}

function diabeticFamilyProgress()
{
    if (diabeticFamilyVerifier == 0)
    {
        progress.value += 6
        diabeticFamilyVerifier = 1
    }
}

function smokeProgress()
{
    if (smokeVerifier == 0)
    {
        progress.value += 6
        smokeVerifier = 1
    }
}

function sugarProgress()
{
    if (sugarVerifier == 0)
    {
        progress.value += 6
        sugarVerifier = 1
    }
}

function glicemyLevelProgress()
{
    if (glicemyLevelVerifier == 0)
    {
        progress.value += 6
        glicemyLevelVerifier = 1
    }
}

function isGirlProgress()
{
    if (isGirlVerifier == 0)
    {
        progress.value += 6
        isGirlVerifier = 1
    }
}

function diabetesProgress()
{
    if (diabetesVerifier == 0)
    {


        progress.value += 6
        diabetesVerifier = 1
    }
}

function weightProgress()
{
    if (weightVerifier == 0)
    {
        progress.value += 6
        weightVerifier = 1
    }
}

function heightProgress()
{
    if (heightVerifier == 0)
    {
        progress.value += 6
        heightVerifier = 1
    }
}

function glicemyValueFieldProgress()
{
    if (glicemyValueVerifier == 0)
    {
        progress.value += 6
        glicemyValueVerifier = 1
    }
}

function physicalExerciseProgress()
{
    if (physicalExerciseVerifier == 0)
    {
        progress.value += 6
        physicalExerciseVerifier = 1
    }
}

function fatProgress()
{
    if (fatVerifier == 0)
    {
        progress.value += 6
        fatVerifier = 1
    }
}

//Event listeners that listen whenver the form fields are selected or filled
document.querySelectorAll("input[name='idade']").forEach((input) =>
{
    input.addEventListener('change', ageProgress);
});

document.querySelectorAll("input[name='cintura']").forEach((input) =>
{
    input.addEventListener('change', waistProgress);
});

document.querySelectorAll("input[name='medicamento']").forEach((input) =>
{
    input.addEventListener('change', pillsProgress);
});

document.querySelectorAll("input[name='fruta']").forEach((input) =>
{
    input.addEventListener('change', fruitsProgress);
});

document.querySelectorAll("input[name='familia']").forEach((input) =>
{
    input.addEventListener('change', diabeticFamilyProgress);
});

document.querySelectorAll("input[name='fumar']").forEach((input) =>
{
    input.addEventListener('change', smokeProgress);
});

document.querySelectorAll("input[name='acucar']").forEach((input) =>
{
    input.addEventListener('change', sugarProgress);
});

document.querySelectorAll("input[name='levelglic']").forEach((input) =>
{
    input.addEventListener('change', glicemyLevelProgress);
});

document.querySelectorAll("input[name='ifgirl']").forEach((input) =>
{
    input.addEventListener('change', isGirlProgress);
});

document.querySelectorAll("input[name='diabetes']").forEach((input) =>
{
    input.addEventListener('change', diabetesProgress);
});

document.querySelectorAll("input[name='peso']").forEach((input) =>
{
    input.addEventListener('change', weightProgress);
});

document.querySelectorAll("input[name='altura']").forEach((input) =>
{
    input.addEventListener('change', heightProgress);
});

document.querySelectorAll("input[name='glicemia']").forEach((input) =>
{
    input.addEventListener('change', glicemyValueFieldProgress);
});

document.querySelectorAll("input[name='atividade']").forEach((input) =>
{
    input.addEventListener('change', physicalExerciseProgress);
});

document.querySelectorAll("input[name='gordura']").forEach((input) =>
{
    input.addEventListener('change', fatProgress);
});

//event lister that alerts user if he tries to submit uncompleted form
document.getElementById("submitButton").addEventListener("click", (e) =>
{
    if (timeOnThisPage > 0)
    {
        e.stopPropagation();
        handlePrematureSubmit(progress.value)
    } else { timeOnThisPage++ }
})

const form = document.querySelector('form')

//event lister handles form submission
form.onsubmit = async (e) =>
{
    e.preventDefault()
    const formData = new FormData(e.target);
    let csrftoken = getCookie('csrftoken'); //Gets crsf token which is necessary to make post requests to django

    let formObject = JSONParser(formData)

    const requestOptions =
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            "sex": formObject.sexo,
            "age": formObject.idade,
            "waist": formObject.cintura,
            "weight": formObject.peso,
            "height": formObject.altura,
            "exercise": formObject.atividade,
            "pills": formObject.medicamento,
            "fruits": formObject.fruta,
            "diabeticFamily": formObject.familia,
            "fats": formObject.gordura,
            "smoke": formObject.fumar,
            "highBloodGlucose": formObject.acucar,
            "glucoseAnalysis": formObject.glicemia,
            "glucoseLevelChange": formObject.levelglic,
            "womanGlucose": formObject.ifgirl,
            "areYouDiabetic": formObject.diabetes
        })
    }

    let response = await fetch('http://127.0.0.1:8080/projectsupport/contribute', requestOptions)
    let data = await response.json()

    if (data.isAuthroized == 1)//If submmited successfully, it displays the user a message
    {
        document.querySelector(".outputTextSection").style.display = "block";

        setTimeout(() => window.location.href = "http://127.0.0.1:8080/userprofile",4000)
        
        

    } else if (data.isAuthroized == 0)//If submmited unsuccessfully, it displays the user a message
    {
        alert(`Muito obrigado pela intenção, porem esta conta só podera contribuir novamente em ${data.daysLeft} dias!`)
    } else //If user tries to submit form with login
    {
        let confirmation = confirm("È necessario inciar uma sessão para fazer a contribuição, pretende prosseguir?")

        if (confirmation)
            window.location.href = "http://127.0.0.1:8080/login"
    }
}

let divAtual = 1;

//Handles form div next button
document.getElementById("btnNext").addEventListener("click", function (e)
{
    e.stopPropagation();
    divAtual = nextDiv(divAtual);
});
//Handles form div forward button
document.getElementById("btnPrev").addEventListener("click", function (e)
{
    e.stopPropagation();
    divAtual = previousDiv(divAtual);
});
