<template>
  <main class="flex flex-col min-h-screen bg-white">
    <ProblemHeader :problem="problem" />
    <slot />
    <ProblemFooter :problem="problem" />
  </main>
</template>

<script>
import ProblemHeader from "../components/headers/ProblemHeader.vue";
import ProblemFooter from "../components/headers/ProblemFooter.vue";

export default {
  components: {
    ProblemHeader,
    ProblemFooter,
  },
  // props: {
  //   title: String,
  //   problem: Object,
  // },
  data() {
    return {
      title: "",
      problem: null,
    };
  },
  watch: {
    title: {
      immediate: true,
      handler(title) {
        document.title = title;
      },
    },
  },
  created() {
    this.title = this.$page.title;
    this.problem = this.$page.problem;
  },
};
</script>
