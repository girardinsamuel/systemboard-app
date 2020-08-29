<template>
  <nav class="flex-shrink-0 bg-gray-800">
    <div class="px-2 mx-auto max-w-7xl sm:px-4 lg:px-8">
      <div class="relative flex items-center justify-between h-12">
        <button
          @click="showProblemsList"
          class="inline-flex items-center justify-center p-2 text-gray-400 transition duration-150 ease-in-out rounded-md hover:text-white hover:bg-gray-600 focus:outline-none focus:bg-gray-600 focus:text-white"
          aria-label="Main menu"
          aria-expanded="false"
        >
          <svg
            class="block w-6 h-6"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </button>
        <p class="flex-grow text-center text-white">
          {{ problem.title }}
          <span class="text-gray-400">{{ problem.grade }}</span>
        </p>
        <button
          @click="showProblemDetails"
          class="inline-flex items-center justify-center p-2 text-gray-400 transition duration-150 ease-in-out rounded-md hover:text-white hover:bg-gray-600 focus:outline-none focus:bg-gray-600 focus:text-white"
          aria-label="Main menu"
          aria-expanded="false"
        >
          <svg
            class="block w-6 h-6"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "ProblemHeader",
  props: {
    problem: {
      type: Object,
      default: () => {},
    },
  },
  methods: {
    showProblemsList() {
      this.$inertia.visit("/problems", { method: "get" });
    },
    showProblemDetails() {
      this.$inertia.visit(`/problems/${this.problem.id}/details`);
    },
  },
};
</script>

<style></style>
