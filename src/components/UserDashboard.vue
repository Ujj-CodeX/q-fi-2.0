<template>

    <div class="heading" style="margin-left: 200px; margin-top:100px; color: black; ">
      <div style="display: flex; align-items: flex-start; gap: 20px; margin-top: 0px;">
      <img :src="require('@/assets/90.png')" alt="Logo" width="40" height="40"  class="d-inline-block align-text-top" style="margin-left: 0px;">
        <h1 style="font-weight: bold;">Q-Fi</h1></div>
      <h5 style="font-weight: bold;">Looking for something specific ?</h5>
    

     
</div>
    <div style="display: flex; align-items: flex-start; gap: 30px; margin-top: 0px; margin-left: 10px">

    <div style="display: flex; flex-direction: column; align-items: center; gap: 10px; margin-top: 0px; margin-left: 100px">
            <div  style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/10.png')" @click="openLeaderboard"  class="card-img service-img" style="cursor: pointer; width: 100px; height: 100px; margin-top: 10px; margin-left: 20px; border-radius: 8px;">
                <h7 style="margin-left: 20px; font-weight: bold; font-size: medium; margin-top: 20px;" >Leaderboard</h7>
            </div>

            <div  style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/6.png')" @click="downloadReport()" class="card-img service-img" style="cursor: pointer;width: 100px; height: 100px; margin-top: 10px; margin-left: 20px; border-radius: 8px; ">
                <h7 style="margin-left: 5px; margin-top: 20px; font-weight: bold; font-size: medium;" >Download Report</h7>
                
            </div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 10px; margin-top: 0px; ">
        

            <div style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/7.jpg')" @click="toggleScoreCard" class="card-img service-img" style="cursor: pointer;width: 100px; height: 100px; margin-top: 10px; margin-left: 20px; border-radius: 8px; ">
                <h7 style="margin-left: 10px; font-weight: bold; font-size: medium; margin-top: 20px;" >Score Overtime</h7>
            </div>

            <div style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/9.png')" @click="openattemptcard" class="card-img service-img" style="cursor: pointer;width: 100px; height: 100px; margin-top: 10px; margin-left: 20px;  border-radius: 8px;">
                <h7 style="margin-left: 20px; margin-top: 20px; font-weight: bold; font-size: medium;" >Past attempts</h7>
                
            </div>


            
        </div>

        <div class="illustrative">
        <img :src="require('@/assets/5.jpg')" style="height: 500px;  margin-left: 200px;">
      </div>

    </div>

  <h2 style="margin-left: 220px; font-weight: bold; margin-top: 50px;"> Start your Quiz Now</h2>  

<div style="display: flex; align-items: flex-start; gap: 50px; margin-top: 20px; margin-left: 10px">
<div class="sidebar-card">
  <h5 style="color: white;"> Choose Subjects</h5>
  <hr>
  <div 
    v-for="(subject, key) in subjects" 
    :key="key" 
    class="subject-item" 
    @click="fetchChapters(subject.subject_id)">
    <span>{{ subject.name }}</span>
    <span>&gt;</span>
  </div>
</div>


<div class="quiz-container">
  <h5 style="color: black; font-weight: bold;">Available Quiz (Choose any)</h5>
  <hr>
  <div v-for="(chapter, index) in chapters"
       :key="index"
       class="quiz-item"
       @click="openQuizCard(chapter.name)">>
      
    <span>{{ chapter.name }}</span>
  </div>
</div>
</div>
    

<div v-if="showcard" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 1200px; height: 600px;margin-left: 100px;  border-radius: 10px;">
 <h2 style="font-weight: bold; color:rgb(3, 3, 137) ; margin-top: 50px;">Good Start Buddy</h2>
 <h6 style="font-weight: bold;  margin-top: 10px;">Just one step - Please Choose your Preferences</h6>
 <h2 style="font-weight: bold; color:black ; margin-top: 10px;">Quiz Name: {{ name }}</h2>

        <div style="display: flex; align-items: center; justify-content: center; gap: 40px; margin-top: 20px;">
  <div class="form-group mb-3">
          
          <select v-model.number="quizSettings.duration" class="form-control" style="border-radius: 10px; background-color: rgb(3, 3, 137); color: white;">
  <option disabled value="">Select Duration</option>
  <option :value="1">1 Minutes</option>
  <option :value="5">5 Minutes</option>
  <option :value="10">10 Minutes</option>
  <option :value="15">15 Minutes</option>
</select>
        </div>

        
        <div class="form-group mb-3">
          
          <select id="questions" class="form-control" v-model="quizSettings.questions" style="border-radius: 10px; background-color: rgb(3, 3, 137); color: white;">
            <option disabled value=""> Select Number of Questions </option>
            <option>5</option>
            <option>10</option>
            <option>15</option>
          </select>
        </div>
</div>


        <div class="start-quiz-btn">
            <button class="btn btn-success" @click="startQuiz">Start Quiz</button>
        </div>

        

      <img :src="require('@/assets/85.jpg')" style="height: 200px; width: 250px; margin-left: 450px; ">  




  </div>
  </div>
  
