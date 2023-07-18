<template>
  <UContainer>
    <main>
      <div class="register flex flex-row rounded-3xl border border-cyan-500">
        <div>
          <img src="register.jpg" alt="" class="rounded-l-3xl" />
        </div>
        <form class="mx-auto mt-6 flex flex-col items-center" @submit.prevent="chech_empty">
          <h1 class="text-2xl">Welcome to GPT Decipher Project</h1>
          <div class="flex flex-row gap-3 mx-auto mt-6">
            <UInput
              size="xl"
              color="cyan"
              placeholder="Email Address"
              icon="i-solar-letter-broken"
              v-model="login_user.email"
            />
            <UInput
              size="xl"
              color="cyan"
              placeholder="***"
              icon="i-solar-lock-password-bold-duotone"
              v-model="login_user.password"
            />
          </div>
          <div class="mt-12">
            <button class="bg-cyan-400 text-white w-36 h-9 rounded-full" @click="">Sign In</button>
          </div>
        </form>
      </div>
    </main>
  </UContainer>
</template>

<script setup>
let login_user = ref({ email: "", password: "" });
let toast = useToast();
function populate_toast() {
  toast.add({ title: "oops either email or password is blank" });
}
async function chech_empty() {
  let user = login_user.value;
  if ((user.email === "") | (user.password === "")) {
    console.log("either email or password is blank");
  }
}

async function login() {
  try {
    let user = login_user.value;
    console.log(user);
    let response = await $fetch("http://localhost:8000/users/login", {
      method: "POST",
      body: JSON.stringify({ email: user.email, password: user.password }),
    });
    console.log({ email: user.email, password: user.password });
    console.log(response);
  } catch (error) {
    error ? console.log(error) : "";
  }

  let condition = false;
  if (condition) {
  }
}
</script>

<style lang="scss" scoped></style>
