<template>
  <li class="border-t border-gray-200">
    <inertia-link
      :href="`/problems/${problem.id}`"
      class="block transition duration-150 ease-in-out hover:bg-gray-50 focus:outline-none focus:bg-gray-50"
    >
      <div class="flex items-center px-4 py-4 sm:px-6">
        <div class="flex-1 min-w-0 sm:flex sm:items-center sm:justify-between">
          <div>
            <div class="text-sm font-medium leading-5 text-indigo-600 truncate">
              {{ problem.title }}
              <!-- <span class="ml-1 font-normal text-gray-500">
                    in Engineering
                  </span> -->
            </div>
            <div class="flex mt-2">
              <div class="sm:flex">
                <div
                  class="flex items-center mr-6 text-sm leading-5 text-gray-500"
                >
                  <svg
                    class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"
                    />
                  </svg>
                  Engineering
                </div>
                <div
                  class="flex items-center mt-2 text-sm leading-5 text-gray-500 sm:mt-0"
                >
                  <svg
                    class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  Remote
                </div>
              </div>
            </div>
          </div>
          <div class="flex-shrink-0 mt-4 sm:mt-0">
            <div
              class="flex items-center mt-2 text-sm leading-5 text-gray-500 sm:mt-0"
            >
              <svg
                class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
                  clip-rule="evenodd"
                />
              </svg>
              <span>
                Closing on
                <time datetime="2020-01-07">January 7, 2020</time>
              </span>
            </div>
          </div>
        </div>
        <div class="flex-shrink-0 ml-5">
          <svg
            class="w-5 h-5 text-gray-400"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
              clip-rule="evenodd"
            />
          </svg>
        </div>
      </div>
    </inertia-link>
  </li>
</template>

<script>
export default {
  props: {
    problem: {
      type: Object,
      default: () => {},
    },
  },
};
</script>

<style></style>
