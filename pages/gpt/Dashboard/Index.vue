<template>
  <DashContent>
    <div class="">
      <div class="flex flex-row justify-end gap-6 mt-6 px-6">
        <h2 class="text-2xl text-gray-800">Welcome User</h2>
        <UInput icon="i-solar-minimalistic-magnifer-line-duotone" color="cyan" trailing />
      </div>
      <hr />
      <h2 class="text-3xl text-gray-600">All Specialities</h2>
      <div class="sm:grid sm:grid-cols-1 md:grid md:grid-cols-3 gap-3 mt-6 px-6">
        <div
          v-for="card in cards"
          :key="card.id"
          class="border border-amber-500 rounded-xl p-3 mx-2 bg-white"
        >
          <p class="text-emerald-700 text-2xl my-2">
            <NuxtLink :to="`/majors/${titles[card.id]}`">{{ titles[card.id] }}</NuxtLink>
          </p>
          <div class="lead my-2">
            <p class="text-lg text-gray-700">Lead Investigator</p>
            <div class="flex gap-6">
              <UIcon name="i-solar-user-circle-line-duotone" class="text-3xl text-emerald-500" />

              <p class="text-gray-500 italic">Mr / Ms firstname lastname</p>
              <UButton size="xs" variant="ghost" icon="i-solar-pen-new-round-bold-duotone">Edit</UButton>
            </div>
          </div>
          <hr />
          <div class="residents my-2">
            <p class="text-lg text-gray-700">Assisting Residents</p>
            <ul v-for="item in ['John Hamond', 'Mario Nala', 'Janette Soozana']">
              <li class="ml-2 text-sm text-gray-400">{{ item }}</li>
            </ul>
          </div>
          <hr />
          <p class="mt-2">Description</p>
          <p class="text-gray-500">{{ card.body }}</p>
          <div class="bg-slate-50 rounded-xl p-2">
            <p>Target Cases</p>
            <span>120</span>
            <span
              class="w-20 h-20 rounded-full border border-slate-800 text-lg flex items-center justify-center"
              >6</span
            >
            <p class="text-slate-700">Finished Projects</p>
            <div
              class="w-20 h-20 rounded-full border border-slate-800 text-lg flex items-center justify-center"
            >
              6
            </div>
          </div>
          <div class="flex flex-row gap-6 border border-slate-400 bg-amber-50 rounded-xl p-2 items-center">
            <div class="grid grid-cols-1">
              <p>Cases</p>
              <p class="bg-blue-400 text-cyan-900 rounded-lg p-2 w-auto">120</p>
            </div>
            <div class="grid grid-cols-1">
              <p>Progress</p>
              <div class="flex flex-row">
                <span
                  v-for="(p, index) in ps"
                  :key="p.id"
                  class="w-10 h-3 border border-slate-500 rounded-xl"
                  :class="tones[index]"
                >
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </DashContent>
</template>

<script setup>
definePageMeta({
  layout: "dash",
  middleware: "auth",
});

let cards = [
  {
    id: 0,
    body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam distinctio sint, ratione fuga quam maiores? Accusantium, ducimus. Exercitationem accusamus incidunt aliquam, vero molestias autem praesentium? Facilis eum omnis eligendi voluptatibus in, aspernatur enim, quam provident, tenetur ipsam dolor adipisci quos deserunt itaque accusantium debitis ex natus. Consequatur recusandae odio ea.",
  },
  {
    id: 1,
    body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam distinctio sint, ratione fuga quam maiores? Accusantium, ducimus. Exercitationem accusamus incidunt aliquam, vero molestias autem praesentium? Facilis eum omnis eligendi voluptatibus in, aspernatur enim, quam provident, tenetur ipsam dolor adipisci quos deserunt itaque accusantium debitis ex natus. Consequatur recusandae odio ea.",
  },
  {
    id: 2,
    body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam distinctio sint, ratione fuga quam maiores? Accusantium, ducimus. Exercitationem accusamus incidunt aliquam, vero molestias autem praesentium? Facilis eum omnis eligendi voluptatibus in, aspernatur enim, quam provident, tenetur ipsam dolor adipisci quos deserunt itaque accusantium debitis ex natus. Consequatur recusandae odio ea.",
  },
  {
    id: 3,
    body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam distinctio sint, ratione fuga quam maiores? Accusantium, ducimus. Exercitationem accusamus incidunt aliquam, vero molestias autem praesentium? Facilis eum omnis eligendi voluptatibus in, aspernatur enim, quam provident, tenetur ipsam dolor adipisci quos deserunt itaque accusantium debitis ex natus. Consequatur recusandae odio ea.",
  },
  {
    id: 4,
    body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam distinctio sint, ratione fuga quam maiores? Accusantium, ducimus. Exercitationem accusamus incidunt aliquam, vero molestias autem praesentium? Facilis eum omnis eligendi voluptatibus in, aspernatur enim, quam provident, tenetur ipsam dolor adipisci quos deserunt itaque accusantium debitis ex natus. Consequatur recusandae odio ea.",
  },
  {
    id: 5,
    body: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam distinctio sint, ratione fuga quam maiores? Accusantium, ducimus. Exercitationem accusamus incidunt aliquam, vero molestias autem praesentium? Facilis eum omnis eligendi voluptatibus in, aspernatur enim, quam provident, tenetur ipsam dolor adipisci quos deserunt itaque accusantium debitis ex natus. Consequatur recusandae odio ea.",
  },
];
let titles = [
  "Allergy and Immunology",
  "Anesthesiology",
  "Cardiology",
  "Dermatology",
  "Emergency Medicine",
  "Endocrinology",
  "Family Medicine",
  "Gastroenterology",
  "General Surgery",
  "Geriatrics",
  "Hematology",
  "Infectious Disease",
  "Internal Medicine",
];
let ps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let tones = ["bg-slate-50", "bg-slate-100", "bg-slate-200", "bg-slate-300", "bg-slate-400"];
let icons = ["i-solar-bone-crack-outline", "i-solar-heart-pulse-2-bold"];
</script>

<style scoped></style>
