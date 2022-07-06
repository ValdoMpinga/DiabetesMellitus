//Handles form premature submit
function handlePrematureSubmit(progress)
{
    if (progress != 100)
        alert('O formulário deve ser completamente preenchido antes de submetido, se por acaso chegou no final, por favor volte atrás e veja o que esta em falta.')
}

export { handlePrematureSubmit }

