<template>
 <div style="display: flex; align-items: flex-start;">
   
    <div class="sidebar-card">
      <h5 style="color: white; margin-left: 20px;">Admin Management</h5>
      <hr>
    </div>


    <div style="flex: 2; padding: 10px;">


    <h2 style="font-weight: bold; margin-left: 550px; margin-top: 50px;">Quiz Management</h2>
    <h5 style="font-weight: bold; margin-top: 50px; margin-left: 350px;">After Successfully creating a new Quiz click on the button below to send Reminder</h5>
    <a href="#" class="btn btn-primary" style="margin-left: 620px; margin-top: 50px; border-radius: 20px; background-color: red;">Send Reminder</a>
    <div class="card inset-card p-4 text-center" style="width: 1300px; height: 500px; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
    <div style="display: flex; align-items: flex-start; gap: 40px; margin-top: 0px;">
        <div class="dropdown" >
           <button class="btn btn dropdown-toggle shadow" type="button" data-bs-toggle="dropdown" aria-expanded="false" style=" margin-top: 30px; margin-left: 150px; background-color: white; color: black; border-radius: 10px;">
          Choose Courses
           </button>
         </div>

         <div class="dropdown" >
           <button class="btn btn dropdown-toggle shadow" type="button" data-bs-toggle="dropdown" aria-expanded="false" style=" margin-top: 30px; margin-left: 200px; background-color: white; color: black; border-radius: 10px;">
          Choose Subject
           </button>
         </div>


         <div class="dropdown" >
           <button class="btn btn dropdown-toggle shadow" type="button" data-bs-toggle="dropdown" aria-expanded="false" style=" margin-top: 30px; margin-left: 200px; background-color: white; color: black; border-radius: 10px;">
          Choose Quiz
           </button>
         </div>

    </div>
    <div style="display: flex; align-items: flex-start; gap: 200px; ">
    <h4 style="font-weight: bold; margin-left: 500px; margin-top: 60px;">Existing Questions</h4>

    <a href="#" class="btn btn-primary" style="margin-left: 100px; margin-top: 50px; border-radius: 20px; background-color: rgb(3, 3, 137);">Add +</a>
        
   </div>


<div class="card inset-card p-4 text-center" style="width: 1200px; height: 500px; margin-left: 30px; margin-top: 50px; border-radius: 10px;">
</div>
</div>
</div>

</div>
</template>
<script>
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
