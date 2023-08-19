<template>
  <ProposalMain></ProposalMain>
  <UButton lable="Toggle" @click="toggle" size="xl" />
  <USlideover v-model="isOpen">
    <!-- Content -->
  </USlideover>
  <section class="container mx-auto">
    <div class="">
      <ProposalTable></ProposalTable>
    </div>
  </section>
</template>

<script setup>
const isOpen = ref(false);
let toggle = () => {
  isOpen.value = !isOpen.value;
};
let x = [1, 2, 3, 4, 5, 6];
async function get_articles() {
  let { data } = await useAsyncData("home", () => {
    queryContent("/articles").findOne();
  });
  console.log(data);
}
</script>

<style></style>
