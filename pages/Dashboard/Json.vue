<template>
  <DashContent>
    <div class="bg-gray-50 p-6 m-6">
      <p>Type your Question</p>
      <UIcon name="i-solar-question-square-bold-duotone" class="text-2xl text-teal-400" />
      <UTextarea
        v-model="query"
        color="teal"
        placeholder="Hey chat give me a json object representing a patient with acute appendicitis"
        class="px-4 py-3 text-teal-900"
      />

      <UButton
        class="mt-6"
        @click="call_fastapi_backend"
        color="emerald"
        icon="i-solar-map-arrow-square-line-duotone"
        :loading="loading_slate"
        >Ask Chat callGpt</UButton
      >

      <div>{{ gpt_response }}</div>
      <div></div>
    </div>
  </DashContent>
</template>

<script setup>
definePageMeta({
  layout: "dash",
});
let gpt_response = ref("");
async function callGpt() {
  let response = await $fetch("http://localhost:3000/api/gpt");
  console.log(response);
}
let query = ref("");
let loading_slate = ref(false);
async function call_fastapi_backend() {
  try {
    loading_slate.value = true;
    console.log(query.value);
    let response = await fetch("http://localhost:8000/gpt/index", {
      method: "POST",
      body: JSON.stringify({ query: query.value }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    let data = await response.json();
    console.log(data, response);
    gpt_response.value = data.message;
    if (response.status == "200") {
      console.log("returning to normal");
      loading_slate.value = false;
    }
  } catch (error) {
    error ? console.log(error) : "";
  }
}
</script>
