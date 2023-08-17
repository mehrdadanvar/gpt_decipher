<template>
  <div>
    {{ id }}
  </div>
</template>

<script setup>
let route = useRoute();
let id = route.params;
</script>

<style lang="scss" scoped></style>
