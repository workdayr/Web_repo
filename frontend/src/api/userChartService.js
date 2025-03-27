
const USER_ENDPOINT = "http://127.0.0.1:8000/api/user_analytics/";

export const fetchChartData = async () => {
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

    // Calcular total de usuarios registrados y no registrados
    const totalUsers =
      data.registeredUsers.reduce((acc, val) => acc + val, 0) +
      data.unregisteredUsers.reduce((acc, val) => acc + val, 0);

    // Calcular subtítulos para las gráficas
    const totalViewsCount = data.totalViews.reduce((acc, val) => acc + val, 0);
    const totalSignupsCount = data.newUsers.reduce((acc, val) => acc + val, 0);

    return {
      charts: [
        {
          id: 1,
          header: "Total Users",
          subtitle: `${totalUsers.toLocaleString()} users`,
          type: "line",
          data: {
            labels: data.months,
            datasets: [
              {
                label: "Registered users",
                data: data.registeredUsers,
                borderColor: "#321647",
                backgroundColor: "rgba(0, 123, 255, 0.2)",
              },
              {
                label: "Unregistered users",
                data: data.unregisteredUsers,
                borderColor: "#00C2FF",
                backgroundColor: "rgba(0, 123, 255, 0.2)",
              },
            ],
          },
          options: { responsive: true, maintainAspectRatio: false
           },
        },
        {
          id: 2,
          header: "Total Views",
          subtitle: `${totalViewsCount.toLocaleString()} views`,
          type: "bar",
          data: {
            labels: data.months,
            datasets: [
              {
                label: "Views",
                data: data.totalViews,
                backgroundColor: "#28a745",
              },
            ],
          },
          options: { responsive: true, maintainAspectRatio: false },
        },
        {
          id: 3,
          header: "New Signups",
          subtitle: `${totalSignupsCount.toLocaleString()} signups`,
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
          subtitle: `${totalSignupsCount.toLocaleString()} minutes`,
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
          },
        },
      ],
      // Valores para StatsCard.vue
      stats: {
        totalRegisteredUsers: data.registeredUsers.reduce((acc, val) => acc + val, 0),
        totalUnregisteredUsers: data.unregisteredUsers.reduce((acc, val) => acc + val, 0),
        totalNewSignups: totalSignupsCount,
      },
    };
  } catch (error) {
    console.error("Error fetching chart data:", error);
    return { charts: [], stats: {} };
  }
};
