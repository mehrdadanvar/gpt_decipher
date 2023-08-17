let loggedin = true;
export default defineNuxtRouteMiddleware((to, from) => {
  console.log(to, from);

  if (!loggedin) {
    return navigateTo("/register");
  }
});
