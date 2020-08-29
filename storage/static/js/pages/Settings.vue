<template>
  <div class="container p-4 mx-auto">
    <form>
      <div>
        <div>
          <div>
            <h3 class="text-lg font-medium leading-6 text-gray-900">
              General
            </h3>
            <p class="mt-1 text-sm leading-5 text-gray-500">
              General settings for your system board.
            </p>
          </div>
          <div class="grid grid-cols-1 row-gap-6 col-gap-4 mt-6 sm:grid-cols-6">
            <div class="sm:col-span-4">
              <label
                for="username"
                class="block text-sm font-medium leading-5 text-gray-700"
              >
                Username
              </label>
              <div class="flex mt-1 rounded-md shadow-sm">
                <span
                  class="inline-flex items-center px-3 text-gray-500 border border-r-0 border-gray-300 rounded-l-md bg-gray-50 sm:text-sm"
                >
                  workcation.com/
                </span>
                <input
                  id="username"
                  class="flex-1 block w-full min-w-0 transition duration-150 ease-in-out rounded-none form-input rounded-r-md sm:text-sm sm:leading-5"
                />
              </div>
            </div>

            <div class="sm:col-span-6">
              <label
                for="about"
                class="block text-sm font-medium leading-5 text-gray-700"
              >
                About
              </label>
              <div class="mt-1 rounded-md shadow-sm">
                <textarea
                  id="about"
                  rows="3"
                  class="block w-full transition duration-150 ease-in-out form-textarea sm:text-sm sm:leading-5"
                ></textarea>
              </div>
              <p class="mt-2 text-sm text-gray-500">
                Write a few sentences about yourself.
              </p>
            </div>

            <div class="sm:col-span-6">
              <label
                for="photo"
                class="block text-sm font-medium leading-5 text-gray-700"
              >
                Photo
              </label>
              <div class="flex items-center mt-2">
                <span
                  class="w-12 h-12 overflow-hidden bg-gray-100 rounded-full"
                >
                  <svg
                    class="w-full h-full text-gray-300"
                    fill="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      d="M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z"
                    />
                  </svg>
                </span>
                <span class="ml-5 rounded-md shadow-sm">
                  <button
                    type="button"
                    class="px-3 py-2 text-sm font-medium leading-4 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                  >
                    Change
                  </button>
                </span>
              </div>
            </div>

            <div class="sm:col-span-6">
              <label
                for="cover_photo"
                class="block text-sm font-medium leading-5 text-gray-700"
              >
                Cover photo
              </label>
              <div
                class="flex justify-center px-6 pt-5 pb-6 mt-2 border-2 border-gray-300 border-dashed rounded-md"
              >
                <div class="text-center">
                  <svg
                    class="w-12 h-12 mx-auto text-gray-400"
                    stroke="currentColor"
                    fill="none"
                    viewBox="0 0 48 48"
                  >
                    <path
                      d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                  <p class="mt-1 text-sm text-gray-600">
                    <button
                      type="button"
                      class="font-medium text-indigo-600 transition duration-150 ease-in-out hover:text-indigo-500 focus:outline-none focus:underline"
                    >
                      Upload a file
                    </button>
                    or drag and drop
                  </p>
                  <p class="mt-1 text-xs text-gray-500">
                    PNG, JPG, GIF up to 10MB
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="pt-8 mt-8 border-t border-gray-200">
          <div>
            <h3 class="text-lg font-medium leading-6 text-gray-900">
              System board controller
            </h3>
            <p class="mt-1 text-sm leading-5 text-gray-500">
              Remote control your system board leds controller.
            </p>
          </div>
          <div class="mt-6">
            <div class="flex justify-end">
              <span class="inline-flex rounded-md shadow-sm">
                <button
                  type="button"
                  class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                >
                  Restart
                </button>
              </span>
              <span class="inline-flex ml-3 rounded-md shadow-sm">
                <button
                  type="submit"
                  class="inline-flex justify-center px-4 py-2 text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700"
                >
                  Shutdown
                </button>
              </span>
            </div>
          </div>
        </div>
        <div class="pt-8 mt-8 border-t border-gray-200">
          <div>
            <h3 class="text-lg font-medium leading-6 text-gray-900">
              Testing & Troubleshooting
            </h3>
            <p class="mt-1 text-sm leading-5 text-gray-500">
              Test controls for troubleshoot and configure your system board.
            </p>
          </div>
          <div class="mt-6">
            <div>
              <label
                for="email"
                class="block text-sm font-medium leading-5 text-gray-700"
                >Toggle LED number</label
              >
              <div class="flex mt-1 rounded-md shadow-sm">
                <div class="relative flex-grow focus-within:z-10">
                  <div
                    class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                  >
                    <svg
                      class="w-5 h-5 text-gray-400"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"
                      />
                    </svg>
                  </div>
                  <input
                    id="email"
                    class="block w-full pl-10 transition duration-150 ease-in-out rounded-none form-input rounded-l-md sm:text-sm sm:leading-5"
                    placeholder="LED index"
                  />
                </div>
                <button
                  class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-indigo-500 border border-gray-300 rounded-r-md hover:text-gray-500 hover:bg-white focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-gray-100 active:text-gray-700"
                >
                  <svg
                    class="w-5 h-5 text-gray-400"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z"
                    />
                  </svg>
                  <span class="ml-2">Toggle</span>
                </button>
              </div>
            </div>
            <div>
              <label
                for="location"
                class="block text-sm font-medium leading-5 text-gray-700"
                >Color</label
              >
              <select
                id="location"
                class="block w-full py-2 pl-3 pr-10 mt-1 text-base leading-6 border-gray-300 form-select focus:outline-none focus:shadow-outline-blue focus:border-blue-300 sm:text-sm sm:leading-5"
              >
                <option>Red</option>
                <option selected>Blue</option>
                <option>Green</option>
              </select>
            </div>
            <div>
              <label
                for="location"
                class="block text-sm font-medium leading-5 text-gray-700"
                >Brightness</label
              >
              <select
                id="brightness"
                class="block w-full py-2 pl-3 pr-10 mt-1 text-base leading-6 border-gray-300 form-select focus:outline-none focus:shadow-outline-blue focus:border-blue-300 sm:text-sm sm:leading-5"
              >
                <option>10%</option>
                <option selected>20%</option>
                <option>30%</option>
                <option>100%</option>
              </select>
            </div>
            <div class="pt-5 mt-6">
              <div class="flex justify-start">
                <span class="inline-flex rounded-md shadow-sm">
                  <button
                    type="button"
                    class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                  >
                    Run start animation
                  </button>
                </span>
                <span class="inline-flex ml-3 rounded-md shadow-sm">
                  <button
                    type="button"
                    class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                  >
                    Light all leds
                  </button>
                </span>
                <span class="inline-flex ml-3 rounded-md shadow-sm">
                  <button
                    type="button"
                    class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                  >
                    Clear board
                  </button>
                </span>
                <span class="inline-flex ml-3 rounded-md shadow-sm">
                  <button
                    type="button"
                    class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                  >
                    Display test problem
                  </button>
                </span>
                <span class="inline-flex ml-3 rounded-md shadow-sm">
                  <button
                    type="button"
                    class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                  >
                    Display first hold
                  </button>
                </span>
                <span class="inline-flex ml-3 rounded-md shadow-sm">
                  <button
                    type="button"
                    class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                  >
                    Display last hold
                  </button>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pt-5 mt-8 border-t border-gray-200">
        <div class="flex justify-end">
          <span class="inline-flex rounded-md shadow-sm">
            <button
              type="button"
              class="px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
            >
              Cancel
            </button>
          </span>
          <span class="inline-flex ml-3 rounded-md shadow-sm">
            <button
              type="submit"
              class="inline-flex justify-center px-4 py-2 text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700"
            >
              Save
            </button>
          </span>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Settings",
  //   ### Settings
  // * Brightness
  // * Animation
  // * Colors for each holds type

  // * Test mode
  // * Board holds (set A, B, C)

  // * Restart
  // * Shut down
};
</script>

<style></style>
