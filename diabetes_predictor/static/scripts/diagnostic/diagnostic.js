let actualDiv = 1;
function nextDiv()
{
  disableAllDivs();
  switch (actualDiv)
  {
    case 1:
      actualDiv++;
      document.getElementById("btnPrev").classList.remove("disableDiv");
      document.getElementById("div2").classList.remove("disableDiv");
      break;
    case 2:
      actualDiv++;
      document.getElementById("div3").classList.remove("disableDiv");
      break;
    case 3:
      actualDiv++;
      document.getElementById("div4").classList.remove("disableDiv");
      break;
    case 4:
      actualDiv++;
      document.getElementById("btnNext").classList.add("disableDiv");
      document.getElementById("div5").classList.remove("disableDiv");
      break;
    case 5:
      document.getElementById("div5").classList.remove("disableDiv");
      break;
  }
}

function previousDiv()
{
  disableAllDivs();

  switch (actualDiv)
  {
    case 1:
      document.getElementById("div1").classList.remove("disableDiv");
      break;
    case 2:
      actualDiv--;
      document.getElementById("btnPrev").classList.add("disableDiv");
      document.getElementById("div1").classList.remove("disableDiv");
      break;
    case 3:
      actualDiv--;
      document.getElementById("div2").classList.remove("disableDiv");
      break;
    case 4:
      actualDiv--;
      document.getElementById("div3").classList.remove("disableDiv");
      break;
    case 5:
      actualDiv--;
      document.getElementById("btnNext").classList.remove("disableDiv");
      document.getElementById("div4").classList.remove("disableDiv");
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
}

function ageChange()
{
  document.querySelector('.idade').forEa
}

let ageSelection = 0

function myfunction(event)
{
  console.log("bbbbbbbbbb");
  if( ageSelection == 0)
    {

    var progress = document.getElementById("progress");
    progress.value += 25
    ageSelection++
  }
}
document.querySelectorAll("input[name='idade']").forEach((input) =>
{
  console.log("zzz");

  input.addEventListener('change', myfunction);
});
