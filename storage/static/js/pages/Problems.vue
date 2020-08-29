<template>
  <div class="overflow-hidden bg-white shadow sm:rounded-md">
    <ul v-for="problem in problems" v-if="problems.length > 0">
      <ProblemItem :problem="problem" :key="problem.id" />
    </ul>
    <p v-else>0 problems :(</p>
  </div>
</template>

<script>
import ProblemItem from "../components/ProblemItem.vue";
import BaseLayout from "../layouts/BaseLayout.vue";

export default {
  name: "Problems",
  layout: BaseLayout,
  components: {
    ProblemItem,
  },
  props: {
    problems: {
      type: Array,
      default: () => [],
    },
  },
};
</script>
