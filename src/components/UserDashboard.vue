<template>

    <div class="heading" style="margin-left: 200px; margin-top:100px; color: black;">
      <h1 style="font-weight: bold;">Q-Fi</h1>
      <h5 style="font-weight: bold;">Looking for something specific ?</h5>
    </div>

    <div style="display: flex; align-items: flex-start; gap: 50px; margin-top: 0px; margin-left: 10px">

    <div style="display: flex; flex-direction: column; align-items: center; gap: 10px; margin-top: 0px; margin-left: 100px">
            <div class="card" style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/2.jpg')" class="card-img service-img" style="width: 100px; height: 100px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 30px; font-weight: bold; font-size: small; margin-top: 20px;" >Leaderboard</h7>
            </div>

            <div class="card" style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/3.jpg')" class="card-img service-img" style="width: 100px; height: 100px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 10px; margin-top: 20px; font-weight: bold; font-size: small;" >Performance Report</h7>
                
            </div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 10px; margin-top: 0px; ">
        

            <div class="card" style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/2.jpg')" class="card-img service-img" style="width: 100px; height: 100px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 30px; font-weight: bold; font-size: small; margin-top: 20px;" >Score Overtime</h7>
            </div>

            <div class="card" style="height: 120px; width: 150px; margin-left: 100px; margin-top: 80px;">
                <img :src="require('@/assets/3.jpg')" class="card-img service-img" style="width: 100px; height: 100px; margin-top: 10px; margin-left: 20px; ">
                <h7 style="margin-left: 30px; margin-top: 20px; font-weight: bold; font-size: small;" >Past attempts</h7>
                
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
       @click="navigateToQuiz(chapter.name)">
      
    <span>{{ chapter.name }}</span>
  </div>
</div>
</div>
    
        <div>
             <h3 style="margin-left: 220px; font-weight: bold; margin-top: 50px;"> Search more Courses</h3>  

        <form class="d-flex" role="search" style="margin-top: 40px; width: 450px; margin-left: 210px;" action="/Show_table" method="post" >
          <input class="form-control mr-2" name="service_name" type="search" placeholder="Enter the Course" aria-label="Search Services by SERVICE ID" style="border-radius: 10px;">
          <button class="button" style="background-color: blue; color: white; border-radius: 8px;" type="submit">Search</button>
        </form>

        </div>


</template>
<script>

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
  background-color:blue;
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