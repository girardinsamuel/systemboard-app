<template>
  <Board @swipe-right="next" @swipe-left="previous" :placements="problem.placements" />
</template>

<script>
import ProblemLayout from "../layouts/ProblemLayout.vue";
import Board from "../components/Board.vue";

export default {
  layout: ProblemLayout,
  components: {
    Board,
  },
  props: {
    problem: {
      type: Object,
      default: () => {},
    },
  },
  methods: {
    next() {
      // this.problem.title = "Problem Title Next";
    },
    previous() {
      // this.problem.title = "Problem Title Previous";
    },
  },
};
</script>
