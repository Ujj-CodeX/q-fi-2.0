<template>
  
  

    <div class="heading" style="margin-left: 200px; margin-top:110px; color: black;">
      <h1 style="font-weight: bold;">Q-Fi</h1>
      <h5 style="font-weight: bold;">Challenge yourself and ace your grade</h5>
    </div>

    <div style="display: flex; align-items: flex-start; gap: 120px; margin-top: 0px;">
      <div class="card" style="height: 350px; width: 330px; margin-left: 200px; margin-top: 50px; border-radius: 10px;">
        <form @submit.prevent="handleSubmit">
          <div class="mb-3" style="width: 290px; margin-left: 20px; margin-top: 20px;">
            <label for="username" class="form-label" style="color: black; font-weight: bold;">Username</label>
            <input type="text" class="form-control" id="username" v-model="username" placeholder="Username">

            <label for="password" class="form-label" style="color: black; font-weight: bold; margin-top: 10px;">Password</label>
            <input type="password" class="form-control" id="password" v-model="password" placeholder="Password">

            <button type="submit" class="btn btn-primary" style="margin-top: 20px; width: 290px; background-color: blue; color: white;">Sign In</button>
            <a href="/forgot_user" style=" font-weight: bold; display: block; text-decoration: underline; color:black; margin-top: 15px;">Forgot Password?</a>

            <div v-if="errorMessage" class="alert alert-danger mt-3">
              {{ errorMessage }}
            </div>
          </div>
        </form>
      </div>

      <div class="illustrative">
        <img :src="require('@/assets/1.png')" style="height: 400px;  margin-left: 200px;">
      </div>
    
</div>
    <div class="heading" style="margin-left: 200px; margin-top:100px; color: black; " >
      <h5 style="font-weight: bold;">Choose your subject & courses</h5>
      <div class="mb-3 d-flex">
        <select class="form-select" v-model="selectedCourse" style="width: 250px; height: 30px; border-radius: 8px;">
          <option selected disabled>Select Courses</option>
          <option>Lucknow</option>
          <option>Gorakhpur</option>
          <option>Varanasi</option>
          <option>Prayagraj</option>
          <option>Delhi</option>
          <option>Harayana</option>
        </select>

        <select class="form-select" v-model="selectedSubject" style="margin-left: 20px; height: 30px; border-radius: 8px;">
          <option selected disabled>Choose Subject</option>
          <option>Plumbing</option>
          <option>Cleaning</option>
          <option>Electrical</option>
        </select>

        <button type="button" class="btn btn-primary" style="margin-left: 20px; border-radius: 8px; width: 100px; background-color: blue; color: white;" @click="handleBookNow">Start Quiz</button>
      </div>
    </div>

    <div>
      <h3 style="color:black; margin-top: 100px; margin-left: 200px; font-weight: bold;"> Key Features</h3>

    <div class="minicards" style="display: flex; align-items: flex-start; gap: 10px; margin-left: 100px; ">

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/2.jpg')" class="card-img service-img" style="width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 90px; font-weight: bold; font-size: larger; margin-top: 50px;" >Track your Progress</h7>
            </div>

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/3.jpg')" class="card-img service-img" style="width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 70px; margin-top: 50px; font-weight: bold; font-size: larger;" >Syllabus based Quizes</h7>
                
            </div>

            <div class="card" style="height: 400px; width: 350px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/4.png')" class="card-img service-img" style="width: 300px; height: 250px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 100px; margin-top: 50px; font-weight: bold; font-size: larger;" >Multiple Courses</h7>
            </div>
        </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  
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
</style>
