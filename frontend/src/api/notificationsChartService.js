const NOTIFICATION_ENDPOINT = "http://127.0.0.1:8000/api/notification_analytics/";

export const fetchNotiChartData = async () => {
    try {
        const response = await fetch(NOTIFICATION_ENDPOINT, {
            method: "GET",
            headers: {

                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }

        const data = await response.json();

        console.log("Fetched Data:", data);
        return {
            charts: [
                {
                    id: 1,
                    header: "Effective Alert Timing",
                    type: "bar",
                    data: {
                        labels: data.days,
                        datasets: [
                            {
                                label: "On Time",
                                data: data.onTimeAlerts,
                                backgroundColor: "#9B55E5",
                                barThickness: 10
                            },
                        ],
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                    },
                },
                {
                    id: 2,
                    header: "Redictered users",
                    subtitle: `${data.totalRedirects.toLocaleString()} K`,
                    type: "doughnut",
                    data: {
                        labels: data.platforms,
                        datasets: [
                            {
                                label: "Registered users",
                                data: data.redirectCounts,
                                borderColor: "#FFF",
                                backgroundColor: ["#CB3CFF", "#0038FF", "#00C2FF"],
                                weight: 2,
                                circumference: 300,
                                rotation: -90
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
                                labels: {
                                    usePointStyle: true,
                                    pointStyle: "circle",
                                    padding: 15,
                                },
                            },
                        },
                    },
                },
            ],
            stats: {
                totalOnTime: data.totalOnTime,
                totalRedirects: data.totalRedirects,
            },
        };
    } catch (error) {
        console.error("Error fetching chart data:", error);
        return { charts: [], stats: {} };
    }
};