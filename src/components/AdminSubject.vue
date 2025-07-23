<template>
  <div style="display: flex; align-items: flex-start;">
    <div class="sidebar-card">
      <h5 style="color: white; margin-left: 20px;">Admin Management</h5>
      
       <a class="nav-link" style="color:whitesmoke; cursor:pointer; display: block; margin-top:30px;" href="/Admin_Dash">Academics Management</a>
       <a class="nav-link" style="color:whitesmoke;cursor:pointer; display: block; margin-top:30px;" href="/Admin_User">User Management</a>
       <a class="nav-link" style="color:whitesmoke; cursor:pointer;display: block; margin-top:30px;" href="/Admin_Quiz">Quiz Management</a>
       <a class="nav-link" 
   style="color:whitesmoke; display: block; margin-top:30px; cursor:pointer; font-weight: bold;" 
    @click="logout">
   Logout</a>
   <button class="btn btn-primary" style="background-color: white; color: black; margin-top: 20px;  border-radius: 10px;" @click="sendmonthlyreminder">Send Monthly Reminder</button>
    </div>

    <div style="flex: 1; padding: 20px;">
      <h2 style="font-weight: bold; text-align: center; margin-top: 30px;">Courses and Subject Management</h2>

      <div class="card inset-card p-4 text-center" style="width: 100%; margin-top: 30px; border-radius: 10px;">
        <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">

          
          <div class="card" style="border-radius: 10px; width: 350px; background-color: #dfe6e9;">
            <div class="card-body">
              <h5 class="card-title">Courses</h5>
              
              <ul class="list-group">
                <li
                  v-for="course in courses"
                  :key="course.id"
                  class="list-group-item d-flex justify-content-between align-items-center"
                >
                  {{ course.name }}
                  <span>
                    <button @click="editCourse(course)" class="btn btn-sm btn-outline-primary">Edit</button>
                    <button @click="deleteCourse(course.id)" class="btn btn-sm btn-outline-danger ms-1" style="margin-left: 8px;">Delete</button>
                  </span>
                </li>
              </ul>

              <button
                @click="showAddCourseForm = true"
                class="btn btn-primary"
                style="margin-top: 15px; border-radius: 20px; background-color: rgb(3, 3, 137);">+</button>
            </div>
          </div>

          <div v-if="showAddCourseForm" class="form-card card p-3" style="width: 350px; border-radius: 10px;">
            <h4>Add New Course</h4>
            <input v-model="newCourseName" placeholder="Course Name" class="form-control mb-2" />
            <button @click="addCourse" class="btn btn-success btn-sm">Add</button>
            <button @click="showAddCourseForm = false" class="btn btn-secondary btn-sm ms-1" style="margin-top: 8px;">Cancel</button>
          </div>

          
          <div class="card" style="border-radius: 10px; width: 350px; background-color: #dfe6e9;">
            <div class="card-body">
              <h5 class="card-title">Subjects</h5>

              <select v-model="selectedCourse" @change="fetchSubjects" class="form-select mb-3" style="border-radius: 10px;">
                <option disabled value="">Choose Course</option>
                <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.name }}</option>
              </select>

              <ul class="list-group">
                <li
                  v-for="subject in filteredSubjects"
                  :key="subject.id"
                  class="list-group-item d-flex justify-content-between align-items-center"
                >
                  {{ subject.name }}
                  <span>
                    <button @click="editSubject(subject)" class="btn btn-sm btn-outline-primary">Edit</button>
                    <button @click="deleteSubject(subject.id)" class="btn btn-sm btn-outline-danger ms-1" style="margin-left: 8px;">Delete</button>
                  </span>
                </li>
              </ul>

              <button
                @click="showAddSubjectForm = true"
                class="btn btn-primary"
                style="margin-top: 15px; border-radius: 20px; background-color: rgb(3, 3, 137);">+</button>
            </div>
          </div>

          <div v-if="showAddSubjectForm" class="form-card card p-3" style="width: 350px; border-radius: 10px;">
            <h4>Add New Subject</h4>
            <input v-model="newSubjectName" placeholder="Subject Name" class="form-control mb-2" />
            <button @click="addSubject" class="btn btn-success btn-sm" >Add</button>
            <button @click="showAddSubjectForm = false" class="btn btn-secondary btn-sm ms-1" style="margin-top: 8px;">Cancel</button>
          </div>

          
          <div class="card" style="border-radius: 10px; width: 350px; background-color: #dfe6e9;">
            <div class="card-body">
              <h5 class="card-title">Quizzes</h5>

              <select v-model="selectedCourse" @change="fetchSubjects" class="form-select mb-2" style="border-radius: 10px;">
                <option disabled value="">Choose Course</option>
                <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.name }}</option>
              </select>

              <select v-model="selectedSubject" @change="fetchChapters" class="form-select mb-3" style="border-radius: 10px; margin-left: 8px;">
                <option disabled value="">Choose Subject</option>
                <option v-for="subject in filteredSubjects" :key="subject.id" :value="subject.id">{{ subject.name }}</option>
              </select>

              <ul class="list-group">
                <li
                  v-for="chapter in filteredChapters"
                  :key="chapter.id"
                  class="list-group-item d-flex justify-content-between align-items-center"
                >
                  {{ chapter.name }}
                  <span>
                    <button @click="editChapter(chapter)" class="btn btn-sm btn-outline-primary">Edit</button>
                    <button @click="deleteChapter(chapter.id)" class="btn btn-sm btn-outline-danger ms-1" style="margin-left: 5px;">Delete</button>
                  </span>
                </li>
              </ul>

              <button
                @click="showAddChapterForm = true"
                class="btn btn-primary"
                style="margin-top: 15px; border-radius: 20px; background-color: rgb(3, 3, 137);">+</button>
            </div>
          </div>

          <div v-if="showAddChapterForm" class="form-card card p-3" style="width: 350px; border-radius: 10px;">
            <h4>Add New Chapter</h4>
            <input v-model="newChapterName" placeholder="Chapter Name" class="form-control mb-2" />
            <button @click="addChapter" class="btn btn-success btn-sm">Add</button><br>
            <button @click="showAddChapterForm = false" class="btn btn-secondary btn-sm ms-1" style="margin-top: 8px;">Cancel</button>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { auth } from '../store';
