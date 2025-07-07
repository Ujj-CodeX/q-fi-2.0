<template>
    <h2 style="font-weight: bold; margin-left: 670px; margin-top: 50px;">Quiz Management</h2>
    <div class="card inset-card p-4 text-center" style="width: 1300px; height: 500px; margin-left: 160px; margin-top: 110px; border-radius: 10px;">
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


</style>
