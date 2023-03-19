const diagnosticData = {
    labels: ["Diabeticos", "Não Diabeticos",],
    datasets: [
        {
            label: "Diagnosticos feitos pelos usuarios",
            data: [diabetic_predicted, non_diabetic_predicted],
            backgroundColor: [
                "rgb(54, 162, 235)",
                "rgb(255, 205, 86)",
            ],
            hoverOffset: 4,
        },
    ],
};


const diagnosticConfig = {
    type: "doughnut",
    data: diagnosticData,
    options:
    {
        plugins: {
            title: {
                display: true,
                text: 'Diagnosticos feito pelos usuários',
                font: {
                    size: 16
                }
            }
        }
    },
};

const diagnosticChart = new Chart(
    document.getElementById("diagnosticChart"),
    diagnosticConfig);