<div v-if="showleaderboard" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 1200px; height: 600px;margin-left: 100px;  border-radius: 10px;">

<h3 class="text-center mb-4">🏆 Quiz Leaderboard</h3>
<button class="btn btn-danger mb-3" @click="showleaderboard = false" style="width: 200px; margin-left:500px;">Close</button>

      
      <div class="alert alert-info text-center mb-4" v-if="loggedInUser">
  <span v-if="userRank">
    You are currently ranked <strong>#{{ userRank }}</strong> - <strong>{{ loggedInUser }}</strong>
  </span>
  <span v-else>
    You haven’t attempted this quiz yet.
  </span>
</div>

      
      <div style="max-height: 400px; overflow-y: auto;">
        <table class="table table-hover table-bordered text-center">
          <thead class="table-dark sticky-top">
            <tr>
              <th>Rank</th>
              <th>Username</th>
              
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(user, index) in leaderboard"
              :key="user.username"
              :class="{ 'table-primary': user.username === loggedInUser }"
            >
              <td>#{{ index + 1 }}</td>
              <td>{{ user.username }}</td>
              
            </tr>
          </tbody>
        </table>
        </div>


</div>
</div>


<div v-if="showScoreCard" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 1200px; height: 600px;margin-left: 100px;  border-radius: 10px;">

<h3 style="text-align: center;">Score Over Time</h3>
<div style="max-height: 400px; overflow-y: auto; margin-top: 20px;">
    <table class="table table-bordered table-striped text-center">
      <thead class="table-dark sticky-top">
        <tr>
          <th>Quiz Name</th>
          <th>Score</th>
          <th>Submitted On</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in scoreHistory" :key="row.timestamp">
          <td>{{ row.quiz_name }}</td>
          <td>{{ row.score }}</td>
          <td>{{ row.timestamp }}</td>
        </tr>
      </tbody>
    </table></div>
    <button @click="toggleScoreCard" class="btn btn-danger" style="width: 200px; margin-left:500px;">Close</button>


</div>
</div>

<div v-if="showpast" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 1200px; height: 600px;margin-left: 100px;  border-radius: 10px;">
<h5 class="mb-3">📚 Past Quiz Attempts</h5>
    <button class="btn btn-danger mb-3" @click="showpast = false" style="width: 200px; margin-left:500px;">Close</button>

    <div style="max-height: 400px; overflow-y: auto;">
      <table class="table table-bordered table-striped text-center">
        <thead class="table-dark sticky-top">
          <tr>
            <th>#</th>
            <th>Quiz Name</th>
            <th>Submitted On</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(attempt, index) in pastAttempts" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ attempt.quiz_name }}</td>
            <td>{{ attempt.submission_time }}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
  </div>



   <div style="display: flex; gap: 200px; margin-top: 100px;">
    <img :src="require('@/assets/87.png')" style="height: 300px; width: 400px; margin-top: 100px; margin-left: 300px;" />

    <div class="card" style="height: 380px; width: 500px; border-radius: 15px; background-color: white; margin-top: 50px;">
      <div class="mb-3" style="width: 250px; margin-left: 25px; margin-top: 20px;">
        <h5 style="color: black; margin-left: 10px;">Write a Customer Review</h5>
      </div>

      <div class="d-flex" style="margin-top: 40px; width: 500px;">
        <textarea
          v-model="review"
          class="form-control mr-2"
          style="margin-left: 50px; height: 200px; width: 300px;"
          placeholder="Write your review here"
        ></textarea>
        <button
          class="btn btn-outline-light"
          @click="submitReview"
          style="width: 100px; color: white; background-color: rgb(3, 3, 137);"
        >
          Submit
        </button>
      </div>

      <p v-if="message" :style="{ color: messageColor, marginLeft: '50px', marginTop: '20px' }">
        {{ message }}
      </p>
    </div>
  </div>

  



       


