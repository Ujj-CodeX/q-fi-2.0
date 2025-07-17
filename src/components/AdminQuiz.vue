<template>
 <div style="display: flex; align-items: flex-start;">
   
    <div class="sidebar-card">
      <h5 style="color: white; margin-left: 20px;">Admin Management</h5>
      <a class="nav-link" style="color:whitesmoke; display: block; margin-top:30px;" href="/Admin_Dash">Academics Management</a>
       <a class="nav-link" style="color:whitesmoke; display: block; margin-top:30px;" href="/Admin_User">User Management</a>
       <a class="nav-link" style="color:whitesmoke; display: block; margin-top:30px;" href="/Admin_Quiz">Quiz Management</a>
 
    </div>


    <div style="flex: 2; padding: 10px;">


    <h2 style="font-weight: bold; margin-left: 550px; margin-top: 50px;">Quiz Management</h2>
    <h5 style="font-weight: bold; margin-top: 50px; margin-left: 350px;">After Successfully creating a new Quiz click on the button below to send Reminder</h5>
    <a href="#" class="btn btn-primary" style="margin-left: 620px; margin-top: 50px; border-radius: 20px; background-color: red;">Send Reminder</a>
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
   


<div class="card inset-card p-4 text-center" style="width: 1200px; height: 500px; margin-left: 30px; margin-top: 50px; border-radius: 10px;">
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
     <button @click="deleteQuestion(question.id)" class="btn btn-primary btn-sm" style="margin-left: 10px;">Edit</button>


    
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
import axios from 'axios';
export default{
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
          const response = await axios.get('http://localhost:5000/courses');
          this.courses = response.data;
        } catch (error) {
          console.error('Error fetching courses:', error);
        }
      },

      async fetchSubjects() {
        try {
          const response = await axios.get(`http://localhost:5000/subjects/${this.selectedCourse}`);
          this.subjects = response.data;
        } catch (error) {
          console.error('Error fetching subjects:', error);
        }
      },

      async fetchChapters() {
        try {
          const response = await axios.get(`http://localhost:5000/chapters/${this.selectedSubject}/${this.selectedCourse}`);
          this.chapters = response.data;
        } catch (error) {
          console.error('Error fetching chapters:', error);
        }
      },
      async fetchQuestions() {
        try {
            const response = await axios.get(`http://localhost:5000/api/get_questions/${this.selectedChapter}`);
            console.log('Fetched Questions:', response.data); 
            this.questions = Array.isArray(response.data) ? response.data : [];
        } catch (error) {
            console.error('Error fetching questions:', error);
            alert('Failed to fetch questions. Please try again.');
        }
    },
      async submitQuestion() {
        try {
            await axios.post('http://localhost:5000/api/questions', {
                question: this.newQuestion,
                options: this.newOptions,
                correctAnswer: this.correctAnswer,
                chapter: this.selectedChapter
            });
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
            await axios.put(`http://localhost:5000/api/edit_question/${this.editingQuestionId}`, {
                question: this.newQuestion,
                options: this.newOptions,
                correctAnswer: this.correctAnswer
            });
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
                await axios.delete(`http://localhost:5000/api/delete_question/${questionId}`);
                alert('Question deleted successfully!');
                this.fetchQuestions();
            } catch (error) {
                console.error('Error deleting question:', error);
                alert('Failed to delete question. Please try again.');
            }
        }
    }





    },



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
