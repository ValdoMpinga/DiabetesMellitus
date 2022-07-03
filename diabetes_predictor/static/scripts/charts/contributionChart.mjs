const diagnosticData = {
    labels: ["Diabeticos", "Não Diabeticos",],
    datasets: [
        {
            label: "Diagnosticos feitos pelos usuarios",
            data: [diabetics, non_diabetics],
            backgroundColor: [
                "#323643",
                "#93DEFF",
            ],
            hoverOffset: 4,
        },
    ],
};


const contributionConfig = {
    type: "doughnut",
    data: diagnosticData,
    options:
    {
        plugins: {
            title: {
                display: true,
                text: 'Quantidade de diabéticos VS não diabéticos nas contribuições',
                font: {
                    size: 16,
                },
            }
            
        }
    },
};

const contributionChart = new Chart(
    document.getElementById("contributionChart"),
    contributionConfig);

