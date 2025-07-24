<template>
 <div style="display: flex; align-items: flex-start;">
   
    <div class="sidebar-card">
      <h5 style="color: white; margin-left: 20px;">Admin Management</h5>
      <router-link class="nav-link" style="color:whitesmoke; cursor:pointer; display: block; margin-top:30px;" to="/Admin_Dash">Academics Management</router-link>
       <router-link class="nav-link" style="color:whitesmoke;cursor:pointer; display: block; margin-top:30px;" to="/Admin_User">User Management</router-link>
       <router-link class="nav-link" style="color:whitesmoke; cursor:pointer;display: block; margin-top:30px;" to="/Admin_Quiz">Quiz Management</router-link>
       <a class="nav-link" 
   style="color:whitesmoke; display: block; margin-top:30px; cursor:pointer; font-weight: bold;" 
   @click="logout">
   Logout</a>
   <button class="btn btn-primary" style="background-color: white; color: black; margin-top: 20px;  border-radius: 10px;" @click="sendmonthlyreminder">Send Monthly Reminder</button>
    </div>


    <div style="flex: 2; padding: 10px;">


    <h2 style="font-weight: bold; margin-left: 550px; margin-top: 50px;">Quiz Management</h2>
    <h5 style="font-weight: bold; margin-top: 50px; margin-left: 350px;">After Successfully creating a new Quiz click on the button below to send Reminder</h5>
    <a @click="sendReminder()" class="btn btn-primary" style="margin-left: 620px; margin-top: 50px; border-radius: 20px; background-color: red;">Send Reminder</a>
    <div class="card inset-card p-4 text-center" style="width: 1300px; height: auto; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
    <div style="display: flex; align-items: flex-start; gap: 40px; margin-top: 0px;">
        <div class="dropdown-container">
        <select v-model="selectedCourse" @change="fetchSubjects" style="border-radius: 8px; margin-left: 250px; margin-top: 50px;">
          <option value="" disabled >Select Course</option>
          <option v-for="course in courses" :key="course.id" :value="course.id" style="border-radius: 8px;">{{ course.name }}</option>
        </select>

        <select v-model="selectedSubject" @change="fetchChapters" style="margin-left: 200px; border-radius: 8px;">
          <option value="" disabled >Select Subject</option>
          <option v-for="subject in subjects" :key="subject.id" :value="subject.id" style="border-radius: 8px;">{{ subject.name }}</option>
        </select>

        <select v-model="selectedChapter" @change="fetchQuestions" style="margin-left: 200px; border-radius: 8px;">
          <option value="" disabled >Select Chapter</option>
          <option v-for="chapter in chapters" :key="chapter.id" :value="chapter.id" style="border-radius: 8px;">{{ chapter.name }}</option>
        </select>
      </div>
    </div>
    <div style="display: flex; align-items: flex-start; gap: 200px; ">
    <h4 style="font-weight: bold; margin-left: 500px; margin-top: 60px;">Existing Questions</h4>
     
    
    <button class="btn btn-primary" @click="showcard = true " style=" margin-left: 100px; margin-top: 50px; border-radius: 20px; background-color: rgb(3, 3, 137);">Add +</button>
    
     
     
   </div>
   


<div class="card inset-card p-4 text-center" style="width: 1200px; height: auto; margin-left: 30px; margin-top: 50px; border-radius: 10px;">
  <div v-for="question in questions" :key="question.id" class="question-card">
   <div style="display: flex; align-items: flex-start;">
  <h4>Question-  {{ question.text }}</h4>
  <button @click="deleteQuestion(question.id)" class="btn btn-danger btn-sm" style="margin-left: auto;">Delete</button>
  <button @click="editQuestion(question)" class="btn btn-primary btn-sm" style="margin-left: 10px;">Edit</button>
  </div> 
  <ul>
  <li v-for="option in question.options" :key="option.id" style="margin-top: 10px;">
    <span :class="{'text-success font-weight-bold': option.text === question.correctAnswer}" >
      {{ option.text }} <span v-if="option.text === question.correctAnswer">(✔️)</span>
    </span>
     

    
  </li>
</ul>

</div>
</div>


  
</div>
</div>


