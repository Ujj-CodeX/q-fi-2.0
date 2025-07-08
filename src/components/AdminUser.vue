<template>
  <div style="display: flex; align-items: flex-start;">
   
    <div class="sidebar-card">
      <h5 style="color: white; margin-left: 20px;">Admin Management</h5>
      <hr>
    </div>

    
    <div style="flex: 1; padding: 20px;">
      <h2 style="font-weight: bold; margin-top: 20px; margin-left: 400px;">User Management and Overview</h2>

     
      <div style="display: flex; gap: 40px; margin-top: 50px;">
        <div class="card inset-card p-4 text-center" style="flex: 2; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quiz Name vs No of User attempts</h6>
        </div>
        <div class="card inset-card p-4 text-center" style="flex: 1; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quiz Name and No of attempts</h6>
        </div>
      </div>

      
      <div style="display: flex; gap: 40px; margin-top: 50px;">
        <div class="card inset-card p-4 text-center" style="flex: 1.5; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">User Review and Rating</h6>
        </div>
        <div class="card inset-card p-4 text-center" style="flex: 1; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">User Details</h6>
        </div>
      </div>

     
      <div style="display: flex; gap: 40px; margin-top: 50px;">
        <div class="card inset-card p-4 text-center" style="flex: 2; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quizzes vs Ratings</h6>
        </div>
        <div class="card inset-card p-4 text-center" style="flex: 1; height: 500px; border-radius: 10px;">
          <h6 style="font-weight: bold; margin-top: 10px;">Quiz Name and No of attempts</h6>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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
