<template>
  <section class="container mx-auto w-7/12">
    <table class="table-auto">
      <thead class="border border-green-100">
        <tr class="border border-red-400">
          <th>Specialities</th>
          <th v-for="x in items" :key="x" class="text-slate-700 px-2">
            {{ x }}
          </th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="item in specials" :key="item" class="border border-b-slate-300">
          <td class="px-4 py-1">{{ item }}</td>
          <td>x</td>
          <td>x</td>
          <td>x</td>
          <td class="">x</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup>
let items = [
  "Junior Medical Student",
  "Senior Medical Student",
  "Medical resident",
  "Attending Physician",
];
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
];
</script>

<style lang="scss" scoped></style>
