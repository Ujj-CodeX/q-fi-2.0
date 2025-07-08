<template>

    <div style="display: flex; align-items: flex-start; gap: 300px; margin-top: 50px;">
   
    
      <h5 style="color: black; font-weight: bold; margin-left: 300px;">Quiz Name:-</h5>
      <h5 style="color: black; font-weight: bold; margin-left: 20px;">No. of Question:-</h5>
      <h5 style="color: black; font-weight: bold; margin-left: 20px;">Duration:-</h5>
      
    
    </div>

    <div style="display: flex; align-items: flex-start; gap: 20px; margin-top: 50px;">

    <div class="card inset-card p-4 text-center" style="width: 1000px; height: 500px; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
    <div style="display: flex; align-items: flex-start; gap: 300px; margin-top: 350px;">
        <button class="btn btn-primary"  style=" margin-left: 50px; margin-top: 50px; border-radius: 20px; background-color: green">Previous</button>

        <button class="btn btn-primary"  style="  margin-top: 50px; border-radius: 20px; background-color: green">Submit</button>

        <button class="btn btn-primary"  style=" margin-top: 50px; border-radius: 20px; background-color: green">Next</button>
    </div>



    </div>
    <div class="card inset-card p-4 text-center" style="width: 400px; height: 250px; margin-left: 50px; margin-top: 50px; border-radius: 10px;">
        <div class="timer">Time Left: </div>

    </div>




    </div>




</template>
<script>
</script>
<style scoped>
.timer {
  font-size: 1.5rem;
  font-weight: bold;
  color: #d9534f;  /* Red color for urgency */
  margin-bottom: 20px;
}
</style>