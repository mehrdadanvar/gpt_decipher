<template>
  <div class="register flex flex-row rounded-3xl border border-teal-200 shadow-slate-300 shadow-xl">
    <div>
      <img src="register.jpg" alt="" class="rounded-l-3xl" />
    </div>
    <form @submite.prevent class="mx-auto mt-6 flex flex-col gap-y-16">
      <h1 class="text-2xl text-gray-700">Welcome to GPT Decipher Project</h1>
      <div class="flex flex-col mx-auto gap-y-10">
        <div class="flex flex-row gap-3">
          <UInput
            size="xl"
            color="teal"
            placeholder="First Name"
            icon="i-solar-user-circle-bold-duotone"
            v-model="firstname"
            :required="true"
            trailing
          />
          <UInput
            size="xl"
            color="teal"
            placeholder="Last Name"
            v-model="lastname"
            icon="i-solar-user-circle-bold-duotone"
            trailing
            class="text-slate-600"
          />
        </div>

        <UInput
          size="xl"
          color="teal"
          placeholder="Email Address"
          v-model="email"
          icon="i-solar-letter-broken"
          trailing
        />
        <div class="flex flex-row gap-3">
          <UInput
            size="xl"
            color="teal"
            placeholder="More than 6 chracters"
            type="password"
            v-model="password"
            icon="i-solar-lock-password-bold-duotone"
            trailing
          />
          <UInput
            size="xl"
            color="teal"
            placeholder="Repeat Password"
            icon="i-solar-lock-password-bold-duotone"
            trailing
          />
        </div>
        <USelectMenu
          v-model="speciality"
          :options="specials"
          searchable
          icon="i-solar-buildings-2-bold-duotone"
          size="xl"
          color="teal"
          trailing
        />
      </div>
      <div class="flex flex-col items-center gap-6">
        <UButton size="xl" lable="Create Account" color="teal" variant="solid" @click="createUser"
          >Create Account</UButton
        >

        <NuxtLink to="/login"
          >Already a Member? <span class="text-teal-500 italic">Login</span></NuxtLink
        >
      </div>
    </form>
  </div>
</template>

<script setup>
let firstname = ref("");
let lastname = ref("");
let email = ref("");
let password = ref("");
let specials = [
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
  "Medical Genetics",
  "Nephrology",
  "Neurology",
  "Neurosurgery",
  "Obstetrics and Gynecology",
  "Oncology",
  "Ophthalmology",
  "Orthopedic Surgery",
  "Otolaryngology (ENT)",
  "Pathology",
  "Pediatrics",
  "Physical Medicine and Rehabilitation",
  "Plastic Surgery",
  "Psychiatry",
  "Pulmonology",
  "Radiology",
  "Rheumatology",
  "Thoracic Surgery",
  "Urology",
  "Vascular Surgery",
];
let speciality = ref(specials[4]);
async function createUser() {
  console.log("user data about to be sent");
  console.log(firstname.value, lastname.value, email.value, password.value), speciality.value;
  try {
    let response = await fetch("http://localhost:8000/users", {
      method: "POST",
      body: JSON.stringify({
        firstname: firstname.value,
        lastname: lastname.value,
        email: email.value,
        password: password.value,
        speciality: speciality.value,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}
</script>

<style lang="scss" scoped></style>
