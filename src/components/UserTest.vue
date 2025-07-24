<template>

    <div style="display: flex; align-items: flex-start; gap: 500px; margin-top: 50px;">
   
    
      <div style="display: flex; align-items: center; gap: 60px; margin: 40px 0 0 180px;">
  <h3 style="color: blue; font-weight: bold;">Quiz Name: {{ quizTitle }}</h3>
  <h3 style="color: blue; font-weight: bold;">No. of Questions: {{ totalQuestions }}</h3>
  <h3 style="color: blue; font-weight: bold;">Duration: {{ quizDurationMinutes }} min</h3>
</div>
      
    
    </div>

    <div style="display: flex; align-items: flex-start; gap: 20px; margin-top: 50px;">

    <div class="card inset-card p-4 text-center" style="width: 1000px; height: auto; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
     <div v-if="currentQuestionIndex < questionsCopy.length" class="question-card">
    <h4 style="font-weight: bold; color: black;">{{ questionsCopy[currentQuestionIndex].text }}</h4>

    <div v-for="(option, i) in questionsCopy[currentQuestionIndex].options" :key="i" style="font-weight: bold; color: black; font-size: large;">
    <input 
        type="radio" 
        :name="'question-' + questionsCopy[currentQuestionIndex].id" 
        :value="typeof option === 'object' ? option.text : option"
        :checked="userAnswers[questionsCopy[currentQuestionIndex].id] === (typeof option === 'object' ? option.text : option)"
        @change="handleSelection(questionsCopy[currentQuestionIndex].id, typeof option === 'object' ? option.text : option)"
    />
    {{ typeof option === 'object' ? option.text : option }}
    </div>
    </div>

<div v-else>
    <p>All questions completed!</p>
</div>


    <div style="display: flex; align-items: flex-start; gap: 300px; margin-top: 350px;">
        <button class="btn btn-primary" @click="prevQuestion"  style=" margin-left: 50px; margin-top: 50px; border-radius: 20px; background-color: green">Previous</button>

       

        <button class="btn btn-primary" @click="currentQuestionIndex < questionsCopy.length - 1 ? nextQuestion() : submitQuiz()" style=" margin-top: 50px; border-radius: 20px; background-color: green">{{ currentQuestionIndex < questionsCopy.length - 1 ? 'Next' : 'Submit' }}</button>
    </div>



    </div>
    <div class="card inset-card p-4 text-center" style="width: 400px; height: 250px; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
        <div class="timer">Time Left: {{ formatTime(remainingTime) }}</div>

    </div>




    </div>

<div v-if="showRatingCard" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 800px; height: 500px;margin-left: 100px;  border-radius: 10px;">

<h3 style="text-align: center;">Enjoyed the quiz? Rate it!</h3>
    
    <div>
          <span
            v-for="star in 5"
            :key="star"
            @click="setRating(star)"
            @mouseover="hover = star"
            @mouseleave="hover = 0"
            style="font-size: 2rem; cursor: pointer; color: gold; margin-left: 20px;"
          >
            {{ star <= (hover || rating) ? '★' : '☆' }}
          </span>
        </div>

        <button class="btn btn-primary" @click="submitRating" style="width: 100px; margin-left: 320px; margin-top: 50px;">Submit</button>
        <button class="btn btn-danger" @click="closeOverlay" style="margin-top: 20px; margin-left: 320px; width: 100px;">Cancel</button>
      

      <img :src="require('@/assets/88.jpg')" style="height: 200px; width: 350px; margin-left: 200px; "> 
      
</div>
<p v-if="message" :style="{ color: messageColor, marginLeft: '50px', marginTop: '20px' }">
        {{ message }}
      </p>


</div>

<div v-if="showtimesupCard" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 800px; height: 500px;margin-left: 100px;  border-radius: 10px;">

<h3 style="text-align: center; color: red;">Times Up !!! Buddy</h3>


<button class="btn btn-danger" @click="closeOverlay" style="margin-top: 20px; margin-left: 320px; width: 100px;">Back to Home</button>
</div>
</div>




