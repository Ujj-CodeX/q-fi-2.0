/* eslint-disable vue/multi-word-component-names */

<template>
  <nav class="navbar navbar-expand-lg navbar-dark mt-4"
    style="background-color: rgba(0, 0, 0, 0.2); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); margin: 20px auto; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    
    <div class="container-fluid px-4">
      <!-- Logo + Brand -->
      <div class="d-flex align-items-center gap-2">
        <img :src="require('@/assets/91.png')" alt="Logo" width="40" height="40" class="d-inline-block align-text-top" style="margin-left: 80px;">
        <span class="navbar-brand mb-0 h1 text-white fs-3 fw-bold">Q_Fi</span>
      </div>

      <!-- Toggle button -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent"
        aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Centered links -->
      <div class="collapse navbar-collapse justify-content-center" id="navbarContent">
        <ul class="navbar-nav text-center d-flex flex-column flex-lg-row gap-2 gap-lg-4 mt-3 mt-lg-0">
          <li class="nav-item">
            <router-link class="nav-link text-light" to="/About">About Us</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-light" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-light" to="/SignUp">Sign Up</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-light" to="/admin">Admin</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link text-light" v-if="auth.isLoggedIn" @click="logout" style="cursor: pointer;">User Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { auth } from '../store';
import { useRouter } from 'vue-router';

const router = useRouter();

function logout() {
  localStorage.removeItem('token');
  auth.isLoggedIn = false;
  router.push('/');
}
</script>
