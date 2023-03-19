import { getCookie } from "../handlers/cookieHandler.mjs";

document.querySelector('#contributeButton').addEventListener('click', contribute)

async function contribute()
{
    let csrftoken = getCookie('csrftoken');

    const requestOptions =
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: {}
    }


    let response = await fetch('http://0.0.0.0:8000/projectsupport', requestOptions)
    let data = await response.json()

    if (data.isAuthroized == 1)//Takes user to contribute page
    {
        window.location.href = "http://0.0.0.0:8000/projectsupport/contribute"
    }
    else if (data.isAuthroized == -1)//Warns user about he must login to contribute
    {

        let confirmation = confirm("È necessario inciar uma sessão para fazer a contribuição, pretende prosseguir?")

        if (confirmation)
            window.location.href = "http://0.0.0.0:8000/login"
    } else if (data.isAuthroized == 0)//Warns the user about the remaining time until he can contribute again
    {
        alert(`Muito obrigado pela intenção, porem esta conta só podera contribuir novamente em ${data.daysLeft} dias!`)
    }

}
