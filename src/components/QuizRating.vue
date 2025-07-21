<template>

    <div class="card inset-card p-4 text-center" style="  width: 1200px; height: 600px;margin-left: 100px;  border-radius: 10px;">

<h3 style="text-align: center;">Rate the </h3>

<div>
      <span
        v-for="star in 5"
        :key="star"
        @click="setRating(star)"
        @mouseover="hover = star"
        @mouseleave="hover = 0"
        style="font-size: 2rem; cursor: pointer; color: gold;"
      >
        {{ star <= (hover || rating) ? '★' : '☆' }}
      </span>
    </div>
</div>

</template>
<script>
</script>