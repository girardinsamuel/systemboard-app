<template>
  <nav class="bottom-0 flex-shrink-0 bg-gray-800">
    <div class="px-2 mx-auto max-w-7xl sm:px-4 lg:px-8">
      <div class="relative flex items-center justify-around h-12">
        <button
          class="p-1 border-2 border-transparent rounded-full transition duration-150 ease-in-out focus:outline-none "
          :class="isLit ? 'text-yellow-500  bg-gray-100' : 'text-gray-400'"
          @click="toggleLight"
        >
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24">
            <path
              fill="currentColor"
              d="M20,11H23V13H20V11M1,11H4V13H1V11M13,1V4H11V1H13M4.92,3.5L7.05,5.64L5.63,7.05L3.5,4.93L4.92,3.5M16.95,5.63L19.07,3.5L20.5,4.93L18.37,7.05L16.95,5.63M12,6A6,6 0 0,1 18,12C18,14.22 16.79,16.16 15,17.2V19A1,1 0 0,1 14,20H10A1,1 0 0,1 9,19V17.2C7.21,16.16 6,14.22 6,12A6,6 0 0,1 12,6M14,21V22A1,1 0 0,1 13,23H11A1,1 0 0,1 10,22V21H14M11,18H13V15.87C14.73,15.43 16,13.86 16,12A4,4 0 0,0 12,8A4,4 0 0,0 8,12C8,13.86 9.27,15.43 11,15.87V18Z"
            />
          </svg>
        </button>

        <button
          class="p-1 border-2 border-transparent rounded-full transition duration-150 ease-in-out focus:outline-none "
          :class="isLiked ? 'text-red-500  bg-gray-100' : 'text-gray-400'"
        >
          <svg
            class="w-6 h-6"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
            />
          </svg>
        </button>
        <button
          class="p-1 text-gray-400 border-2 border-transparent rounded-full transition duration-150 ease-in-out hover:text-gray-300 focus:outline-none focus:text-gray-500 focus:bg-gray-100"
        >
          <svg
            class="w-6 h-6"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M5 13l4 4L19 7"
            />
          </svg>
        </button>
        <button
          class="p-1 text-gray-400 border-2 border-transparent rounded-full transition duration-150 ease-in-out hover:text-gray-300 focus:outline-none focus:text-gray-500 focus:bg-gray-100"
        >
          <svg
            class="w-6 h-6"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </button>
        <button
          class="p-1 text-gray-400 border-2 border-transparent rounded-full transition duration-150 ease-in-out hover:text-gray-300 focus:outline-none focus:text-gray-500 focus:bg-gray-100"
        >
          <svg
            class="w-6 h-6"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"
            />
          </svg>
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  props: {
    problem: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      isLit: false,
      isLiked: false,
    };
  },
  methods: {
    toggleLight() {
      this.isLit = !this.isLit;
      console.log(`light ${this.problem.title} ${this.isLit ? "on" : "off"}`);
      this.$inertia.post(`/problems/${this.problem.id}/light`)
    },
  },
};
</script>

<style></style>