</template>
<script>
import axios from 'axios';
   
  
  export default {
    props: {
        quizName: {
            type: String,
            required: true
        },
        duration: {
            type: String,
            default: '5 minutes' 
        },
        questions: {
            type: String,
            required: true
        }
    },
    data() {
      return {
        questionsCopy: [],
        userAnswers: {},
        currentQuestionIndex: 0,
        isLoading: false,
        remainingTime: parseInt(this.duration) * 60 || 300, 
        timer: null,
        quizTitle: "",
        totalQuestions: 0,
        quizDurationMinutes: 0,
        showRatingCard: false,
        showtimesupCard:false,
        hasSubmitted:false,
        rating:0,
        hover:0,
        quizname:"",
        message:"",

      };
    },
    created() {
     
  const duration = parseInt(this.$route.query.duration) || 5;  

  this.quizTitle = this.$route.query.quizName || "Untitled Quiz";
  this.quizDurationMinutes = duration;                         
  this.remainingTime = duration * 60;                        
  this.totalQuestions = parseInt(this.$route.query.questions) || 10;

  this.startTimer(); 




  try {
    const parsedQuestions = JSON.parse(this.questions);
    this.questionsCopy = parsedQuestions;
  } catch (error) {
    console.warn("Invalid question format from prop, skipping local load.");
  }

  this.fetchQuestions(); 
  this.startTimer();    
},


  beforeUnmount() {
    clearInterval(this.timer); 
  },
  
    
  
    methods: {
      async fetchQuestions() {
  this.isLoading = true;

  try {
    const response = await axios.get(`https://q-fi.onrender.com/get-questions`, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      params: {
        quizName: this.$route.query.quizName,
        duration: this.$route.query.duration,
        questions: this.$route.query.questions
      }
    });

    console.log("API Response:", response.data);
    this.questionsCopy = response.data || [];
    this.userAnswers = Array(this.questionsCopy.length).fill(null);

  } catch (error) {
    console.error("Error fetching questions:", error);
    alert("Failed to load questions. Please try again.");
  } finally {
    this.isLoading = false;
  }
},

  
      nextQuestion() {
        if (this.currentQuestionIndex < this.questionsCopy.length - 1) {
          this.currentQuestionIndex++;
        } else {
          localStorage.setItem('userAnswers', JSON.stringify(this.userAnswers));
          alert("Answers saved successfully!");
        }
      },
  
      prevQuestion() {
        if (this.currentQuestionIndex > 0) {
          this.currentQuestionIndex--;
        }
      },
      startTimer() {
      this.timer = setInterval(() => {
        if (this.remainingTime > 0) {
          this.remainingTime--;
        } else {
          clearInterval(this.timer);

           if (!this.hasSubmitted) {
            this.hasSubmitted = true; // prevent further calls
            this.showtimesupCard = true;
            this.submitQuiz();
}
        }
      }, 1000); 
    },

    formatTime(seconds) {
      const minutes = Math.floor(seconds / 60);
      const secs = seconds % 60;
      return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
    },
    handleSelection(questionId, selectedOption) {
    this.userAnswers = { ...this.userAnswers, [String(questionId)]: selectedOption };
    console.log(` Question ID: ${questionId}, Selected Option: ${selectedOption}`);



},
async submitQuiz() {


    const userAnswersObject = {};

    this.questionsCopy.forEach((question) => {
        const questionId = String(question.id);  
        console.log(`Mapping ID: ${question.id} -> Answer: ${this.userAnswers[questionId] || 'N/A'}`);

        if (this.userAnswers[questionId]) {
            userAnswersObject[questionId] = this.userAnswers[questionId];
        } else {
            console.warn(`No answer provided for question ID: ${question.id}`);
            userAnswersObject[questionId] = null;
        }
    });
     console.log("Quiz name:", this.$route.query.quizName);  
    const payload = {
        quizName: this.$route.query.quizName,
        userAnswers: userAnswersObject,

        duration: this.remainingTime
    };

    console.log("Payload being sent:", payload);

    try {
        const response = await axios.post('https://q-fi.onrender.com/submit-quiz', payload, {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        });

        if (response.data.message) {
            alert(`Quiz submitted successfully! Your score is: ${response.data.score}`);
            this.showRatingCard = true
        } else {
            alert('Submission failed. Please try again.');
        }

    } catch (error) {
        console.error("Error submitting quiz:", error);
        alert("Failed to submit quiz. Please try again.");
    }
},
setRating(star){
  this.rating=star
},
closeOverlay(){
  this.showRatingCard = false
  this.$router.push('/User');
},
closetimesup(){
  this.showtimesupCard = false
  this.$router.push('/User');
},
async submitRating(){
 

      const token = localStorage.getItem('token')

      
      if (!token) {
        alert('You must be logged in to rate.')
        return
      }
      const payload = JSON.parse(atob(token.split('.')[1]))
      const username = payload.sub.split(':')[0]  
      try {
        const response = await axios.post(
          'https://q-fi.onrender.com/submit_quiz_rating',
          {
            username:username,
            quizname: this.$route.query.quizName,
            rating: this.rating
          }
        );
        if (response.data.message) {
            alert(`Quiz  rating submitted successfully!`);
            this.$router.push('/User');
        } else {
            alert('Submission failed. Please try again.');
           }
        
      } catch (err) {
        console.error(err)
        alert('Submission failed. Please try again.');
      }
    }





  }
};

</script>
<style scoped>
.timer {
  font-size: 1.5rem;
  font-weight: bold;
  color: #d9534f;  /* Red color for urgency */
  margin-bottom: 20px;
}
</style>