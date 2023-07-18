<template>
  <aside
    class="bg-gradient-to-r from-slate-950 from-10% via-slate-800 via-85% to-slate-700 to-99% text-white rounded-tr-xl rounded-br-lg font-body h-screen overflow-hidden transition-all duration-500 border border-violet-500"
    :class="{ 'w-8': !isopen, 'w-1/6': isopen }"
  >
    <div>
      <div @click="toggle_button" class="text-white">
        <UButton icon="i-solar-map-arrow-right-bold-duotone" color="purple" size="sm"></UButton>
      </div>
      <div class="flex flex-row items-center">
        <UAvatar src="https://avatars.githubusercontent.com/u/739984?v=4" size="xl" />
        <div class="flex flex-col"></div>
      </div>
      <hr />
    </div>
    <div>
      <NuxtLink to="/About">About Page</NuxtLink>
    </div>
    <div class="flex flex-row gap-6">
      <NuxtLink to="/about">about</NuxtLink>
    </div>
    <div class="border border-slate-600 rounded-lg mt-6 px-2 py-2">
      <NuxtLink to="/">Applicants</NuxtLink>
    </div>
    <div class="border border-slate-600 rounded-lg mt-6 px-2 py-2 duration-200 hover:translate-x-3">
      <span>Colleges</span>
    </div>
    <div class="border border-slate-600 rounded-lg mt-6 px-2 py-2 duration-200 hover:translate-x-3">
      <span>Inbox</span>
    </div>
    <div class="mt-6 px-2 py-2 bg-slate-700 rounded-lg">
      <span>Cases</span>
    </div>
    <div class="mt-6 px-2 py-2 bg-slate-700 rounded-lg">
      <span> Profile</span>
    </div>
  </aside>
</template>

<script setup>
let isopen = ref(false);
function toggle_button() {
  isopen.value = !isopen.value;
}
let mehrdad = { sample: {} };
</script>

<style scoped></style>
