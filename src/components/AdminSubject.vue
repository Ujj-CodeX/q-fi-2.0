<template>
<div style="display: flex; align-items: flex-start;">
   
    <div class="sidebar-card">
      <h5 style="color: white; margin-left: 20px;">Admin Management</h5>
      <hr>
    </div>
   <div style="flex: 2; padding: 10px;">

    <h2 style="font-weight: bold; margin-left: 450px; margin-top: 50px;">Courses and Subject Management</h2>
    <div class="card inset-card p-4 text-center" style="width: 1300px; height: 500px; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
    <div style="display: flex; align-items: flex-start; gap: 40px; margin-top: 0px;">

        <div class="card" style=" border-radius: 10px; width: 350px; height: 400px; margin-left: 50px; background-color: #dfe6e9; margin-top: 20px;">
       <div class="card-body">
          <h5 class="card-title">Courses</h5>
          <div class="dropdown" >
           <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="background-color: white; color: black; border-radius: 10px;">
          Choose Courses
           </button>
         <ul class="dropdown-menu dropdown-menu-dark">
         <li v-for="course in courses" :key="course.id">
            {{ course.name }}
            <button @click="editCourse(course)">Edit</button>
            <button @click="deleteCourse(course.id)">Delete</button>
          </li>
         </ul>
         </div>
          
        <button @click="showAddSubjectForm = true" class="btn btn-primary" style="margin-top: 250px; border-radius: 20px; background-color: rgb(3, 3, 137);">+</button>
        </div>
        </div>

        <div class="card" style="border-radius: 10px; width: 350px; height: 400px; background-color: #dfe6e9; border-radius: 10px; margin-top: 20px;">
       <div class="card-body">
          <h5 class="card-title">Subjects</h5>
          <div class="dropdown" >
           <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="background-color: white; color: black; border-radius: 10px;">
          Choose Subjects
           </button>
         <ul class="dropdown-menu dropdown-menu-dark">
         
         </ul>
         </div>
          
        <a href="#" class="btn btn-primary" style="margin-top: 250px; border-radius: 20px; background-color: rgb(3, 3, 137);">+</a>
        </div>
        </div>

        <div class="card" style="border-radius: 10px; width: 350px; height: 400px; background-color: #dfe6e9; margin-top: 20px;">
       <div class="card-body">
          <h5 class="card-title">Quizes</h5>
          <div class="dropdown" >
           <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="background-color: white; color: black; border-radius: 10px;">
          Choose Course
           </button>
           <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="background-color: white; color: black; border-radius: 10px; margin-left: 5px;">
          Choose Subject
           </button>
         <ul class="dropdown-menu dropdown-menu-dark">
         <li><a class="dropdown-item active" href="#">Action</a></li>
         <li><a class="dropdown-item" href="#">Another action</a></li>
         <li><a class="dropdown-item" href="#">Something else here</a></li>
         <li><hr class="dropdown-divider"></li>
         <li><a class="dropdown-item" href="#">Separated link</a></li>
         </ul>
         </div>
          
        <a href="#" class="btn btn-primary" style="margin-top: 250px; border-radius: 20px; background-color: rgb(3, 3, 137);">+</a>
        </div>
        </div>


    </div>
</div>
</div>
</div>



</template>
<script>
import axios from 'axios';
  
  export default {
    data() {
      return {
        courses: [],
        subjects: [],
        chapters: [],
  
        newCourseName: '',
        newSubjectName: '',
        newChapterName: '',
  
        selectedCourse: null,
        selectedChapterCourse: null,
        selectedSubject: null,
  
        showAddCourseForm: false,
        showAddSubjectForm: false,
        showAddChapterForm: false
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
  
      async addCourse() {
        try {
          await axios.post('http://localhost:5000/add-course', { name: this.newCourseName });
          this.fetchCourses();
          this.showAddCourseForm = false;
          this.newCourseName = '';
        } catch (error) {
          console.error('Error adding course:', error);
        }
      },
  
      async deleteCourse(courseId) {
        try {
          await axios.delete(`http://localhost:5000/delete-course/${courseId}`);
          this.fetchCourses();
        } catch (error) {
          console.error('Error deleting course:', error);
        }
      },
      async deleteSubject(subjectId) {
    try {
        await axios.delete(`http://localhost:5000/delete-subject/${subjectId}`);
        this.subjects = this.subjects.filter(subject => subject.id !== subjectId);
    } catch (error) {
        console.error('Error deleting subject:', error);
    }
}
,
async deleteChapter(chapterId) {
    try {
        await axios.delete(`http://localhost:5000/delete-chapter/${chapterId}`);
        this.chapters = this.chapters.filter(chapter => chapter.id !== chapterId);
    } catch (error) {
        console.error('Error deleting chapter:', error);
    }
},
  
      async addSubject() {
        try {
          await axios.post('http://localhost:5000/add-subject', {
            name: this.newSubjectName,
            course_id: this.selectedCourse
          });
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
          await axios.post('http://localhost:5000/add-chapter', {
            name: this.newChapterName,
            subject_id: this.selectedSubject
          });
          this.showAddChapterForm = false;
          this.fetchChapters();
          this.newChapterName = '';
        } catch (error) {
          console.error('Error adding chapter:', error);
        }
      },
  
      async fetchChapters() {
        try {
          const response = await axios.get(`http://localhost:5000/chapters/${this.selectedSubject}`);
          this.chapters = response.data;
        } catch (error) {
          console.error('Error fetching chapters:', error);
        }
      },

      async sendReminders() {
      try {
        const response = await fetch('http://localhost:5000/send-reminders', {
          method: 'POST',
        });

        const data = await response.json();
        console.log(data.message);
        alert('Reminders sent!');
      } catch (error) {
        console.error('Error sending reminders:', error);
      }
      },
      async editCourse(course) {
    const updatedName = prompt('Enter new course name:', course.name);
    if (updatedName && updatedName.trim()) {
      try {
        await axios.put(`http://localhost:5000/edit-course/${course.id}`, { name: updatedName.trim() });
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
        await axios.put(`http://localhost:5000/edit-subject/${subject.id}`, { name: updatedName.trim() });
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
        await axios.put(`http://localhost:5000/edit-chapter/${chapter.id}`, { name: updatedName.trim() });
        this.fetchChapters();
      } catch (error) {
        console.error('Error editing chapter:', error);
      }
    }
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
