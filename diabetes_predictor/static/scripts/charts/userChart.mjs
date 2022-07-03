var ctx = document.getElementById("userChart").getContext("2d");
let filteredMonths = []

monthsHandler()


var myChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: filteredMonths,
        datasets: [
            {
                data: userMounthAmount,
                label: "Usuários registados",
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    "rgba(255, 159, 64, 0.2)",
                ],
                borderColor: [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    "rgba(255, 159, 64, 1)",
                ],
                borderWidth: 1,
            },
        ],
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
        skipNull: true,
        plugins: {
            title: {
                display: true,
                text: 'Registo dos usuários ao longo dos meses',
                color: '#323643',
                font: {
                    size: 16
                }
            }
        }

    },
});


function monthsHandler()
{
    userMounthAmount = userMounthAmount.replace("[", "");
    userMounthAmount = userMounthAmount.replace("]", "");
    userMounthAmount = userMounthAmount.split(",");

    months = months.replace('[', '');
    months = months.replace(']', '');
    months = months.split(",");

    months.forEach(element =>
    {
        filteredMonths.push(element.replace(/[^a-z0-9]/gi, ''))
    });
}
