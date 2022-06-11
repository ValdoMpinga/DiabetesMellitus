
const progress = document.getElementById("progress");
let ageVerifier = 0
let waistVerifier= 0
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
    pillsVerifier=1
  }
}

function fruitsProgress()
{
  if (fruitsVerifier == 0)
  {
    progress.value += 6
    fruitsVerifier=1
  }
}

function diabeticFamilyProgress()
{
  if (diabeticFamilyVerifier == 0)
  {
    progress.value += 6
    diabeticFamilyVerifier=1
  }
}

function smokeProgress()
{
  if (smokeVerifier == 0)
  {
    progress.value += 6
    smokeVerifier=1
  }
}

function sugarProgress()
{
  if (sugarVerifier == 0)
  {
    progress.value += 6
    sugarVerifier=1
  }
}

function glicemyLevelProgress()
{
  if (glicemyLevelVerifier == 0)
  {
    progress.value += 6
    glicemyLevelVerifier=1
  }
}

function isGirlProgress()
{
  if (isGirlVerifier == 0)
  {
    progress.value += 6
    isGirlVerifier=1
  }
}

function diabetesProgress()
{
  if (diabetesVerifier == 0)
  {


    progress.value += 6
    diabetesVerifier=1
  }
}

function weightProgress()
{
  if (weightVerifier == 0)
  {
    progress.value += 6
    weightVerifier=1
  }
}

function heightProgress()
{
  if (heightVerifier == 0)
  {
    progress.value += 6
    heightVerifier=1
  }
}

function glicemyValueSelectProgress()
{
  if (glicemyValueVerifier == 0)
  {
    progress.value += 6
    glicemyValueVerifier =1
  }
}

function glicemyValueFieldProgress()
{
  if (glicemyValueVerifier == 0)
  {
    progress.value += 6
    glicemyValueVerifier =1
  }
}

function physicalExerciseProgress()
{
  if (physicalExerciseVerifier == 0)
  {
    progress.value += 6
    physicalExerciseVerifier=1
  }
}

function fatProgress()
{
  if (fatVerifier == 0)
  {
    progress.value += 6
    fatVerifier=1
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

document.querySelectorAll("input[name='glic']").forEach((input) =>
{
  input.addEventListener('change', glicemyValueSelectProgress);
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


//   for (let i = 0, len = comp.length; i < len; i=1)
//   {
//     comp[i].value = null;

//   }
// }
// componentes()

// function resetMyForm()
// {
//   let formulario = document.getElementById('idForm');
//   formulario.reset();
// }

// resetMyForm()

// function increaseValue()
// {

//   const button = document.getElementById('btnNext');

//   let elementClicked = true;

//   button.addEventListener('click', function handleClick()
//   {
//     let progress = document.getElementById('progress');
//     let value = progress.value;
//     let maximumProgress = 100;

//     if (value < maximumProgress)
//     {
//       value = value + 12.5;

//       progress.value = value;
//     } else
//     {
//       console.log("chegou no limite");
//     }


//   });
// }

//increaseValue()


let divAtual = 1;

// function call()
// {
//   console.log("hello");
// }

function nextDiv()
{
  disableAllDivs();
  console.log(divAtual);
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
