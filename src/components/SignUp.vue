<template>
<div style="display: flex; align-items: flex-start; " >
    
    <div class="card inset-card p-4 text-center" style="width: 800px;  margin-top: 50px; margin-bottom: 50px; border-radius: 15px; margin-left: 100px;">
  <div class="row g-0">
    
    <div class="col-md-10">
      <div class="card-body" style="margin-left: 100px;">

        <form @submit.prevent="handleSignup">
            <h4 style="color: black; text-align: center;">Registration</h4>
            <br>
            <div style="display: flex; flex-direction: row; gap: 5px;">
            
            <input type="text" v-model="formData.username" class="form-control" id="username" placeholder="Username" style="font-weight: bold;" name="username"><br>
            <input type="password" v-model="formData.password" class="form-control" id="password" placeholder="Password" style="font-weight: bold;" name="password"><br>
            </div><br>

            <div style="display: flex; flex-direction: row; gap: 5px;">
            
            <input type="text" v-model="formData.name" class="form-control" id="fullname" placeholder="Full Name" style="font-weight: bold;" name="name"><br>
            
            
            </div><br>

            <div style="display: flex; flex-direction: row; gap: 5px;">
            <div class="col-auto">
                <select id="gender" v-model="formData.gender" name="gender" class="form-control" style="width: 100%; font-weight: bold;" >
                    <option disabled value="" >Choose your Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>
            </div><br>
            <input type="date" v-model="formData.birthdate" class="form-control" id="dob" placeholder="Date of Birth" style="font-weight: bold;" name="dob"><br>

            </div><br>
            
            <input type="email" v-model="formData.email" class="form-control" id="email" placeholder="Email ID" style="font-weight: bold;" name="email"><br>

            <select id="services" v-model="formData.course" name="service" class="form-control" required style="font-weight: bold;">
                <option value="" style="font-weight: bold;" >Select your Preffered Course</option>
                <option v-for="course in courses" :key="course.id" :value="course.name">
              {{ course.name }}
            </option>
            </select><br>
            
            <button type="submit" class="btn btn-primary" style="margin-top: 10px; width: 100%; background-color: rgb(3, 3, 137); color: white;">Register Now</button>
            <h7 style="margin-top: 20px; display: block; text-align: center;">Already have an ID?</h7>
            <a type="button" href="/Partner_login" class="btn btn-primary" style="margin-top: 10px; width: 100%; background-color: rgb(3, 3, 137); color: white;">Login</a>
        </form>
    </div>
      
    </div>
  </div>
</div>
<img :src="require('@/assets/15.png')" style="height: 600px; width: 500px;  margin-left: auto; margin-right: 60px; display: block; margin-top: 50px;"  >
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
                const responses =await axios.get('http://localhost:5000/courses');
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

            const response = await axios.post('http://localhost:5000/SignUp', payload);
  
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