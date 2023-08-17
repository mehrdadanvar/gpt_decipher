<template>
  <aside
    class="bg-gradient-to-r from-teal-950 from-10% via-teal-800 via-85% to-teal-800 text-white rounded-2xl h-screen overflow-hidden transition-all duration-150 border-white"
    :class="{ 'w-16': !isopen, 'w-2/12': isopen }"
  >
    <div>
      <div @click="toggle_button" class="text-white">
        <UButton icon="i-solar-map-arrow-right-bold-duotone" color="purple" size="sm"></UButton>
      </div>
      <div class="flex flex-row items-center">
        <UIcon name="i-solar-user-circle-bold-duotone" size="xl" />
        <div class="flex flex-col"></div>
      </div>
      <hr />
    </div>
    <div class="ml-6 space-y-8">
      <div v-for="item in menuItems" class="">
        <NuxtLink
          :to="item.path"
          class="w-full flex flex-row gap-4 rounded-lg p-2 transition-all duration-150 ease-linear hover:backdrop-brightness-150"
        >
          <UIcon :name="item.iconName" class="text-2xl rotate-90" />
          <p class="text-lg">{{ item.title }}</p>
        </NuxtLink>
      </div>
    </div>
  </aside>
</template>

<script setup>
let current_route = ref("");
let route = useRoute();
let data = route.params;
console.log(data);
let isopen = ref(false);
function toggle_button() {
  isopen.value = !isopen.value;
}
let menuItems = [
  {
    id: "0",
    title: "Dashboard",
    iconName: "i-solar-qr-code-bold-duotone",
    path: "/dashboard/Index",
  },
  {
    id: "1",
    title: "Cases",
    iconName: "i-solar-dna-bold-duotone",
    path: "/dashboard/Cases",
  },
  {
    id: "2",
    title: "Create Code",
    iconName: "i-solar-sidebar-code-bold-duotone",
    path: "/dashboard/Json",
  },
  {
    id: "3",
    title: "Settings",
    iconName: "i-solar-settings-bold-duotone",
    path: "/dashboard/Settings",
  },
  {
    id: "4",
    title: "Log Out",
    iconName: "i-solar-upload-bold-duotone",
    path: "/dashboard/Logout",
  },
];
</script>

<style scoped></style>
