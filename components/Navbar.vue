<template>
  <nav class="flex flex-row gap-24 text-slate-600 text-lg bg-gray-800 mb-6 items-center">
    <NuxtLink to="/"><img src="/tri2.svg" alt="" width="70" class="" /></NuxtLink>
    <NuxtLink to="/proposal">Proposal</NuxtLink>
    <NuxtLink to="/Dashboard/Index">Dashboard</NuxtLink>
    <div class="flex flex-row gap-6">
      <NuxtLink to="/register"
        ><UButton class="bg-teal-500 text-white" color="teal">Create Account</UButton>
      </NuxtLink>
      <NuxtLink to="/login"
        ><UButton class="bg-teal-500 text-white rounded-full p-1">Login</UButton></NuxtLink
      >
    </div>
  </nav>
</template>

<script setup></script>

<style lang="scss" scoped></style>
