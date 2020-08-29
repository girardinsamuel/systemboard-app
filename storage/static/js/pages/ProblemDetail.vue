<template>
  <main class="flex flex-col min-h-screen bg-white">
    <nav class="flex-shrink-0 bg-gray-800">
      <div class="px-2 mx-auto max-w-7xl sm:px-4 lg:px-8">
        <div class="relative flex items-center justify-between h-12">
          <button
            @click="back"
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
            {{ details.title }}
            <span class="text-gray-400">{{ details.grade }}</span>
          </p>
        </div>
      </div>
    </nav>
    <p>Setter: {{ details.setter }}</p>
  </main>
</template>

<script>
export default {
  name: "ProblemDetail",
  props: {
    details: {
      type: Object,
      default: () => {},
    },
  },
  methods: {
    back() {
      this.$inertia.replace(`/problems/${this.details.id}`, { method: "get" });
    },
  },
};
</script>
