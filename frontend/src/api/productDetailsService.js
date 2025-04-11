import api from "./axios";

export const productDetailsService = {
	getProduct: (product_id) => api.get(`/product_details/?product_id=${product_id}`),
	fetchProductHistoryChartData: async (product_id, selectedDuration) => {
		try {
			const response = await api.get(`/product/price-history/?product_id=${product_id}&duration=${selectedDuration}`)
			const data = response.data;
			console.log(data.datasets[0]);

			return {
				chart: {
					id: 1,
					header: "Price history",
					type: "line",
					data: {
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

								

								mode: 'nearest',
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
									text: 'Price'
								}
							},
							x: {
								type: 'time',
									
								time: {
									tooltipFormat: 'yyyy-MM-dd',
									unit: 'day',
									displayFormats: {
										day: 'MMM d',
									}
								},
							}
						}
					}
				}
			}
		} catch (error) {
			console.error("Error fetching product chart data:", error);
			return {};
		}
	}

};