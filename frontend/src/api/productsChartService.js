
const USER_ENDPOINT = "http://127.0.0.1:8000/api/user_analytics/";

export const fetchProductsChartData = async () => {
    try {
        const response = await fetch(USER_ENDPOINT, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }

        const data = await response.json();
        const totalSignupsCount = data.newUsers.reduce((acc, val) => acc + val, 0);


        return {
            charts: [
                {
                    id: 1,
                    type: "doughnut",
                    data: {
                        labels: [
                            'Amazon',
                            'Aliexpress',
                            'Mercado Libre'
                        ],
                        datasets: [
                            {
                                label: "Registered users",
                                data: data.registeredUsers,
                                borderColor: "#FFF",
                                backgroundColor: ['#CB3CFF',
                                    '#0038FF',
                                    '#00C2FF'],
                                circumference: 180,
                                rotation: -90,
                            },
                        ],
                    },
                    options: {
                        responsive: true, maintainAspectRatio: false,
                        cutout: "89%",
                        plugins: {
                            legend: {
                                display: true,
                                position: "bottom",
                                align:'start',
                                labels:{
                                    usePointStyle: true,
                                    pointStyle: "circle",
                                },
                            },
                           
                        },
                    },
                },
                {
                    id: 2,
                    header: "Top stores discounts",
                    subtitle: `$ ${totalSignupsCount.toLocaleString()} K`,
                    type: "bar",
                    data: {
                        labels: data.months,
                        datasets: [
                            {
                                label: "Amazon",
                                data: data.totalViews,
                                backgroundColor: "#CB3CFF",
                                barThickness: 6
                            },
                            {
                                label: "Mercado Libre",
                                data: data.totalViews,
                                backgroundColor: "#ffc107",
                                barThickness: 6
                            },
                            {
                                label: "Apple Store",
                                data: data.totalViews,
                                backgroundColor: "#007bff",
                                barThickness: 6
                            },
                        ],
                    },
                    options: { responsive: true, maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: true,
                                position: "top",
                                align:'center',
                                labels:{
                                    usePointStyle: true,
                                    pointStyle: "circle",
                                    

                                },
                            },
                           
                        },
                     },
                },
                {
                    id: 3,
                    header: "New Signups",
                    type: "bar",
                    data: {
                        labels: data.months,
                        datasets: [
                            {
                                label: "Signups",
                                data: data.newUsers,
                                backgroundColor: "#ffc107",
                            },
                        ],
                    },
                    options: { responsive: true, maintainAspectRatio: false },
                },
                {
                    id: 4,
                    header: "Average time of sesions",
                    type: "line",
                    data: {
                        labels: data.months,
                        datasets: [
                            {
                                label: "Signups",
                                data: data.newUsers,
                                backgroundColor: "#ffc107",
                            },
                        ],
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        width: 100,
                        height: 50,
                    },
                },
            ],
            stats: {
                totalNewSignups: totalSignupsCount,
              },
        };
    } catch (error) {
        console.error("Error fetching chart data:", error);
        return { charts: [] };
    }
};
