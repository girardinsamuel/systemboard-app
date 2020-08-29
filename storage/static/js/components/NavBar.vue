<template>
  <!-- Navbar -->
  <nav class="flex-shrink-0 bg-indigo-700">
    <div class="px-2 mx-auto max-w-7xl sm:px-4 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <!-- Logo section -->
        <div class="flex items-center px-2 lg:px-0 xl:w-64">
          <div class="flex-shrink-0">
            <inertia-link href="/">
              <img
                class="w-auto h-8"
                src="https://tailwindui.com/img/logos/workflow-mark-on-brand.svg"
                alt="Workflow logo"
              />
            </inertia-link>
          </div>
        </div>

        <!-- Search section -->
        <div class="flex justify-center flex-1 lg:justify-end">
          <div class="w-full px-2 lg:px-6">
            <label for="search" class="sr-only">Search projects</label>
            <div class="relative text-indigo-300 focus-within:text-gray-400">
              <div
                class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                    clip-rule="evenodd"
                  />
                </svg>
              </div>
              <input
                id="search"
                class="block w-full py-2 pl-10 pr-3 leading-5 text-indigo-300 placeholder-indigo-300 transition duration-150 ease-in-out bg-indigo-400 bg-opacity-25 border border-transparent rounded-md focus:outline-none focus:bg-white focus:placeholder-gray-400 focus:text-gray-900 sm:text-sm"
                placeholder="Search climbs"
                type="search"
                @change="search"
              />
            </div>
          </div>
        </div>
        <div class="flex lg:hidden">
          <!-- Mobile menu button -->
          <button
            class="inline-flex items-center justify-center p-2 text-indigo-400 transition duration-150 ease-in-out rounded-md hover:text-white hover:bg-indigo-600 focus:outline-none focus:bg-indigo-600 focus:text-white"
            aria-label="Main menu"
            aria-expanded="false"
          >
            <!-- Icon when menu is closed. -->
            <!-- Menu open: "hidden", Menu closed: "block" -->
            <svg
              class="block w-6 h-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h8m-8 6h16"
              />
            </svg>
            <!-- Icon when menu is open. -->
            <!-- Menu open: "block", Menu closed: "hidden" -->
            <svg
              class="hidden w-6 h-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <!-- Links section -->
        <div class="hidden lg:block lg:w-80">
          <div class="flex items-center justify-end">
            <div class="flex">
              <a
                href="#"
                class="px-3 py-2 text-sm font-medium leading-5 text-indigo-200 transition duration-150 ease-in-out rounded-md hover:text-white focus:outline-none focus:text-white focus:bg-indigo-600"
                >Documentation</a
              >
              <a
                href="#"
                class="px-3 py-2 text-sm font-medium leading-5 text-indigo-200 transition duration-150 ease-in-out rounded-md hover:text-white focus:outline-none focus:text-white focus:bg-indigo-600"
                >Support</a
              >
            </div>
            <!-- Profile dropdown -->
            <div class="relative flex-shrink-0 ml-4">
              <div>
                <button
                  class="flex text-sm text-white transition duration-150 ease-in-out rounded-full focus:outline-none focus:shadow-solid"
                  id="user-menu"
                  aria-label="User menu"
                  aria-haspopup="true"
                >
                  <img
                    class="w-8 h-8 rounded-full"
                    src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=256&h=256&q=80"
                    alt=""
                  />
                </button>
              </div>
              <!--
                Profile dropdown panel, show/hide based on dropdown state.

                Entering: "transition ease-out duration-100"
                  From: "transform opacity-0 scale-95"
                  To: "transform opacity-100 scale-100"
                Leaving: "transition ease-in duration-75"
                  From: "transform opacity-100 scale-100"
                  To: "transform opacity-0 scale-95"
              -->
              <div
                class="absolute right-0 w-48 mt-2 origin-top-right rounded-md shadow-lg"
              >
                <div
                  class="py-1 bg-white rounded-md shadow-xs"
                  role="menu"
                  aria-orientation="vertical"
                  aria-labelledby="user-menu"
                >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm leading-5 text-gray-700 transition duration-150 ease-in-out hover:bg-gray-100 focus:outline-none focus:bg-gray-100"
                    role="menuitem"
                    >View Profile</a
                  >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm leading-5 text-gray-700 transition duration-150 ease-in-out hover:bg-gray-100 focus:outline-none focus:bg-gray-100"
                    role="menuitem"
                    >Settings</a
                  >
                  <a
                    href="#"
                    class="block px-4 py-2 text-sm leading-5 text-gray-700 transition duration-150 ease-in-out hover:bg-gray-100 focus:outline-none focus:bg-gray-100"
                    role="menuitem"
                    >Logout</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!--
      Mobile menu, toggle classes based on menu state.

      Menu open: "block", Menu closed: "hidden"
    -->
    <div class="hidden lg:hidden">
      <div class="px-2 pt-2 pb-3">
        <a
          href="#"
          class="block px-3 py-2 text-base font-medium text-white transition duration-150 ease-in-out bg-indigo-800 rounded-md focus:outline-none focus:text-indigo-100 focus:bg-indigo-600"
          >Dashboard</a
        >
        <a
          href="#"
          class="block px-3 py-2 mt-1 text-base font-medium text-indigo-200 transition duration-150 ease-in-out rounded-md hover:text-indigo-100 hover:bg-indigo-600 focus:outline-none focus:text-white focus:bg-indigo-600"
          >Support</a
        >
      </div>
      <div class="pt-4 pb-3 border-t border-indigo-800">
        <div class="px-2">
          <a
            href="#"
            class="block px-3 py-2 text-base font-medium text-indigo-200 transition duration-150 ease-in-out rounded-md hover:text-indigo-100 hover:bg-indigo-600 focus:outline-none focus:text-white focus:bg-indigo-600"
            >Your Profile</a
          >
          <a
            href="#"
            class="block px-3 py-2 mt-1 text-base font-medium text-indigo-200 transition duration-150 ease-in-out rounded-md hover:text-indigo-100 hover:bg-indigo-600 focus:outline-none focus:text-white focus:bg-indigo-600"
            >Settings</a
          >
          <a
            href="#"
            class="block px-3 py-2 mt-1 text-base font-medium text-indigo-200 transition duration-150 ease-in-out rounded-md hover:text-indigo-100 hover:bg-indigo-600 focus:outline-none focus:text-white focus:bg-indigo-600"
            >Sign out</a
          >
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
    search() {
      this.$inertia.visit("/problems");
    },
  },
};
</script>

<style></style>
