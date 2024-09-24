<template>
  <div>
    <h2>Transactions Overview</h2>
    <div v-if="chartData && chartData.labels.length > 0">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div v-else>
      <p>No transactions data available.</p>
    </div>
  </div>
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "TransactionsChart",
  components: { Bar },
  props: {
    transactions: {
      type: Array,
      required: true,
      default: () => [],
    },
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Transaction Amounts",
            backgroundColor: "#42A5F5",
            data: [],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        plugins: {
          legend: { display: true },
        },
      },
    };
  },
  watch: {
    transactions: {
      immediate: true,
      handler(newTransactions) {
        this.updateChartData(newTransactions);
      },
    },
  },
  mounted() {
    this.updateChartData(this.transactions);
  },
  methods: {
    updateChartData(transactions) {
      if (Array.isArray(transactions) && transactions.length > 0) {
        const dates = transactions.map((t) => t.date);
        const amounts = transactions.map((t) => t.amount);

        // 새로운 배열로 할당
        this.chartData.labels = [...dates];
        this.chartData.datasets[0].data = [...amounts];
      } else {
        // 데이터가 없는 경우
        this.chartData.labels = [];
        this.chartData.datasets[0].data = [];
      }
    },
  },
};
</script>

<style scoped>
h2 {
  margin-bottom: 16px;
}
</style>
