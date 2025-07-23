<template>
    <div class="container my-5">
    
    <div class="card inset-card p-4 text-center mx-auto my-card" style="max-height: 100%; width: 100%; border-radius: 25px; background-color:white; overflow: auto;">
            
        
            <div style="display: flex; align-items: flex-start;  gap: 100px;" >
          <img :src="require('@/assets/16.png')" style="height: 350px; width: 350px;  margin-left: 50px;  margin-top:100px;"  >
            
        <div style="width: 1px; height: 400px; background-color: #ccc; margin-top: 100px;"></div>
            <div class="mb-3" style="width: 300px; margin-left: 50px; margin-top: 150px;">




              
                <form @submit.prevent="handleLogin" >


                
                    
                    
                <h4 style="color: black;  ">Admin Login</h4>
                <br>
                
                
                <input type="username" class="form-control" id="username" v-model="username" placeholder="Username" name="username" style="font-weight: bold;"><br>
                
                
               
                <input type="password" class="form-control" id="Password" v-model="password" placeholder="Password" name="password" style="font-weight: bold;"><br>
                <button 
  :disabled="loading" 
  type="submit" 
  class="btn btn-primary"
  style="margin-top: 10px; width: 100px; border-radius: 15px; background-color: rgb(3, 3, 137); color: white;"
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