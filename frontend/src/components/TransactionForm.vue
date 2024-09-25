<template>
  <div>
    <h2>Add New Transaction</h2>
    <input
      type="text"
      v-model="newTransaction.name"
      placeholder="Name"
      required
    />
    <input type="number" v-model="newTransaction.amount" placeholder="Amount" />
    <input
      type="text"
      v-model="newTransaction.category"
      placeholder="Category"
      require
    />
    <input type="date" v-model="newTransaction.date" placeholder="Date" />
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
