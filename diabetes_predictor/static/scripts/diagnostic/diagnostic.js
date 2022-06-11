
let ageSelection = 0
let check = 0
let checkWaist = 0
let checkMeds = 0
let checkFruit = 0
let checkFam = 0
let checkSmoke = 0
let checkSugar = 0
let checkLevelGlic = 0
let checkIfGirl = 0
let checkDiabetes = 0
let checkWeight = 0
let checkHeight = 0
let checkActivity = 0
let checkFat = 0


function myfunction(event)
{
  console.log("bbbbbbbbbb");
  if (ageSelection == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    ageSelection++
  }
}

function check2(event)
{
  if (check == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    check++
  }
}

function check3(event)
{
  if (checkMeds == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkMeds++
  }
}

function check4(event)
{
  if (checkFruit == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkFruit++
  }
}

function check5(event)
{
  if (checkFam == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkFam++
  }
}
function check6(event)
{
  if (checkSmoke == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkSmoke++
  }
}

function check7(event)
{
  if (checkSugar == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkSugar++
  }
}


function check8(event)
{
  if (checkLevelGlic == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkLevelGlic++
  }
}

function check9(event)
{
  if (checkIfGirl == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkIfGirl++
  }
}

function check10(event)
{
  if (checkDiabetes == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkDiabetes++
  }
}

function check11(event)
{
  if (checkWeight == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkWeight++
  }
}


function check12(event)
{
  if (checkHeight == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkHeight++
  }
}

function check13(event)
{
  if (checkActivity == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkActivity++
  }
}

function check14(event)
{
  if (checkFat == 0)
  {

    var progress = document.getElementById("progress");
    progress.value += 6
    checkFat++
  }
}

document.querySelectorAll("input[name='idade']").forEach((input) =>
{
  console.log("zzz");

  input.addEventListener('change', myfunction);
});

document.querySelectorAll("input[name='cintura']").forEach((input) =>
{
  input.addEventListener('change', check2);
});

document.querySelectorAll("input[name='medicamento']").forEach((input) =>
{
  input.addEventListener('change', check3);
});

document.querySelectorAll("input[name='fruta']").forEach((input) =>
{
  input.addEventListener('change', check4);
});

document.querySelectorAll("input[name='familia']").forEach((input) =>
{
  input.addEventListener('change', check5);
});

document.querySelectorAll("input[name='fumar']").forEach((input) =>
{
  input.addEventListener('change', check6);
});

document.querySelectorAll("input[name='acucar']").forEach((input) =>
{
  input.addEventListener('change', check7);
});

document.querySelectorAll("input[name='levelglic']").forEach((input) =>
{
  input.addEventListener('change', check8);
});

document.querySelectorAll("input[name='ifgirl']").forEach((input) =>
{
  input.addEventListener('change', check9);
});

document.querySelectorAll("input[name='diabetes']").forEach((input) =>
{
  input.addEventListener('change', check10);
});

document.querySelectorAll("input[name='peso']").forEach((input) =>
{
  input.addEventListener('change', check11);
});

document.querySelectorAll("input[name='altura']").forEach((input) =>
{
  input.addEventListener('change', check12);
});

document.querySelectorAll("input[name='atividade']").forEach((input) =>
{
  input.addEventListener('change', check13);
});

document.querySelectorAll("input[name='gordura']").forEach((input) =>
{
  input.addEventListener('change', check14);
});






function ifChecked()
{
  // if (document.orderform.elements[].checked == true){
  //     console.log("Oieee");
  // }                                                                                                  
}
ifChecked()

function componentes()
{
  let comp = document.getElementsByClassName('my-component');
  console.warn(comp);

  for (let i = 0, len = comp.length; i < len; i++)
  {
    comp[i].value = null;

  }
}
componentes()

function resetMyForm()
{
  let formulario = document.getElementById('idForm');
  formulario.reset();
}

resetMyForm()

function increaseValue()
{

  const button = document.getElementById('btnNext');

  let elementClicked = true;

  button.addEventListener('click', function handleClick()
  {
    let progress = document.getElementById('progress');
    let value = progress.value;
    let maximumProgress = 100;

    if (value < maximumProgress)
    {
      value = value + 12.5;

      progress.value = value;
    } else
    {
      console.log("chegou no limite");
    }


  });
}

//increaseValue()



let divAtual = 1;

function call()
{
  console.log("hello");
}

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


function validate()
{
  if (document.getElementById('progress').checked)
  {
    alert("checked");
  } else
  {
    alert("You didn't check it! Let me check it for you.");
  }
}
