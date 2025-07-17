<template>
  
  

    <div class="heading" style="margin-left: 200px; margin-top:110px; color: black;">
      <h1 style="font-weight: bold;">Q-Fi</h1>
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
            <a href="/forgot_user" style=" font-weight: bold; display: block; text-decoration: underline; color:black; margin-top: 15px;">Forgot Password?</a>

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
                <img :src="require('@/assets/2.jpg')" class="card-img service-img" style="width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 90px; font-weight: bold; font-size: larger; margin-top: 50px;" >Track your Progress</h7>
            </div>

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/3.jpg')" class="card-img service-img" style="width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 70px; margin-top: 50px; font-weight: bold; font-size: larger;" >Syllabus based Quizes</h7>
                
            </div>

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/4.png')" class="card-img service-img" style="width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 100px; margin-top: 50px; font-weight: bold; font-size: larger;" >Multiple Courses</h7>
            </div>
        </div>
  </div>
</template>

<script>
import axios from 'axios';

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
          'http://localhost:5000/login', 
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
    }
  },
  handleBookNow() {
  alert(`Thannks for your Interest Login with your Student ID to start acing your Grades.`)
}


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
