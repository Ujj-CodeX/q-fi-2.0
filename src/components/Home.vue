<template>
  
  

    <div class="heading" style="margin-left: 200px; margin-top:110px; color: black;">
      <div style="display: flex; align-items: flex-start; gap: 20px; margin-top: 0px;">
      <img :src="require('@/assets/90.png')" alt="Logo" width="40" height="40"  class="d-inline-block align-text-top" style="margin-left: 0px;">
      <h1 style="font-weight: bold;">Q-Fi</h1>
    </div>
      <h5 style="font-weight: bold;">Challenge yourself and ace your grade</h5>
    </div>

    <div style="display: flex; align-items: flex-start; gap: 120px; margin-top: 0px;">
      <div class="card" style="height: 350px; width: 330px; margin-left: 200px; margin-top: 50px; border-radius: 10px;">
        <form @submit.prevent="handleLogin">
          <div class="mb-3" style="width: 290px; margin-left: 20px; margin-top: 20px;">
            <label for="username" class="form-label" style="color: black; font-weight: bold;">Username</label>
            <input  type="text" class="form-control" id="username" v-model="username" placeholder="Username">

            <label for="password" class="form-label" style="color: black; font-weight: bold; margin-top: 10px;">Password</label>
            <input  type="password" class="form-control" id="password" v-model="password" placeholder="Password">

            <button type="submit" class="btn btn-primary" style="margin-top: 20px; width: 290px; background-color: rgb(3, 3, 137); color: white;">Sign In</button>
            <a @click.prevent="forget"
   style="cursor: pointer; font-weight: bold; display: block; text-decoration: underline; color: black; margin-top: 15px;">
   Forgot Password?
</a>
            <div v-if="errorMessage" class="alert alert-danger mt-3">
              {{ errorMessage }}
            </div>
          </div>
        </form>
      </div>

      <div class="illustrative">
        <img :src="require('@/assets/1.png')" style="height: 400px;  margin-left: 200px;">
      </div>
    
</div>
    <div class="heading" style="margin-left: 200px; margin-top:100px; color: black; " >
      <h5 style="font-weight: bold;">Choose your subject & courses</h5>
      <div class="mb-3 d-flex">
        <select class="form-select" style="width: 250px; height: 30px; border-radius: 8px;">
          <option disabled selected>Select Courses</option>

          <option>BS</option>
          <option>BCA</option>
          <option>BA</option>
          <option>BTech</option>
          <option>BBA</option>
         
        </select>

        <select class="form-select" style="margin-left: 20px; height: 30px; border-radius: 8px;" >
          <option disabled selected>Select Courses</option>

          <option>Python</option>
          <option>Machine Learning</option>
          <option>Operating System</option>
          <option>Business Management</option>
          <option>System Automation</option>
          <option>Ancient History</option>

        </select>

        <button type="button" class="btn btn-primary" style="margin-left: 20px; border-radius: 8px; width: 100px; background-color: rgb(3, 3, 137); color: white;" @click="handleBookNow">Start Quiz</button>
      </div>
    </div>

    <div>
      <h3 style="color:black; margin-top: 100px; margin-left: 200px; font-weight: bold;"> Key Features</h3>

    <div class="minicards" style="display: flex; align-items: flex-start; gap: 10px; margin-left: 100px; ">

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/2.jpg')" class="card-img service-img" style="cursor: pointer;width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 90px; font-weight: bold; font-size: larger; margin-top: 50px;" >Track your Progress</h7>
            </div>

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/3.jpg')" class="card-img service-img" style="cursor: pointer;width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 70px; margin-top: 50px; font-weight: bold; font-size: larger;" >Syllabus based Quizes</h7>
                
            </div>

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/4.png')" class="card-img service-img" style=" cursor: pointer;width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 100px; margin-top: 50px; font-weight: bold; font-size: larger;" >Multiple Courses</h7>
            </div>
        </div>
  </div>


  <div v-if="showforgetcard" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 500px; height: 600px;margin-left: 100px;  border-radius: 10px;">
    <div >
  <h2 class="card-heading">Change Password</h2>
  
        <form @submit.prevent="handleChangePassword">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input v-model="username" type="text" class="form-control" id="username" required>
          </div>
  
          <div class="mb-3">
            <label for="new_password" class="form-label">New Password</label>
            <input v-model="new_password" type="password" class="form-control" id="new_password" required>
          </div>
  
          <div class="mb-3">
            <label for="confirm_password" class="form-label">Confirm New Password</label>
            <input v-model="confirm_password" type="password" class="form-control" id="confirm_password" required>
          </div>
  
          <button type="submit" class="btn btn" style="background-color: rgb(3, 3, 137); color: white;">Change Password</button>
          
        </form></div>
        <button class="btn btn-danger mb-3" @click="showforgetcard = false" style="width: 100px; margin-left:180px; margin-top: 20px;">Cancel</button>
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
      loading: false,
      showforgetcard:false,
      new_password: '',
      confirm_password: ''
    };
  },
  methods: {
    async handleLogin() {
      this.loading = true;
      this.errorMessage = '';

      try {
        const response = await axios.post(
          'https://q-fi.onrender.com/login', 
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
          localStorage.setItem('token', response.data.access_token); 
          auth.isLoggedIn = true;
          this.$router.push('/User');  
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
  
  handleBookNow() {
  alert(`Thannks for your Interest Login with your Student ID to start acing your Grades.`)
}
,
async handleChangePassword() {
        if (this.new_password !== this.confirm_password) {
          alert('Passwords do not match!');
          return;
        }
  
        try {
          const payload = {
            username: this.username,
            new_password: this.new_password
          };
  
          const response = await axios.post('https://q-fi.onrender.com/change-password', payload);
  
          if (response.data.success) {
            alert('Password changed successfully!');
            this.showforgetcard=false;
          } else {
            alert(response.data.error || 'Failed to change password.');
          }
        } catch (error) {
          console.error('Change password error:', error);
          alert('Error changing password. Please try again.');
        }
      },
      forget() {
    this.showforgetcard = !this.showforgetcard;
    
  }

},

}




</script>


<style scoped>
.service-img {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-img:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}
</style>
