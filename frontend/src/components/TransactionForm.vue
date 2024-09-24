<template>
  <div>
    <h2>Add New Transaction</h2>
    <input type="date" v-model="newTransaction.date" placeholder="Date" />
    <input type="number" v-model="newTransaction.amount" placeholder="Amount" />
    <button @click="addTransaction">Add Transaction</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTransaction: {
        date: "",
        amount: 0,
      },
    };
  },
  methods: {
    addTransaction() {
      if (this.newTransaction.date && this.newTransaction.amount > 0) {
        this.$emit("transaction-added", { ...this.newTransaction });
        this.newTransaction.date = "";
        this.newTransaction.amount = 0;
      }
    },
  },
};
</script>
