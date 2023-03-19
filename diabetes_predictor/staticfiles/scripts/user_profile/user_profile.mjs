import { getCookie } from "../handlers/cookieHandler.mjs";

async function logout()
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

    let confirmation = confirm("Tem a certeza?")
    console.log(confirmation);
    if (confirmation)
    {
        await fetch('http://127.0.0.1:8000/userprofile', requestOptions)
        window.location.href = "http://127.0.0.1:8000/"
    }
}

function goToLoginPage() { window.location.href = 'http://127.0.0.1:8000/login' }

//Add event listener if element is rendered
if (document.getElementById('userLogoutButton') != null)
    document.getElementById('userLogoutButton').addEventListener('click', logout)

//Add event listener if element is rendered
if (document.getElementById('userLoginBtn') != null)
    document.getElementById('userLoginBtn').addEventListener('click', goToLoginPage)
