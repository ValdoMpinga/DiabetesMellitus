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
        await fetch('/userprofile', requestOptions)
        window.location.href = "/"
    }
}

function goToLoginPage(){  window.location.href = '/login' }

//Add event listener if element is rendered
if (document.getElementById('userLogoutButton') != null)
document.getElementById('userLogoutButton').addEventListener('click', logout)

//Add event listener if element is rendered
if (document.getElementById('userLoginBtn') != null)
    document.getElementById('userLoginBtn').addEventListener('click', goToLoginPage)
