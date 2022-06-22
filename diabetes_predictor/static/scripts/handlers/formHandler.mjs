//Handles form premature submit
function handlePrematureSubmit(progress)
{
    if (progress != 100)
        alert('O formulário deve ser completamente preenchido antes de submetido')
}

export { handlePrematureSubmit }
