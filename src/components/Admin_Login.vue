<template>
  <div class="container my-5">
    <div
      class="card inset-card p-4 text-center mx-auto my-card"
      style="max-height: 100%; width: 100%; border-radius: 25px; background-color:white; overflow: auto;"
    >
      <div class="row justify-content-center align-items-center">
        <!-- Image Section -->
        <div class="col-lg-5 col-md-6 col-sm-12 text-center mb-4 mb-lg-0">
          <img
            :src="require('@/assets/16.png')"
            class="img-fluid"
            style="max-height: 350px; margin-top: 100px;"
            alt="Admin"
          />
        </div>

        <!-- Divider (visible only on large screens) -->
        <div class="d-none d-lg-block col-lg-1">
          <div style="width: 1px; height: 300px; background-color: #ccc;"></div>
        </div>

        <!-- Login Form -->
        <div class="col-lg-5 col-md-6 col-sm-12">
          <form @submit.prevent="handleLogin" class="text-start px-3 px-md-0">
            <h4 class="text-center text-dark mb-4">Admin Login</h4>

            <input
              type="text"
              class="form-control mb-3"
              v-model="username"
              placeholder="Username"
              name="username"
              style="font-weight: bold;"
            />

            <input
              type="password"
              class="form-control mb-3"
              v-model="password"
              placeholder="Password"
              name="password"
              style="font-weight: bold;"
            />

            <button
              :disabled="loading"
              type="submit"
              class="btn btn-primary w-100"
              style="border-radius: 15px; background-color: rgb(3, 3, 137);"
            >
              {{ loading ? 'Logging in...' : 'Log IN' }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { auth } from '../store';
export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
      loading: false
    };
  },
  methods: {
    async handleLogin() {
      this.loading = true;
      this.errorMessage = '';

      try {
        const response = await axios.post(
          'https://q-fi.onrender.com/Admin_login', 
          {
            username: this.username,
            password: this.password
          }, 
          {
            headers: {
              'Content-Type': 'application/json'
            }
          }
        );

         if (response.status === 200 && response.data.access_token) {
          localStorage.setItem('admin_token', response.data.access_token); 
          auth.isLoggedIn = true;
          this.$router.push('/Admin_dash');
        } else {
          this.errorMessage = 'Unexpected response from the server.';
        }
      } catch (error) {
        if (error.response) {
          this.errorMessage = error.response.data.error || 'Invalid credentials.';
        } else if (error.request) {
          this.errorMessage = 'No response from server. Please check your connection.';
        } else {
          this.errorMessage = 'Error occurred during request.';
        }
      } finally {
        this.loading = false;
      }
    },
  
  
},

}
</script>
<style>
.my-card {
  height: 600px; /* default for desktop */
}

@media (max-width: 768px) {
  .my-card {
    height: auto; /* on mobile screens */
  }
}
</style>