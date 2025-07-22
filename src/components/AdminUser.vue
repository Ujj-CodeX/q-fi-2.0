<template>
  <div style="display: flex; align-items: flex-start;">
   
    <div class="sidebar-card">
      <h5 style="color: white; margin-left: 20px;">Admin Management</h5>
      <a class="nav-link" style="color:whitesmoke; cursor:pointer; display: block; margin-top:30px;" href="/Admin_Dash">Academics Management</a>
       <a class="nav-link" style="color:whitesmoke;cursor:pointer; display: block; margin-top:30px;" href="/Admin_User">User Management</a>
       <a class="nav-link" style="color:whitesmoke; cursor:pointer;display: block; margin-top:30px;" href="/Admin_Quiz">Quiz Management</a>
       <a class="nav-link" 
   style="color:whitesmoke; display: block; margin-top:30px; cursor:pointer; font-weight: bold;" 
   v-if="auth.isLoggedIn" @click="logout">
   Logout</a>
    </div>

    
    <div style="flex: 1; padding: 20px;">
      <h2 style="font-weight: bold; margin-top: 20px; margin-left: 400px;">User Management and Overview</h2>

     
      <div style="display: flex; gap: 40px; margin-top: 50px;">
        <div class="card inset-card p-4 text-center" style="flex: 2; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quiz Name vs No of User attempts</h6>
<div style="height: 400px;"> 
     <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
        <div v-else>Loading chart...</div>
  </div>
        </div>
        <div class="card inset-card p-4 text-center" style="flex: 1; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quiz Name and No of attempts</h6>
          <table class="table table-bordered">
        <thead style="background-color: rgb(3, 3, 137)">
          <tr style="color: white;">
            <th>Quiz Name</th>
            <th>No. of Attempts</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in quizAttempts" :key="item.subject_name">
            <td>{{ item.subject }}</td>
            <td>{{ item.attempts }}</td>
          </tr>
        </tbody>
      </table>
        </div>
      </div>

      
      <div style="display: flex; gap: 40px; margin-top: 50px;">
        <div class="card inset-card p-4 text-center" style="flex: 1.5; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">User Review and Rating</h6>
          <div style="max-height: 420px; overflow-y: auto;">
    <table class="table table-striped table-hover">
      <thead style="position: sticky; top: 0; background-color:rgb(3, 3, 137) ">
        <tr style="color: white;">
          <th>Username</th>
          <th>Review</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="review in userReviews" :key="review.username + review.review.slice(0,10)">
          <td style="font-weight: bold;">{{ review.username }}</td>
          <td style="text-align: left;">{{ review.review }}</td>
        </tr>
      </tbody>
    </table>
  </div>
        </div>
        <div class="card inset-card p-4 text-center" style="flex: 1; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">User Details</h6>
          <div>

        <div class="input-group">
    <input class="form-control" v-model="userId" placeholder="Enter User_Id for Details" style="border-radius: 10px;">
    <button @click="fetchUserDetails" class="btn btn-primary" style="margin-left: 10px; background-color: rgb(3, 3, 137); border-radius: 8px;">Search</button>
  </div>

        <div v-if="userDetails" class="mt-4 text-start" style="margin-left: 10px; text-align: left;">
  <h6 style="font-weight: bold;">User Information:</h6>
  <p><strong>ID:</strong> {{ userDetails.id }}</p>
  <p><strong>Name:</strong> {{ userDetails.name }}</p>
  <p><strong>Username:</strong> {{ userDetails.username }}</p>
  <p><strong>Email:</strong> {{ userDetails.email }}</p>
  <p><strong>DOB:</strong> {{ userDetails.dob }}</p>
  <p><strong>Gender:</strong> {{ userDetails.gender }}</p>
  <p><strong>Course:</strong> {{ userDetails.course }}</p>
