<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
      <input v-model="username" placeholder="Username" required />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        required
      />
      <button type="submit">Login</button>
    </form>
    <div v-if="user">
      <h3>Welcome, {{ user.username }}</h3>
    </div>
  </div>
</template>

<script>
import { login, fetchUser } from "./api";

export default {
  data() {
    return {
      username: "",
      password: "",
      user: null,
      token: "",
    };
  },
  methods: {
    async loginUser() {
      const response = await login(this.username, this.password);
      this.token = response.access_token;
      this.user = await fetchUser(this.token);
    },
  },
};
</script>