<div v-if="showcard" class="overlay">

<div class="card inset-card p-4 text-center" style="position: absolute;  width: 1200px; height: 600px;margin-left: 300px; margin-top: 100px; border-radius: 10px;">
 <h2 style="font-weight: bold;  margin-top: 50px;">Add new Questions</h2>
 <div style="display: flex; align-items: flex-start; gap: 40px; margin-top: 0px;">




  <div class="dropdown-container" >
        <select v-model="selectedCourse" @change="fetchSubjects" style="border-radius: 8px; margin-left: 250px; margin-top: 50px;">
          <option value="" disabled >Select Course</option>
          <option v-for="course in courses" :key="course.id" :value="course.id" style="border-radius: 8px;">{{ course.name }}</option>
        </select>

        <select v-model="selectedSubject" @change="fetchChapters" style="margin-left: 200px; border-radius: 8px;">
          <option value="" disabled >Select Subject</option>
          <option v-for="subject in subjects" :key="subject.id" :value="subject.id" style="border-radius: 8px;">{{ subject.name }}</option>
        </select>

        <select v-model="selectedChapter" @change="fetchQuestions" style="margin-left: 200px; border-radius: 8px;">
          <option value="" disabled >Select Chapter</option>
          <option v-for="chapter in chapters" :key="chapter.id" :value="chapter.id" style="border-radius: 8px;">{{ chapter.name }}</option>
        </select>
      </div>
        

    </div>

    <div class="add-question" style="margin-top: 20px;">
        <input class="form-control"  v-model="newQuestion" placeholder="Enter new question" />
        <div v-for="(option, index) in newOptions" :key="index">
          <input class="form-control" style="margin-top: 5px;" v-model="newOptions[index]" placeholder="Enter option" />
        </div>
        <input class="form-control" style="margin-top: 5px;" v-model="correctAnswer" placeholder="Enter correct answer" /><br>
        <button class="btn btn-primary" @click="addOption">+ Add Option</button>
        <button class="btn btn-success" @click="submitQuestion" style="margin-left: 10px;">Submit</button>
      </div>


</div>
</div>

</div>
<div v-if="showeditcard" class="overlay">
  <div class="card inset-card p-4 text-center" style="position: absolute; width: 1200px; height: 600px; margin-left: 300px; margin-top: 100px; border-radius: 10px;">
    <h2 style="font-weight: bold; margin-top: 50px;">Edit Question</h2>

    <div class="add-question" style="margin-top: 20px;">
      <input class="form-control" v-model="newQuestion" placeholder="Edit question" />
      <div v-for="(option, index) in newOptions" :key="index">
        <input class="form-control" style="margin-top: 5px;" v-model="newOptions[index]" placeholder="Edit option" />
      </div>
      <input class="form-control" style="margin-top: 5px;" v-model="correctAnswer" placeholder="Edit correct answer" /><br>
      
      <button class="btn btn-success" @click="saveEditedQuestion" style="margin-left: 10px;">Save Changes</button>
    </div>
  </div>
</div>
</template>
<script>
import { auth } from '../store';
import axios from 'axios';
import { useRouter } from 'vue-router';


