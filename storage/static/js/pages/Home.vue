<template>
  <div>
    <div
      class="bg-white xl:flex-shrink-0 xl:w-64 xl:border-r xl:border-gray-200"
    >
      <div class="py-6 pl-4 pr-6 sm:pl-6 lg:pl-8 xl:pl-0">
        <div class="flex items-center justify-between">
          <div class="flex-1 space-y-8">
            <div
              class="space-y-8 sm:space-y-0 sm:flex sm:justify-between sm:items-center xl:block xl:space-y-8"
            >
              <!-- Profile -->
              <div class="flex items-center space-x-3">
                <div class="flex-shrink-0 w-12 h-12">
                  <img
                    class="w-12 h-12 rounded-full"
                    src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=256&h=256&q=80"
                    alt=""
                  />
                </div>
                <div class="space-y-1">
                  <div class="text-sm font-medium leading-5 text-gray-900">
                    Debbie Lewis
                  </div>
                  <a href="#" class="group flex items-center space-x-2.5">
                    <svg
                      class="w-5 h-5 text-gray-400 group-hover:text-gray-500"
                      viewBox="0 0 18 18"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        fill-rule="evenodd"
                        clip-rule="evenodd"
                        d="M8.99917 0C4.02996 0 0 4.02545 0 8.99143C0 12.9639 2.57853 16.3336 6.15489 17.5225C6.60518 17.6053 6.76927 17.3277 6.76927 17.0892C6.76927 16.8762 6.76153 16.3104 6.75711 15.5603C4.25372 16.1034 3.72553 14.3548 3.72553 14.3548C3.31612 13.316 2.72605 13.0395 2.72605 13.0395C1.9089 12.482 2.78793 12.4931 2.78793 12.4931C3.69127 12.5565 4.16643 13.4198 4.16643 13.4198C4.96921 14.7936 6.27312 14.3968 6.78584 14.1666C6.86761 13.5859 7.10022 13.1896 7.35713 12.965C5.35873 12.7381 3.25756 11.9665 3.25756 8.52116C3.25756 7.53978 3.6084 6.73667 4.18411 6.10854C4.09129 5.88114 3.78244 4.96654 4.27251 3.72904C4.27251 3.72904 5.02778 3.48728 6.74717 4.65082C7.46487 4.45101 8.23506 4.35165 9.00028 4.34779C9.76494 4.35165 10.5346 4.45101 11.2534 4.65082C12.9717 3.48728 13.7258 3.72904 13.7258 3.72904C14.217 4.96654 13.9082 5.88114 13.8159 6.10854C14.3927 6.73667 14.7408 7.53978 14.7408 8.52116C14.7408 11.9753 12.6363 12.7354 10.6318 12.9578C10.9545 13.2355 11.2423 13.7841 11.2423 14.6231C11.2423 15.8247 11.2313 16.7945 11.2313 17.0892C11.2313 17.3299 11.3937 17.6097 11.8501 17.522C15.4237 16.3303 18 12.9628 18 8.99143C18 4.02545 13.97 0 8.99917 0Z"
                        fill="currentcolor"
                      />
                    </svg>
                    <div
                      class="text-sm font-medium leading-5 text-gray-500 group-hover:text-gray-900"
                    >
                      debbielewis
                    </div>
                  </a>
                </div>
              </div>
              <!-- Action buttons -->
              <div
                class="flex flex-col space-y-3 sm:space-y-0 sm:space-x-3 sm:flex-row xl:flex-col xl:space-x-0 xl:space-y-3"
              >
                <span class="inline-flex rounded-md shadow-sm">
                  <button
                    type="button"
                    class="inline-flex items-center justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700"
                  >
                    Random problem
                  </button>
                </span>
                <span class="inline-flex rounded-md shadow-sm">
                  <button
                    type="button"
                    class="inline-flex items-center justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out bg-white border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:text-gray-800 active:bg-gray-50"
                  >
                    Sync
                  </button>
                </span>
                <p class="text-sm text-gray-500">
                  Last updated at XX/XX/XX le XX:XX
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Recent climbs -->
    <div class="bg-white lg:min-w-0 lg:flex-1">
      <div
        class="pt-4 pb-4 pl-4 pr-6 border-t border-b border-gray-200 sm:pl-6 lg:pl-8 xl:pl-6 xl:pt-6 xl:border-t-0"
      >
        <div class="flex items-center">
          <h1 class="flex-1 text-lg font-medium leading-7">
            Accessed recently
          </h1>
          <div class="relative">
            <span class="rounded-md shadow-sm">
              <button
                id="sort-menu"
                type="button"
                class="inline-flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out bg-white border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
                aria-haspopup="true"
                aria-expanded="false"
              >
                <svg
                  class="w-5 h-5 mr-3 text-gray-400"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z"
                  />
                </svg>
                Sort
                <svg
                  class="ml-2.5 -mr-1.5 h-5 w-5 text-gray-400"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  />
                </svg>
              </button>
            </span>
            <div
              class="absolute right-0 z-10 w-56 mt-2 origin-top-right rounded-md shadow-lg"
            >
              <div class="bg-white rounded-md shadow-xs">
                <div
                  class="py-1"
                  role="menu"
                  aria-orientation="vertical"
                  aria-labelledby="sort-menu"
                >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm leading-5 text-gray-700 hover:bg-gray-100 hover:text-gray-900 focus:outline-none focus:bg-gray-100 focus:text-gray-900"
                    role="menuitem"
                    >Name</a
                  >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm leading-5 text-gray-700 hover:bg-gray-100 hover:text-gray-900 focus:outline-none focus:bg-gray-100 focus:text-gray-900"
                    role="menuitem"
                    >Date modified</a
                  >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm leading-5 text-gray-700 hover:bg-gray-100 hover:text-gray-900 focus:outline-none focus:bg-gray-100 focus:text-gray-900"
                    role="menuitem"
                    >Date created</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <ul
        class="relative z-0 border-b border-gray-200 divide-y divide-gray-200"
      >
        <li
          class="relative py-5 pl-4 pr-6 hover:bg-gray-50 sm:py-6 sm:pl-6 lg:pl-8 xl:pl-6"
        >
          <div class="flex items-center justify-between space-x-4">
            <!-- Repo name and link -->
            <div class="min-w-0 space-y-3">
              <div class="flex items-center space-x-3">
                <span
                  aria-label="Running"
                  class="flex items-center justify-center w-4 h-4 bg-green-100 rounded-full"
                >
                  <span class="w-2 h-2 bg-green-400 rounded-full"></span>
                </span>

                <span class="block">
                  <h2 class="text-sm font-medium leading-5">
                    <a href="#">
                      <span class="absolute inset-0"></span>
                      Workcation
                    </a>
                  </h2>
                </span>
              </div>
              <a href="#" class="relative group flex items-center space-x-2.5">
                <svg
                  class="flex-shrink-0 w-5 h-5 text-gray-400 group-hover:text-gray-500"
                  viewBox="0 0 18 18"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M8.99917 0C4.02996 0 0 4.02545 0 8.99143C0 12.9639 2.57853 16.3336 6.15489 17.5225C6.60518 17.6053 6.76927 17.3277 6.76927 17.0892C6.76927 16.8762 6.76153 16.3104 6.75711 15.5603C4.25372 16.1034 3.72553 14.3548 3.72553 14.3548C3.31612 13.316 2.72605 13.0395 2.72605 13.0395C1.9089 12.482 2.78793 12.4931 2.78793 12.4931C3.69127 12.5565 4.16643 13.4198 4.16643 13.4198C4.96921 14.7936 6.27312 14.3968 6.78584 14.1666C6.86761 13.5859 7.10022 13.1896 7.35713 12.965C5.35873 12.7381 3.25756 11.9665 3.25756 8.52116C3.25756 7.53978 3.6084 6.73667 4.18411 6.10854C4.09129 5.88114 3.78244 4.96654 4.27251 3.72904C4.27251 3.72904 5.02778 3.48728 6.74717 4.65082C7.46487 4.45101 8.23506 4.35165 9.00028 4.34779C9.76494 4.35165 10.5346 4.45101 11.2534 4.65082C12.9717 3.48728 13.7258 3.72904 13.7258 3.72904C14.217 4.96654 13.9082 5.88114 13.8159 6.10854C14.3927 6.73667 14.7408 7.53978 14.7408 8.52116C14.7408 11.9753 12.6363 12.7354 10.6318 12.9578C10.9545 13.2355 11.2423 13.7841 11.2423 14.6231C11.2423 15.8247 11.2313 16.7945 11.2313 17.0892C11.2313 17.3299 11.3937 17.6097 11.8501 17.522C15.4237 16.3303 18 12.9628 18 8.99143C18 4.02545 13.97 0 8.99917 0Z"
                    fill="currentcolor"
                  />
                </svg>
                <div
                  class="text-sm font-medium leading-5 text-gray-500 truncate group-hover:text-gray-900"
                >
                  debbielewis/workcation
                </div>
              </a>
            </div>
            <div class="sm:hidden">
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
            <!-- Repo meta info -->
            <div
              class="flex-col items-end flex-shrink-0 hidden space-y-3 sm:flex"
            >
              <p class="flex items-center space-x-4">
                <a
                  href="#"
                  class="relative text-sm font-medium leading-5 text-gray-500 hover:text-gray-900"
                >
                  Visit site
                </a>
                <button class="relative" type="button">
                  <svg
                    class="w-5 h-5 text-yellow-300 hover:text-yellow-400"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    />
                  </svg>
                </button>
              </p>
              <p class="flex space-x-2 text-sm leading-5 text-gray-500">
                <span>Laravel</span>
                <span>&middot;</span>
                <span>Last deploy 3h ago</span>
                <span>&middot;</span>
                <span>United states</span>
              </p>
            </div>
          </div>
        </li>

        <!-- More items... -->
      </ul>
    </div>
  </div>
</template>

<script>
// * Recent climbs
// * Climb list
// * Last update
// * Random one
// * Status
// * Add a climb (V2)
import BaseLayout from "../layouts/BaseLayout.vue";

export default {
  name: "Home",
  layout: BaseLayout,
};
</script>

<style></style>