</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      review: '',
      message: '',
      messageColor: 'green',
      subjects: [],   
      chapters: [],   
      selectedSubjectId: null,
      showcard:false,
      showleaderboard:false, 
      selectedChapterName: '',
            quizSettings: {
                duration: "",
                questions: "",
                quizName:""
            },
      leaderboard: [],
      loggedInUser: null,
      userRank: null,
     selectedQuiz: null,
     showScoreCard: false,
    scoreHistory: [],
    showpast: false,
    pastAttempts: [],
    
 
    };
  },

  
  mounted() {
    this.fetchSubjects();
    console.log('JWT Token:', localStorage.getItem('token'));

  },
  methods: {
    async fetchSubjects() {
  try {
    const token = localStorage.getItem('token');  

    const response = await axios.get('https://q-fi.onrender.com/subjects1', {
      headers: {
        'Authorization': `Bearer ${token}` 
      }
    });

    this.subjects = response.data;
  } catch (error) {
    console.error('Error fetching subjects:', error);
  }
},
async fetchChapters(subjectId) {
    this.selectedSubjectId = subjectId;
    const token = localStorage.getItem('token');

    
    if (!token) {
        alert('Session expired or not logged in. Redirecting to login page...');
        this.$router.push('/');
        return;
    }

    try {
        const response = await axios.get(`https://q-fi.onrender.com/chapters1/${subjectId}`, {
            headers: { Authorization: `Bearer ${token}` }
        });

        
        if (!response.data || response.data.length === 0) {
            alert('No chapters available for the selected subject.');
            this.chapters = [];
            return;
        }

        this.chapters = response.data;
    } catch (error) {
        
        if (error.response) {
            if (error.response.status === 401) {
                alert('Unauthorized access. Please log in again.');
                this.$router.push('/');
            } else if (error.response.status === 404) {
                alert('No chapters found for the selected subject.');
                this.chapters = [];
            } else {
                alert(`Error: ${error.response.status} - ${error.response.data.message || 'Unknown error occurred'}`);
            }
        } else if (error.request) {
            alert('Server is not responding. Please try again later.');
        } else {
            console.error('Error fetching chapters:', error);
            alert('An unexpected error occurred. Please try again.');
        }
    }
},openQuizCard(chapterName) {
  this.name = chapterName;
  this.showcard = true;
  this.quizSettings.quizName = chapterName;

},
setOption(type, value) {
            this.quizSettings[type] = value;
        },

startQuiz() {
  const { quizName, duration, questions } = this.quizSettings;

  if (!quizName || !duration || !questions) {
    alert("Please fill all fields before starting quiz.");
    return;
  }

  
  this.$router.push({
    path: "/Test",
    query: {
      quizName: quizName,
      duration: duration,
      questions: questions
    }
  });
},
async fetchLeaderboard() {
    try {
      const token = localStorage.getItem("token");
      const response = await axios.get(`https://q-fi.onrender.com/leaderboard`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      this.leaderboard = response.data.leaderboard;
      this.userRank = response.data.userRank;
      this.loggedInUser = response.data.currentUser;

    } catch (error) {
      console.error("Error fetching leaderboard:", error);
    }
  }
,

  getUserRank(username) {
    const entry = this.leaderboard.findIndex(user => user.username === username);
    return entry !== -1 ? entry + 1 : 'N/A';
  },

  openLeaderboard() {
    
    this.showleaderboard = true;
    this.fetchLeaderboard();
  },

  toggleScoreCard() {
    this.showScoreCard = !this.showScoreCard;
    if (this.showScoreCard) {
      this.fetchScoreHistory();
    }
  },
  async fetchScoreHistory() {
    try {
      const response = await fetch("https://q-fi.onrender.com/score-history", {
        headers: {
          "Authorization": `Bearer ${localStorage.getItem("token")}`
        }
      });

      if (response.ok) {
        this.scoreHistory = await response.json();
      } else {
        console.error("Failed to fetch score history");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  },
openattemptcard() {
  this.showpast = true;
  this.fetchPastAttempts(); // Trigger data fetch when opening
},

async fetchPastAttempts() {
  try {
    const response = await axios.get('https://q-fi.onrender.com/past_attempts', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    this.pastAttempts = response.data.attempts;
  } catch (error) {
    console.error("Error fetching past attempts:", error);
    alert("Unable to load past attempts. Please try again.");
  }
},
downloadReport() {
  fetch('https://q-fi.onrender.com/download-report', {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    }
  })
  .then(response => {
    if (!response.ok) throw new Error('Failed to download');
    return response.blob();
  })
  .then(blob => {
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;

    
    link.setAttribute('download', ''); 
    link.setAttribute('target', '_blank');

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    window.URL.revokeObjectURL(url); // Free up memory
  })
  .catch(err => console.error('❌ Error downloading report:', err));
},
async submitReview(e) {

      e.preventDefault()

      const token = localStorage.getItem('token')
      const payload = JSON.parse(atob(token.split('.')[1]))
      const username = payload.sub.split(':')[0] 

      if (!this.review) {
        this.message = 'Please write a review before submitting.';
        this.messageColor = 'red';
        return;
      }

      try {
        const response = await axios.post('https://q-fi.onrender.com/submit_review', {
          username: username || 'Anonymous', 
          review: this.review
        });

        if (response.data.success) {
          this.message = 'Review submitted successfully!';
          this.messageColor = 'green';
          this.review = '';
        } else {
          this.message = response.data.error || 'Something went wrong.';
          this.messageColor = 'red';
        }
      } catch (error) {
        this.message = 'Failed to submit review. Server error.';
        this.messageColor = 'red';
      }
    },
    


  


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


.sidebar-card {
  width: 250px;
  border-radius: 15px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  background-color:rgb(3, 3, 137);
  padding: 15px;
  margin-left: 200px;
  top: 80px;
  left: 20px;
  height: 80vh;
  overflow-y: auto;
  margin-top: 50px;
}

.subject-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s;
  color: white;
}

.subject-item:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.quiz-container {
  
  padding: 20px;
  margin-top: 50px;
}

.quiz-item {
  background: #f8f9fa;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: background 0.3s;
}

.quiz-item:hover {
  background: #e0e0e0;
}
</style>