export default{
  setup(){
      const router = useRouter()
      function logout(){
  localStorage.removeItem('admin_token');
  auth.isLoggedIn = false;
  router.push('/admin');
}

      return { logout, auth };

    },
  data (){
    return {
      courses: [],
      subjects: [],
      chapters: [],
      questions: [],

      showcard:false,
      showeditcard:false,

      selectedCourse:'',
      selectedChapter:'' ,
      selectedSubject:'' ,

      newQuestion: '',
      newOptions: ['', '', '', ''],
      correctAnswer: '',
      




    };
  },
  mounted() {
      this.fetchCourses();
      
    },

  
  methods: {
      async fetchCourses() {
        try {
          const response = await axios.get('https://q-fi.onrender.com/courses');
          this.courses = response.data;
        } catch (error) {
          console.error('Error fetching courses:', error);
        }
      },

      async fetchSubjects() {
        try {
          const response = await axios.get(`https://q-fi.onrender.com/subjects/${this.selectedCourse}`);
          this.subjects = response.data;
        } catch (error) {
          console.error('Error fetching subjects:', error);
        }
      },

      async fetchChapters() {
        try {
          const response = await axios.get(`https://q-fi.onrender.com/chapters/${this.selectedSubject}/${this.selectedCourse}`);
          this.chapters = response.data;
        } catch (error) {
          console.error('Error fetching chapters:', error);
        }
      },
      async fetchQuestions() {
        try {
          const token = localStorage.getItem('admin_token');
            const response = await axios.get(`https://q-fi.onrender.com/api/get_questions/${this.selectedChapter}`,{headers: {
        'Authorization': `Bearer ${token}` 
      }} );
            console.log('Fetched Questions:', response.data); 
            this.questions = Array.isArray(response.data) ? response.data : [];
        } catch (error) {
            console.error('Error fetching questions:', error);
            alert('Failed to fetch questions. Please try again. Might Need Authorization');
        }
    },
      async submitQuestion() {
        try {
          const token = localStorage.getItem('admin_token');
            await axios.post('https://q-fi.onrender.com/api/questions', {
                question: this.newQuestion,
                options: this.newOptions,
                correctAnswer: this.correctAnswer,
                chapter: this.selectedChapter
            },
          {headers: {
        'Authorization': `Bearer ${token}` 
      }});
            alert('Question added successfully!');
            this.newQuestion = '';
            this.newOptions = ['', '', '', ''];
            this.correctAnswer = '';
        } catch (error) {
            console.error('Error adding question:', error);
            alert('Failed to add question. Please try again.');
        }
    },

    editQuestion(question) {
    this.editingQuestionId = question.id;
    this.newQuestion = question.text;

   
    if (Array.isArray(question.options)) {
        this.newOptions = question.options.map(opt => opt.text || '');
    } else {
       
        this.newOptions = ['', '', '', ''];
    }

    this.correctAnswer = question.correctAnswer || '';
    this.showeditcard = true;
},


    async saveEditedQuestion() {
        try {
          const token = localStorage.getItem('admin_token');
            await axios.put(`https://q-fi.onrender.com/api/edit_question/${this.editingQuestionId}`, {
              
                question: this.newQuestion,
                options: this.newOptions,
                correctAnswer: this.correctAnswer
            }, {headers: {
        'Authorization': `Bearer ${token}` 
      }}
          );
            alert('Question updated successfully!');
            this.fetchQuestions();
            this.resetForm();
        } catch (error) {
            console.error('Error editing question:', error);
            alert('Failed to edit question. Please try again.');
        }
    },

    resetForm() {
        this.editingQuestionId = null;
        this.newQuestion = '';
        this.newOptions = ['', '', '', ''];
        this.correctAnswer = '';
    },

    async deleteQuestion(questionId) {
        if (confirm('Are you sure you want to delete this question?')) {
            try {
              const token = localStorage.getItem('admin_token');
                await axios.delete(`https://q-fi.onrender.com/api/delete_question/${questionId}`,{headers: {
           'Authorization': `Bearer ${token}` 
      }});
                alert('Question deleted successfully!');
                this.fetchQuestions();
            } catch (error) {
                console.error('Error deleting question:', error);
                alert('Failed to delete question. Please try again.');
            }
        }
    },
    sendReminder() {
      const token = localStorage.getItem('admin_token');
    fetch("https://q-fi.onrender.com/send-reminder", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${(token)}`,
      }
    })
      .then(res => res.json())
      .then(data => {
        alert(data.message); 
      })
      .catch(err => {
        console.error("❌ Error sending reminders:", err);
      });
  },
  sendmonthlyreminder() {
      const token = localStorage.getItem('admin_token');
    fetch("https://q-fi.onrender.com/send-monthly-reminder", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${(token)}`,
      }
    })
      .then(res => res.json())
      .then(data => {
        alert(data.message); 
      })
      .catch(err => {
        console.error("❌ Error sending reminders:", err);
      });
    }
  
}





    }




</script>
<style>
.inset-card {
  background: white;
  border-radius: 12px;
  box-shadow: 
    inset 0 0 5px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease-in-out;
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
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
</style>
