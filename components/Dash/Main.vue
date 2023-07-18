<template>
  <section class="flex flex-row">
    <DashSidebar />
    <div>
      <UButton label="Open" @click="profiledata.is_open = true" />
      <USlideover v-model="profiledata.is_open">
        <div class="border border-slate-500 h-full p-1">
          <h2>Profile</h2>
          <UAvatar />
          <div>hi {{ user }}</div>
        </div>
      </USlideover>
      <section class="">
        <div class="ml-80">
          <p>createing a patient is easy peasy</p>
        </div>
      </section>
      <section class="container">
        <div class="mx-80 border border-salte-500">
          <table class="table-auto">
            <thead class="">
              <tr class="bg-slate-100 border border-b-teal-500">
                <th>ID</th>
                <th>Name</th>
                <th>Last Name</th>
                <th>Gender</th>
                <th>Age</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="x in cases" class="bg-slate-200">
                <td>{{ x.identifier }}</td>
                <td>{{ x.firstname }}</td>
                <td>{{ x.lastname }}</td>
                <td>{{ x.gender }}</td>
                <td>{{ x.age }}</td>
              </tr>
            </tbody>
            <tfoot>
              footer
            </tfoot>
          </table>
        </div>
      </section>
    </div>
  </section>
</template>

<script setup>
let question = ref("");
let mehrdad = ref("");
let cases = ref("");
let load_locall = async () => {
  let retrieved = localStorage.getItem("patients");
  if (retrieved != null) {
    cases.value = JSON.parse(retrieved);
    console.log(cases);
  } else {
    console.log("nothing found");
  }
};

load_locall();
let profiledata = ref({
  is_open: false,
});

let user = ref({});

async function load_profile() {
  let x = { name: "mehrdad", lasname: "anvar" };
  user.value = x;
}
load_profile();
</script>

<style scoped></style>