import axios from 'axios';
import { useRouter } from 'vue-router';

  export default {
    setup(){
      const router = useRouter()
      function logout(){
  localStorage.removeItem('admin_token');
  auth.isLoggedIn = false;
  router.push('/admin');
}

      return { logout, auth };

    },
    data() {
      return {
        courses: [],
        subjects: [],
        chapters: [],
  
        newCourseName: '',
        newSubjectName: '',
        newChapterName: '',
  
        selectedCourse:'',
        selectedChapterCourse:'' ,
        selectedSubject:'' ,
  
        showAddCourseForm: false,
        showAddSubjectForm: false,
        showAddChapterForm: false,
        
      };
    },
    
  
    mounted() {
      this.fetchCourses();
      this.fetchChapters();
    },
    computed: {
      filteredSubjects() {
      return this.subjects.filter(sub => sub.courseId === this.selectedCourse);
    },
    filteredChapters() {
      return this.chapters.filter(
        chap => chap.courseId === this.selectedCourse && chap.subjectId === this.selectedSubject
      );
    },


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
  
      async addCourse() {
        try {
          const token = localStorage.getItem('admin_token');

          await axios.post('http://localhost:5000/add-course', { name: this.newCourseName },{headers: {
        'Authorization': `Bearer ${token}` 
      }});
          this.fetchCourses();
          this.showAddCourseForm = false;
          this.newCourseName = '';
        } catch (error) {
          console.error('Error adding course:', error);
        }
      },
  
      async deleteCourse(courseId) {
        try {
          const token = localStorage.getItem('admin_token');
          await axios.delete(`http://localhost:5000/delete-course/${courseId}`,{headers: {
        'Authorization': `Bearer ${token}` 
      }});
          this.fetchCourses();
        } catch (error) {
          console.error('Error deleting course:', error);
        }
      },
      async deleteSubject(subjectId) {
    try {
      const token = localStorage.getItem('admin_token');
        await axios.delete(`http://localhost:5000/delete-subject/${subjectId}`,{headers: {
        'Authorization': `Bearer ${token}` 
      }});
        this.subjects = this.subjects.filter(subject => subject.id !== subjectId);
    } catch (error) {
        console.error('Error deleting subject:', error);
    }
}
,
async deleteChapter(chapterId) {
    try {
      const token = localStorage.getItem('admin_token');
        await axios.delete(`http://localhost:5000/delete-chapter/${chapterId}`,{headers: {
        'Authorization': `Bearer ${token}` 
      }});
        this.chapters = this.chapters.filter(chapter => chapter.id !== chapterId);
    } catch (error) {
        console.error('Error deleting chapter:', error);
    }
},
  
      async addSubject() {
        try {
          const token = localStorage.getItem('admin_token');
          await axios.post('http://localhost:5000/add-subject', {
            name: this.newSubjectName,
            course_id: this.selectedCourse
          },{headers: {
        'Authorization': `Bearer ${token}` 
      }});
          this.showAddSubjectForm = false;
          this.fetchSubjects();
          this.newSubjectName = '';
        } catch (error) {
          console.error('Error adding subject:', error);
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
  
      async addChapter() {
        try {
          const token = localStorage.getItem('admin_token');
          await axios.post('http://localhost:5000/add-chapter', {
            name: this.newChapterName,
            subject_id: this.selectedSubject
          },{headers: {
        'Authorization': `Bearer ${token}` 
      }});
          this.showAddChapterForm = false;
          this.fetchChapters();
          this.newChapterName = '';
        } catch (error) {
          console.error('Error adding chapter:', error);
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

      async editCourse(course) {
    const updatedName = prompt('Enter new course name:', course.name);
    if (updatedName && updatedName.trim()) {
      try {
        const token = localStorage.getItem('admin_token');
        await axios.put(`http://localhost:5000/edit-course/${course.id}`, { name: updatedName.trim() },{headers: {
        'Authorization': `Bearer ${token}` 
      }});
        this.fetchCourses();
      } catch (error) {
        console.error('Error editing course:', error);
      }
    }
  },

  async editSubject(subject) {
    const updatedName = prompt('Enter new subject name:', subject.name);
    if (updatedName && updatedName.trim()) {
      try {
        const token = localStorage.getItem('admin_token');
        await axios.put(`http://localhost:5000/edit-subject/${subject.id}`, { name: updatedName.trim() },{headers: {
        'Authorization': `Bearer ${token}` 
      }});
        this.fetchSubjects();
      } catch (error) {
        console.error('Error editing subject:', error);
      }
    }
  },

  async editChapter(chapter) {
    const updatedName = prompt('Enter new chapter name:', chapter.name);
    if (updatedName && updatedName.trim()) {
      try {
        const token = localStorage.getItem('admin_token');
        await axios.put(`http://localhost:5000/edit-chapter/${chapter.id}`, { name: updatedName.trim() },{headers: {
        'Authorization': `Bearer ${token}` 
      }});
        this.fetchChapters();
      } catch (error) {
        console.error('Error editing chapter:', error);
      }
    }
  },
  sendmonthlyreminder() {
      const token = localStorage.getItem('admin_token');
    fetch("http://localhost:5000/send-monthly-reminder", {
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
    
  };
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

</style>
