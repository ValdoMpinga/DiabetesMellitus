function handlePrematureSubmit(progress)
{
  if (progress != 100)
    alert('O formulário deve ser completamente preenchido antes de submetido')
}


function outputDiv()
{
  document.querySelector(".outputTextSection").style.display = "none";
  document.querySelector(".outputReplayButton").style.display = "none";
}


function nextDiv(divAtual)
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
  return divAtual;
}

function previousDiv(divAtual)
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
  return divAtual;
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

export { handlePrematureSubmit, nextDiv, previousDiv, outputDiv }
