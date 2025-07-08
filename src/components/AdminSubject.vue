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

        <div class="card" style="border-radius: 10px; width: 350px; height: 400px; background-color: #dfe6e9; border-radius: 10px; margin-top: 20px;">
       <div class="card-body">
          <h5 class="card-title">Subjects</h5>
          <div class="dropdown" >
           <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="background-color: white; color: black; border-radius: 10px;">
          Choose Courses
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

        <div class="card" style="border-radius: 10px; width: 350px; height: 400px; background-color: #dfe6e9; margin-top: 20px;">
       <div class="card-body">
          <h5 class="card-title">Quizes</h5>
          <div class="dropdown" >
           <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="background-color: white; color: black; border-radius: 10px;">
          Choose Courses
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
