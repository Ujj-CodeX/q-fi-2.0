<template>
  <div class="container mt-5 mb-5">
    <div class="row align-items-center justify-content-center">
      <!-- Registration Card -->
      <div class="col-lg-6 col-md-8 col-sm-12 mb-4">
        <div class="card inset-card p-4 text-center" style="border-radius: 15px;">
          <form @submit.prevent="handleSignup">
            <h4 style="color: black; text-align: center;">Registration</h4>
            <br />

            <div class="row g-2">
              <div class="col-6">
                <input type="text" v-model="formData.username" class="form-control" placeholder="Username" name="username" style="font-weight: bold;" />
              </div>
              <div class="col-6">
                <input type="password" v-model="formData.password" class="form-control" placeholder="Password" name="password" style="font-weight: bold;" />
              </div>
            </div><br />

            <input type="text" v-model="formData.name" class="form-control mb-3" placeholder="Full Name" name="name" style="font-weight: bold;" />

            <div class="row g-2">
              <div class="col-6">
                <select v-model="formData.gender" name="gender" class="form-control" style="font-weight: bold;">
                  <option disabled value="">Choose your Gender</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                  <option value="Other">Other</option>
                </select>
              </div>
              <div class="col-6">
                <input type="date" v-model="formData.birthdate" class="form-control" name="dob" style="font-weight: bold;" />
              </div>
            </div><br />

            <input type="email" v-model="formData.email" class="form-control mb-3" placeholder="Email ID" name="email" style="font-weight: bold;" />

            <select v-model="formData.course" name="course" class="form-control mb-3" required style="font-weight: bold;">
              <option value="">Select your Preferred Course</option>
              <option v-for="course in courses" :key="course.id" :value="course.name">{{ course.name }}</option>
            </select>

            <button type="submit" class="btn btn-primary w-100" style="background-color: rgb(3, 3, 137);">Register Now</button>

            <h7 style="margin-top: 20px; display: block; text-align: center;">Already have an ID?</h7>
            <a href="/Partner_login" class="btn btn-primary w-100 mt-2" style="background-color: rgb(3, 3, 137);">Login</a>
          </form>
        </div>
      </div>

      <!-- Responsive Image -->
      <div class="col-lg-5 col-md-8 col-sm-12 text-center">
        <img :src="require('@/assets/15.png')" class="img-fluid" alt="Illustration" style="max-height: 600px;" />
      </div>
    </div>
  </div>
</template>

<script >
import axios from 'axios';
export default{
    data() {
        return {
            formData: {
                username: '',
                name: '',
                email: '',
                birthdate: '',
                gender: '',
                course: '',
                password: ''
               
            },
            courses: []
        };

    },
    methods:{

        async fetchcourses(){
            try{
                const responses =await axios.get('https://q-fi.onrender.com/courses');
                this.courses = responses.data;
                
            }catch(error){
                console.error('Error fetching courses:', error)
            }

        },
        async handleSignup() {
        try {
            const payload = {
                username: this.formData.username,
                email: this.formData.email,
                dob: this.formData.birthdate,
                gender: this.formData.gender,
                course: this.formData.course,
                password: this.formData.password,
                name: this.formData.name

            };
            console.log('Signup payload:', payload);

            const response = await axios.post('https://q-fi.onrender.com/SignUp', payload);
  
          if (response.data.success) {
            alert(response.data.message || 'Signup successful!');
            this.$router.push('/');
          } else {
            alert(response.data.error || 'Signup failed. Please try again.');
          }
        }
        catch (error) {
          console.error('Signup error:', error);
          alert('Error during signup. Please try again.');
        }



    }

},
mounted(){
    this.fetchcourses();
}
};

</script>

<style>
</style>