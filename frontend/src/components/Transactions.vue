<template>
  <div>
    <h1>Transactions</h1>
    <form @submit.prevent="addTransaction">
      <input v-model="newTransaction.name" placeholder="Name" required />
      <input
        v-model.number="newTransaction.amount"
        placeholder="Amount"
        required
      />
      <input
        v-model="newTransaction.category"
        placeholder="Category"
        required
      />
      <input v-model="newTransaction.date" type="date" required />
      <button type="submit">Add Transaction</button>
    </form>
    <ul>
      <li v-for="transaction in transactions" :key="transaction.id">
        {{ transaction.name }}: {{ transaction.amount }} -
        {{ transaction.category }} ({{ transaction.date }})
      </li>
    </ul>

    <TransactionsChart :transactions="transactions" />
  </div>
</template>

<script>
import api from "../services/api";
import TransactionsChart from "./TransactionsChart.vue";

export default {
  name: "UserTransactions",
  components: {
    TransactionsChart,
  },
  data() {
    return {
      transactions: [],
      newTransaction: {
        name: "",
        amount: 0,
        category: "",
        date: "",
      },
    };
  },
  mounted() {
    this.fetchTransactions();
  },
  methods: {
    async fetchTransactions() {
      try {
        const response = await api.getTransactions();
        this.transactions = response.data;
        console.log("Fetched Transactions:", this.transactions); // 추가
      } catch (error) {
        console.error("Error fetching transactions:", error);
      }
    },
    async addTransaction() {
      try {
        await api.createTransaction(this.newTransaction);
        this.fetchTransactions(); // 새로고침하여 추가된 데이터를 반영
        this.newTransaction = { name: "", amount: 0, category: "", date: "" }; // 입력 필드 초기화
      } catch (error) {
        console.error("Error adding transaction:", error);
      }
    },
  },
};
</script>