</div>

        </div>
        </div>
      </div>

     
      <div style="display: flex; gap: 40px; margin-top: 50px;">
        <div class="card inset-card p-4 text-center" style="flex: 2; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quizzes vs Ratings</h6>
          <div style="height: 400px; width: 600px; margin-left: auto;">
          <Pie v-if="pieChartData" :data="pieChartData" />
           <div v-else>Loading pie chart...</div>
          </div>
        </div>
        <div class="card inset-card p-4 text-center" style="flex: 1; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quiz Name and No of attempts</h6>
          <table class="table table-bordered">
        <thead style="background-color: rgb(3, 3, 137)">
          <tr style="color: white;">
            <th>Quiz Name</th>
            <th>No. of Attempts</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in quizAttempts" :key="item.subject_name">
            <td>{{ item.subject }}</td>
            <td>{{ item.attempts }}</td>
          </tr>
        </tbody>
      </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartData = ref(null)
const chartOptions = {
  responsive: true,
  plugins: {
    legend: { display: false },
    title: { display: true, text: 'Attempts by Subject' }
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: { stepSize: 1 }
    }
  }
}

const userId = ref('')
const userDetails = ref(null)

const fetchUserDetails = async () => {
  if (!userId.value) return alert('Please enter a user ID')

  try {
    const token = localStorage.getItem('admin_token');
    const response = await axios.get(`http://localhost:5000/api/user/${userId.value}`,{headers: {
        'Authorization': `Bearer ${token}` 
      }})
    userDetails.value = response.data
  } catch (err) {
    console.error(err)
    alert('User not found')
    userDetails.value = null
  }
}


// Store attempts for the table
const quizAttempts = ref([])

onMounted(async () => {
  try {
    const token = localStorage.getItem('admin_token')
    const response = await axios.get('http://localhost:5000/api/quiz-attempts', {
      headers: { Authorization: `Bearer ${token}` }
    })

    // Store in ref for table
    quizAttempts.value = response.data

    const subjects = response.data.map(item => item.subject)
    const attempts = response.data.map(item => item.attempts)

    chartData.value = {
      labels: subjects,
      datasets: [{
        label: 'Attempts',
        backgroundColor: '#42A5F5',
        data: attempts
      }]
    }
  } catch (error) {
    console.error('Error loading chart data:', error)
  }
})

import { Pie } from 'vue-chartjs'
import { ArcElement } from 'chart.js'

ChartJS.register(ArcElement)  // Register Pie support

const pieChartData = ref(null)

const loadPieChartData = async () => {
  try {
    const token = localStorage.getItem('admin_token');
    const response = await axios.get('http://localhost:5000/api/quiz-average-ratings',{
      headers: { Authorization: `Bearer ${token}` }
    })
    const data = response.data

    const quizNames = data.map(item => item.quiz_name)
    const avgRatings = data.map(item => item.average_rating)

    pieChartData.value = {
      labels: quizNames,
      datasets: [
        {
          label: 'Average Rating',
          data: avgRatings,
          backgroundColor: [
            '#FF6384', '#36A2EB', '#FFCE56', '#9CCC65', '#FF7043',
            '#AB47BC', '#26C6DA', '#FFA726', '#66BB6A', '#EF5350'
          ]
        }
      ]
    }
  } catch (error) {
    console.error('Error loading pie chart data:', error)
  }
}

onMounted(() => {
  loadPieChartData()
})

const userReviews = ref([])

const loadUserReviews = async () => {
  try {
    const token = localStorage.getItem('admin_token');
    const response = await axios.get('http://localhost:5000/api/user-reviews',{
      headers: { Authorization: `Bearer ${token}` }
    })
    userReviews.value = response.data
  } catch (error) {
    console.error('Error fetching user reviews:', error)
  }
}

onMounted(() => {
  loadUserReviews()
})
const auth = reactive({
  isLoggedIn: true
})

const router = useRouter()

function logout() {
  localStorage.removeItem('admin_token')
  auth.isLoggedIn = false
  router.push('/admin')
}
</script>


<style scoped>
  canvas {
  background-color: white;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
.sidebar-card {
  width: 250px;
  border-radius: 15px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  background-color: rgb(3, 3, 137);
  padding: 15px;
  top: 20px;
  position: sticky;
  height: 85vh;
  overflow-y: auto;
}
</style>
