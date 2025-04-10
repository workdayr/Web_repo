// productViewChartService.js

const PRODUCT_PRICE_HISTORY_ENDPOINT = "http://127.0.0.1:8000/api/product/price-history/";

export const fetchProductHistoryChartData = async (productId) => {
    try {
        const url = `${PRODUCT_PRICE_HISTORY_ENDPOINT}?product_id=${productId}`;
        const response = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }

        const data = await response.json();

        const formattedLabels = data.labels.map(dateStr => dateStr.split('T')[0]);

        return {
            charts: [
                {
                    id: 1,
                    header: "Item approvals in",
                    type: "line",
                    data: {
                        labels: formattedLabels,
                        datasets: data.datasets
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                usePointStyle: true,
                                pointStyle: 'rect',
                                boxWidth: 12,
                                labels: {
                                    usePointStyle: true,
                                    pointStyle: 'rect',
                                    boxWidth: 12,

                                },
                            },
                            tooltip: {
                                mode: 'index',
                                intersect: false
                            },

                        },
                        interaction: {
                            mode: 'nearest',
                            axis: 'x',
                            intersect: false
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: 'Precio'
                                }
                            },
                            x: {
                                title: {
                                    display: true,
                                    text: 'Fecha'
                                }
                            }
                        }
                    },
                }
            ]
        };
    } catch (error) {
        console.error("Error fetching product chart data:", error);
        return { charts: [] };
    }
};
