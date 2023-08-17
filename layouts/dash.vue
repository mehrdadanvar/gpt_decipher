<template>
  <div class="dash flex flex-row mt-6 mb-6">
    <DashSidebar />
    <div class="w-full -mt-3">
      <slot />
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.dash {
  background-image: url("/dash6.png");
}
</style>
