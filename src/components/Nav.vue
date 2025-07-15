/* eslint-disable vue/multi-word-component-names */

<template>
    <nav class="navbar navbar-expand-lg navbar-dark mt-4" style="background-color: rgba(0, 0, 0, 0.2); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); margin: 20px auto; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <div style="display: flex; align-items: flex-start; gap: 400px;">
        <div style=" display: flex; align-items: flex-start; margin-left: 200px; gap: 10px;"> 
        <img src="{{ url_for('static', filename='10.png') }}" alt="Logo" width="40" height="40"  class="d-inline-block align-text-top" style="margin-left: 0px;">
        
        <span style="font-size: 28px; font-weight: bold; color: white;">Q_Fi</span>
        </div>
        <div class="container justify-content-center">
            <ul class="navbar-nav d-flex flex-row gap-3">
                <li class="nav-item">
                    <a class="nav-link text-light" href="/About">About Us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link text-light" href="/">Home</a>
                </li>
                
                <li class="nav-item ">
                    <a class="nav-link text-light" href="/SignUp">Sign Up</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link text-light" href="/admin">Admin</a>
                </li>
            </ul>
            
        </div>
        </div>
    </nav>

</template>
<script>
export default {
    name: "Navbar",
};
</script>