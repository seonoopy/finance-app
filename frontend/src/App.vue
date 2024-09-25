<template>
  <div>
    <TransactionForm @transaction-added="handleTransactionAdded" />
    <TransactionChart :transactions="transactions" />
    <Login />
  </div>
</template>

<script>
import TransactionForm from "./components/TransactionForm.vue";
import TransactionChart from "./components/TransactionsChart.vue";
import Login from "./services/Login.vue";

export default {
  components: {
    TransactionForm,
    TransactionChart,
    Login,
  },
  data() {
    return {
      transactions: [],
    };
  },
  methods: {
    handleTransactionAdded(newTransaction) {
      this.transactions = [...this.transactions, newTransaction];
    },
  },
};
</script>
