<template>
  <div>
    <TransactionForm @transaction-added="handleTransactionAdded" />
    <TransactionChart :transactions="transactions" />
  </div>
</template>

<script>
import TransactionForm from "./components/TransactionForm.vue";
import TransactionChart from "./components/TransactionsChart.vue";

export default {
  components: {
    TransactionForm,
    TransactionChart,
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
