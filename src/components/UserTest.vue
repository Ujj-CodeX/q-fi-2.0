<template>

    <div style="display: flex; align-items: flex-start; gap: 300px; margin-top: 50px;">
   
    
      <h5 style="color: black; font-weight: bold; margin-left: 300px;">Quiz Name:-</h5>
      <h5 style="color: black; font-weight: bold; margin-left: 20px;">No. of Question:-</h5>
      <h5 style="color: black; font-weight: bold; margin-left: 20px;">Duration:-</h5>
      
    
    </div>

    <div style="display: flex; align-items: flex-start; gap: 20px; margin-top: 50px;">

    <div class="card inset-card p-4 text-center" style="width: 1000px; height: 500px; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
     <div v-if="currentQuestionIndex < questionsCopy.length" class="question-card">
    <p>{{ questionsCopy[currentQuestionIndex].text }}</p>

    <div v-for="(option, i) in questionsCopy[currentQuestionIndex].options" :key="i">
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

        <button class="btn btn-primary"  style="  margin-top: 50px; border-radius: 20px; background-color: green">Submit</button>

        <button class="btn btn-primary" @click="currentQuestionIndex < questionsCopy.length - 1 ? nextQuestion() : submitQuiz()" style=" margin-top: 50px; border-radius: 20px; background-color: green">{{ currentQuestionIndex < questionsCopy.length - 1 ? 'Next' : 'Submit' }}</button>
    </div>



    </div>
    <div class="card inset-card p-4 text-center" style="width: 400px; height: 250px; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
        <div class="timer">Time Left: {{ formatTime(remainingTime) }}</div>

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
        timer: null
      };
    },
    created() {
  this.remainingTime = (parseInt(this.$route.query.duration) || 5) * 60;
  this.totalQuestions = parseInt(this.$route.query.questions) || 10;
  this.quizTitle = this.$route.query.quizName || "Untitled Quiz";



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
    const response = await axios.get(`http://localhost:5000/get-questions`, {
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
          this.submitQuiz();
          this.$router.push('/times-up');

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

    const payload = {
        quizName: this.quizName,
        userAnswers: this.userAnswers,
        duration: this.remainingTime
    };

    console.log("Payload being sent:", payload);

    try {
        const response = await axios.post('http://localhost:5000/submit-quiz', payload, {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        });

        if (response.data.message) {
            alert(`Quiz submitted successfully! Your score is: ${response.data.score}`);
            this.$router.push('/Leaderboard');  
        } else {
            alert('Submission failed. Please try again.');
        }

    } catch (error) {
        console.error("Error submitting quiz:", error);
        alert("Failed to submit quiz. Please try again.");
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