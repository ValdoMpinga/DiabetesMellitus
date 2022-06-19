function goToLoginPage()
{
    window.location.href = 'http://127.0.0.1:8080/login'
}

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

    confirmation = confirm("Tem a certeza?")

    if (confirmation)
    {
        await fetch('http://127.0.0.1:8080/userprofile', requestOptions)
        window.location.href = "http://127.0.0.1:8080/"
    }
}

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
