
const progress = document.getElementById("progress");
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


function outputDiv()
{
    document.querySelector(".outputTextSection").style.display = "none";
    document.querySelector(".outputReplayButton").style.display = "none";
}

outputDiv()

function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie !== '')
    {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++)
        {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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

function glicemyValueSelectProgress()
{
    if (glicemyValueVerifier == 0)
    {
        progress.value += 6
        glicemyValueVerifier = 1
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


function handlePrematureSubmit()
{
    if (progress.value != 100)
        alert('O formulário deve ser completamente preenchido antes de submetido')
}

const form = document.querySelector('form')

form.onsubmit = async (e) =>
{
    e.preventDefault()
    const formData = new FormData(e.target);
    let csrftoken = getCookie('csrftoken');

    formObj = {};

    for (const [fieldName] of formData)
    {
        const fieldValue = formData.getAll(fieldName);
        formObj[fieldName] = fieldValue.length == 1 ? fieldValue.toString() : fieldValue
    }

    const requestOptions =
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            "sex": formObj.sexo,
            "age": formObj.idade,
            "waist": formObj.cintura,
            "weight": formObj.peso,
            "height": formObj.altura,
            "exercise": formObj.atividade,
            "pills": formObj.medicamento,
            "fruits": formObj.fruta,
            "diabeticFamily": formObj.familia,
            "fats": formObj.gordura,
            "smoke": formObj.fumar,
            "highBloodGlucose": formObj.acucar,
            "glucoseAnalysis": formObj.glicemia,
            "glucoseLevelChange": formObj.levelglic,
            "womanGlucose": formObj.ifgirl,
            "areYouDiabetic": formObj.diabetes
        })
    }

    let response = await fetch('http://127.0.0.1:8080/projectsupport/contribute', requestOptions)

    console.log("!H");
    document.querySelector(".outputTextSection").style.display = "block";
    document.querySelector(".outputReplayButton").style.display = "block";

}

function handleReplayButton()
{
    document.querySelector('form').reset()
    progress.value = 12.5
    ageVerifier = 0
    waistVerifier = 0
    pillsVerifier = 0
    fruitsVerifier = 0
    diabeticFamilyVerifier = 0
    smokeVerifier = 0
    sugarVerifier = 0
    glicemyLevelVerifier = 0
    glicemyValueVerifier = 0
    isGirlVerifier = 0
    diabetesVerifier = 0
    weightVerifier = 0
    heightVerifier = 0
    physicalExerciseVerifier = 0
    fatVerifier = 0
    for (let i = 7; i > 0; i--)
    {

        document.querySelector('#btnPrev').click()
    }

    outputDiv()
}

function JsonOrganizer(formData)
{
    formObj = {};

    for (const [fieldName] of formData)
    {
        const fieldValue = formData.getAll(fieldName);
        formObj[fieldName] = fieldValue.length == 1 ? fieldValue.toString() : fieldValue
    }

    let sample = {
        "sex": formObj.sexo,
        "age": formObj.idade,
        "waist": formObj.cintura,
        "weight": formObj.peso,
        "height": formObj.altura,
        "exercise": formObj.atividade,
        "pills": formObj.medicamento,
        "fruits": formObj.fruta,
        "diabeticFamily": formObj.familia,
        "fats": formObj.gordura,
        "smoke": formObj.fumar,
        "highBloodGlucose": formObj.acucar,
        "glucoseAnalysis": formObj.glicemia,
        "glucoseLevelChange": formObj.levelglic,
        "womanGlucose": formObj.ifgirl,
        "areYouDiabetic": formObj.diabetes
    }

    return sample
}



let divAtual = 1;

function nextDiv()
{
    disableAllDivs();
    switch (divAtual)
    {
        case 1:
            divAtual++
            document.getElementById("btnPrev").classList.remove("disableDiv");
            document.getElementById("div2").classList.remove("disableDiv");
            break;
        case 2:
            divAtual++
            document.getElementById("div3").classList.remove("disableDiv");
            break;
        case 3:
            divAtual++
            document.getElementById("div4").classList.remove("disableDiv");
            break;
        case 4:
            divAtual++
            document.getElementById("div5").classList.remove("disableDiv");
            break;
        case 5:
            divAtual++
            document.getElementById("div6").classList.remove("disableDiv");
            break;
        case 6:
            divAtual++
            document.getElementById("div7").classList.remove("disableDiv");
            break;
        case 7:
            divAtual++
            document.getElementById("btnNext").classList.add("disableDiv");
            document.getElementById("div8").classList.remove("disableDiv");
            break;
        case 8:
            document.getElementById("div8").classList.remove("disableDiv");
            break;
    }
}

function previousDiv()
{
    disableAllDivs();

    switch (divAtual)
    {
        case 1:
            document.getElementById("div1").classList.remove("disableDiv");
            break;
        case 2:
            divAtual--
            document.getElementById("btnPrev").classList.add("disableDiv");
            document.getElementById("div1").classList.remove("disableDiv");
            break;
        case 3:
            divAtual--
            document.getElementById("div2").classList.remove("disableDiv");
            break;
        case 4:
            divAtual--
            document.getElementById("div3").classList.remove("disableDiv");
            break;
        case 5:
            divAtual--
            document.getElementById("div4").classList.remove("disableDiv");
            break;
        case 6:
            divAtual--
            document.getElementById("div5").classList.remove("disableDiv");
            break;
        case 7:
            divAtual--
            document.getElementById("div6").classList.remove("disableDiv");
            break;
        case 8:
            divAtual--
            document.getElementById("btnNext").classList.remove("disableDiv");
            document.getElementById("div7").classList.remove("disableDiv");
            break;
    }
}

function disableAllDivs()
{
    document.getElementById("div1").classList.add("disableDiv");
    document.getElementById("div2").classList.add("disableDiv");
    document.getElementById("div3").classList.add("disableDiv");
    document.getElementById("div4").classList.add("disableDiv");
    document.getElementById("div5").classList.add("disableDiv");
    document.getElementById("div6").classList.add("disableDiv");
    document.getElementById("div7").classList.add("disableDiv");
    document.getElementById("div8").classList.add("disableDiv");

}


