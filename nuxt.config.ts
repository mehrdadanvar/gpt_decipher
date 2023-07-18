// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  //css: ["@/assets/css/main.css"],
  modules: ["@nuxthq/ui"],
  // content: {
  //   highlight: {
  //     theme: "dracula-soft",
  //   },
  // https://content.nuxtjs.org/api/configuration
  //},
  ui: { icons: ["solar"] },
  ssr: false,
});
