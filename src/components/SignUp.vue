<template>
<div style="display: flex; align-items: flex-start; " >
    
    <div class="card inset-card p-4 text-center" style="width: 800px;  margin-top: 50px; margin-bottom: 50px; border-radius: 15px; margin-left: 100px;">
  <div class="row g-0">
    
    <div class="col-md-10">
      <div class="card-body" style="margin-left: 100px;">

        <form action="{{ url_for('Reg_partner') }}" method="post">
            <h4 style="color: black; text-align: center;">Registration</h4>
            <br>
            <div style="display: flex; flex-direction: row; gap: 5px;">
            
            <input type="text" class="form-control" id="username" placeholder="Username" style="font-weight: bold;" name="username"><br>
            <input type="password" class="form-control" id="password" placeholder="Password" style="font-weight: bold;" name="password"><br>
            </div><br>

            <div style="display: flex; flex-direction: row; gap: 5px;">
            
            <input type="text" class="form-control" id="fullname" placeholder="Full Name" style="font-weight: bold;" name="name"><br>
            
            
            </div><br>

            <div style="display: flex; flex-direction: row; gap: 5px;">
            <div class="col-auto">
                <select id="gender" name="gender" class="form-control" style="width: 100%; font-weight: bold;" >
                    <option value="Choose Your Gender" >Choose your Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>
            </div><br>
            <input type="date" class="form-control" id="dob" placeholder="Date of Birth" style="font-weight: bold;" name="dob"><br>

            </div><br>
            
            <input type="email" class="form-control" id="email" placeholder="Email ID" style="font-weight: bold;" name="email"><br>

            <select id="services" name="service" class="form-control" required style="font-weight: bold;">
                <option value="" style="font-weight: bold;" >Select your Preffered Course</option>
                {% for service_item in service %}
                    <option value="{{ service_item }}">{{ service_item }}</option>
                {% endfor %}
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
<script setup>
</script>

<style>
</style>