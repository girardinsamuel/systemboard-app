<template>
  <div
    class="flex-grow w-full h-full m-auto overflow-auto text-center text-white bg-black"
  >
    <p class="mt-32">{{ swiped }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      swiped: "Swipe me",
    };
  },
  mounted() {
    document.addEventListener("swiped-right", (e) => {
      this.swiped = "Right !";
    });
    document.addEventListener("swiped-left", (e) => {
      this.swiped = "Left !";
    });
  },
};
</script>

<style></style>
