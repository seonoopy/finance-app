<template>
    <div>
      <h2>Transactions Overview</h2>
      <div v-if="chartData && chartData.labels.length > 0">
        <BarChart :chartData="chartData" />
      </div>
      <div v-else>
        <p>No transactions data available.</p>
      </div>
    </div>
</template>
  
<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
  
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);
  
export default {
components: {
    BarChart: Bar
},
data() {
    return {
        chartData: {
            labels: [],  // 날짜를 레이블로 사용
            datasets: [
                {
                    label: 'Amount',
                    backgroundColor: '#f87979',
                    data: []  // 금액 데이터를 여기에 삽입
                }
            ]
        }
    };
    },
    props: {
        transactions: {
            type: Array,
            required: true,
            default: () => []  // 기본값으로 빈 배열을 설정
        }
    },
    watch: {
        transactions: {
            immediate: true,
            handler(newTransactions) {
                this.updateChartData(newTransactions);
            }
        }
    },
    methods: {
        updateChartData(transactions) {
        if (transactions.length > 0) {
            const dates = transactions.map(t => t.date);
            const amounts = transactions.map(t => t.amount);
            
            this.chartData.labels = dates;
            this.chartData.datasets[0].data = amounts;
        } else {
            // 데이터가 없을 경우 기본값으로 초기화
            this.chartData.labels = [];
            this.chartData.datasets[0].data = [];
        }
        }
    }
}
</script>
  