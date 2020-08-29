<template>
  <div class="p-8 bg-white">
    <div>
      <nav class="sm:hidden">
        <a
          href="#"
          class="flex items-center text-sm font-medium leading-5 text-gray-500 transition duration-150 ease-in-out hover:text-gray-700"
        >
          <svg
            class="flex-shrink-0 w-5 h-5 mr-1 -ml-1 text-gray-400"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
              clip-rule="evenodd"
            />
          </svg>
          Back
        </a>
      </nav>
      <nav class="items-center hidden text-sm font-medium leading-5 sm:flex">
        <a
          href="#"
          class="text-gray-500 transition duration-150 ease-in-out hover:text-gray-700"
          >Jobs</a
        >
        <svg
          class="flex-shrink-0 w-5 h-5 mx-2 text-gray-400"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
            clip-rule="evenodd"
          />
        </svg>
        <a
          href="#"
          class="text-gray-500 transition duration-150 ease-in-out hover:text-gray-700"
          >Engineering</a
        >
        <svg
          class="flex-shrink-0 w-5 h-5 mx-2 text-gray-400"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
            clip-rule="evenodd"
          />
        </svg>
        <a
          href="#"
          class="text-gray-500 transition duration-150 ease-in-out hover:text-gray-700"
          >Back End Developer</a
        >
      </nav>
    </div>
    <div class="mt-2 md:flex md:items-center md:justify-between">
      <div class="flex-1 min-w-0">
        <h2
          class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:leading-9 sm:truncate"
        >
          Back End Developer
        </h2>
      </div>
      <div class="flex flex-shrink-0 mt-4 md:mt-0 md:ml-4">
        <span class="rounded-md shadow-sm">
          <button
            type="button"
            class="inline-flex items-center px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out bg-white border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:text-gray-800 active:bg-gray-50"
          >
            Edit
          </button>
        </span>
        <span class="ml-3 rounded-md shadow-sm">
          <button
            type="button"
            class="inline-flex items-center px-4 py-2 text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-500 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-700 active:bg-indigo-700"
          >
            Publish
          </button>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
