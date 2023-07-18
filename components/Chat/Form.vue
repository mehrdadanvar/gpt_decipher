<template>
  <div>
    <div>
      <UButton label="Open" @click="modal_isOpen = true" color="purple">Create Patient</UButton>

      <USlideover v-model="modal_isOpen" side="left" :overlay="true" class="p-12 overflow-auto">
        <p>Create Patient</p>
        <hr />
        <form class="mt-12 bg-slate-100 rounded-xl">
          <div class="flex flex-col gap-y-9 mx-2 px-1">
            <div>
              <UInput
                size="md"
                name="identifier"
                placeholder="Identifier"
                type="text"
                color="purple"
                icon="i-solar-user-id-bold-duotone"
                class="bg-white"
                v-model="identifier"
              />
            </div>
            <div class="flex flex-row justify-center gap-x-3 mt-6">
              <UInput
                size="md"
                name="firstname"
                placeholder="First Name"
                type="text"
                color="purple"
                icon="i-solar-user-circle-bold-duotone"
                class="bg-slate-300"
                v-model="firstname"
              />
              <UInput
                size="md"
                name="lastname"
                placeholder="Last Name"
                type="text"
                color="purple"
                icon="i-solar-user-circle-bold-duotone"
                class="bg-white"
                v-model="lastname"
              />
            </div>

            <div class="age-gender flex flex-row gap-6">
              <UInput type="number" placeholder="Age should be a numer" color="purple" v-model="age" />
              <div class="gender">
                <span class="text-slate-600">Gender</span>
                <URadio
                  v-for="method in gender_methods"
                  :key="method.name"
                  v-model="gender_selected"
                  v-bind="method"
                  color="purple"
                  class="flex flex-row"
                />
              </div>
            </div>
            <div class="center">
              <div class="flex flex-row justify-center gap-x-3">
                <UInput
                  size="md"
                  name="facility"
                  placeholder="Visit Facility"
                  type="text"
                  color="purple"
                  icon="i-solar-hospital-bold-duotone"
                  class="bg-white"
                />
                <UInput
                  size="md"
                  name="department"
                  placeholder="Visit Department"
                  type="text"
                  color="purple"
                  icon="i-solar-clipboard-text-line-duotone"
                  class="bg-white"
                />
              </div>
            </div>
            <hr />
            <div class="complaint">
              <div>
                <UInput type="text" placehoder="chief" color="blue" />
              </div>
              <div v-for="complaint in complaints" :key="complaint.id">
                <UInput :placeholder="complaint.title" />
              </div>
              <UButton icon="i-solar-add-folder-bold-duotone" color="purple" @click="add_complaint">add</UButton>
              <UButton icon="i-solar-add-folder-bold-duotone" color="purple" @click="add_complaint">remove</UButton>
            </div>
            <div class="history"></div>
            <div class="physical"></div>
            <div class="lab"></div>
            <div class="imaging"></div>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <UButton class="bg-purple-800 hover:bg-white hover:text-slate-600" @click="save_patient" size="lg">Save Locally</UButton>
            <UButton class="bg-purple-800 hover:bg-white hover:text-slate-600" @click="" icon="i-solar-cloud-plus-line-duotone" size="lg">
              Save to Cloud
            </UButton>
            <UButton
              class="bg-purple-800 hover:bg-white hover:text-slate-600"
              icon="i-solar-trash-bin-trash-bold-duotone"
              @click=""
              size="lg"
            >
              Empty Local Storage</UButton
            >
          </div>
        </form>
      </USlideover>
    </div>
  </div>
</template>

<script setup>
let modal_isOpen = ref(false);
//////////////firstname and lastname/////////////
let identifier = Math.random().toLocaleString();
let firstname = ref("");
let lastname = ref("");
/////////////////////age and gender///////////////
let age = ref("15");

let gender_methods = [
  { name: "male", value: "male", label: "Male" },
  { name: "female", value: "female", label: "Female" },
];
let gender_selected = ref("male");
///////////////////complaint/////////////////
let complaints = ref([{ id: 1, title: "cheif" }]);
function add_complaint() {
  console.log("added");
  complaints.value.push({ id: 2, title: "hi" });
}

function delete_complaint(complaint) {}
function save_patient() {
  console.log("ran");
  let single_patient = {
    identifier: identifier,
    firstname: firstname.value,
    lastname: lastname.value,
    gender: gender_selected.value,
    age: age.value,
  };
  if (localStorage.getItem("patients") != null) {
    console.log("part1");
    let patients = JSON.parse(localStorage.getItem("patients"));
    console.log(patients);
    patients.push(single_patient);
    console.log(patients);
    localStorage.setItem("patients", JSON.stringify(patients));
  } else {
    console.log("nothing found saving first patient");
    let patients = JSON.stringify([single_patient]);
    localStorage.setItem("patients", patients);
  }
}
</script>

<style lang="scss" scoped></style>
