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


    let response = await fetch('http://127.0.0.1:8080/projectsupport', requestOptions)
    let data = await response.json()
    if (data.isAuthroized == 1){
         window.location.href = "http://127.0.0.1:8080/projectsupport/contribute"}
    else if (data.isAuthroized == -1)
    {

        let confirmation = confirm("È necessario inciar uma sessão para fazer a contribuição, pretende prosseguir?")

        if (confirmation)
            window.location.href = "http://127.0.0.1:8080/login"
    }

}
