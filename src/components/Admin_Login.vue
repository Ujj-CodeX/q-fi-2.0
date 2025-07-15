<template>
    <div class="container my-5">
    
    <div class="card inset-card p-4 text-center mx-auto my-card" style="max-height: 100%; width: 100%; border-radius: 25px; background-color:white; overflow: auto;">
            
        
            <div style="display: flex; align-items: flex-start;  gap: 100px;" >
          <img :src="require('@/assets/16.png')" style="height: 350px; width: 350px;  margin-left: 50px;  margin-top:100px;"  >
            
        <div style="width: 1px; height: 400px; background-color: #ccc; margin-top: 100px;"></div>
            <div class="mb-3" style="width: 300px; margin-left: 50px; margin-top: 150px;">




              
                <form action="{{ url_for('admin') }}" method="post">


                
                    
                    
                <h4 style="color: black;  ">Admin Login</h4>
                <br>
                
                
                <input type="username" class="form-control" id="username" placeholder="Username" name="username" style="font-weight: bold;"><br>
                
                
               
                <input type="password" class="form-control" id="Password" placeholder="Password" name="password" style="font-weight: bold;"><br>
                <button type="submit" class="btn btn-primary" style="margin-top: 10px; width: 100px ;  border-radius: 15px; background-color: rgb(3, 3, 137); color: white;" >Log IN</button>
                
                
                </form>
            
            </div>

            
            
            
            </div>
        </div>
</div>
</template>
<style>
.my-card {
  height: 600px; /* default for desktop */
}

@media (max-width: 768px) {
  .my-card {
    height: auto; /* on mobile screens */
  }
}
</style>