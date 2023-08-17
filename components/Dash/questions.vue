<template>
  <section class="container mx-auto">
    <h2>1500 Collection</h2>
    <div>
      <UButton @click="fetch_questions">Load</UButton>
    </div>
    <div class="grid grid-cols-1 gap-2">
      <div
        v-for="question in questions"
        :key="question.id"
        class="border border-amber-600 rounded-xl p-4 shadow-md bg-slate-100"
      >
        <div class="">
          <p class="text-white text-3xl bg-teal-700 rounded-lg pl-2 mb-4">
            {{ question.id + 1 }}
          </p>
          <p class="text-slate-700 text-lg pl-4 mb-4 text-justify">
            {{ question.title }} ?
          </p>
          <div class="grid grid-cols-1 text-slate-600 bg-white rounded-lg p-4">
            <span v-for="item in question.options" class="text-teal-900">{{
              item
            }}</span>
          </div>
          <!-- <URadio v-for="method of methods" :key="method.name" v-model="selected" v-bind="method" /> -->
          <div class="flex flex-row max-w-md">
            <UButton class="mt-5 mx-auto" color="teal">check answer</UButton>
            <UButton class="mt-5 mx-auto" color="teal">Ask GPT</UButton>
          </div>
        </div>
      </div>
    </div>
    <button @contextmenu="bye">get</button>
  </section>
</template>

<script setup>
let questions = ref([]);
let options_list = ref([]);
async function fetch_questions() {
  try {
    let response = await $fetch("http://localhost:8000/collections");
    console.log(response.documents);
    questions.value = response.documents;
    // console.log(questions.value);
  } catch (error) {
    error ? console.log(error) : "";
  }
}
async function bye() {}
</script>

<style scoped></style>
