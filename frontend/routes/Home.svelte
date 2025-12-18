<script lang="ts">
	// No logic needed for now
    import { onMount } from 'svelte';
    import { authStore } from '../src/stores/auth.svelte.js';
    interface Token{
        access_token: string;
        token_type: string;
    }

    let token = $state<Token | null>(null);
    onMount(() => {
        if (authStore.isAuthenticated) {
            token = {
                access_token: authStore.getToken() || '',
                token_type: 'Bearer'
            };
        }
    });

</script>
<div class="mx-auto">
	<div class="bg-red-100 p-10 text-center">
		<h1>One place for campus life</h1>
		<p>Connect with roommates, find lost items, and share prayer requests. Build your community here, in a safe trusted space</p>
		<button>Sign Up</button>
		<button>Login</button>
	</div>
</div>


<div class="bg-gray-50 py-16 px-6">
	<div class="max-w-3xl mx-auto text-center mb-12">
		<h1 class="text-4xl font-bold text-gray-900 mb-4">
			Core Features
		</h1>
		<p class="text-gray-400">
			Everything you need to navigate student life and feel at home.
		</p>
	</div>

	<!-- Cards -->
	<div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10">
		<!-- Card 1 -->
		<div class="rounded-xl shadow p-6 bg-gray-100">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6 text-blue-300">
  			<path d="M8.25 6.75a3.75 3.75 0 1 1 7.5 0 3.75 3.75 0 0 1-7.5 0ZM15.75 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM2.25 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM6.31 15.117A6.745 6.745 0 0 1 12 12a6.745 6.745 0 0 1 6.709 7.498.75.75 0 0 1-.372.568A12.696 12.696 0 0 1 12 21.75c-2.305 0-4.47-.612-6.337-1.684a.75.75 0 0 1-.372-.568 6.787 6.787 0 0 1 1.019-4.38Z" clipRule="evenodd" />
  			<path d="M5.082 14.254a8.287 8.287 0 0 0-1.308 5.135 9.687 9.687 0 0 1-1.764-.44l-.115-.04a.563.563 0 0 1-.373-.487l-.01-.121a3.75 3.75 0 0 1 3.57-4.047ZM20.226 19.389a8.287 8.287 0 0 0-1.308-5.135 3.75 3.75 0 0 1 3.57 4.047l-.01.121a.563.563 0 0 1-.373.486l-.115.04c-.567.2-1.156.349-1.764.441Z" />
			</svg>

			<h2 class="text-xl font-semibold mb-3 mt-4">
				Roommate Finder
			</h2>

			<p class="text-gray-600">
				Connect with potential roommates based on lifestyle preferences,
				study habits, and interests to find the perfect match.
			</p>
		</div>

		<!-- Card 2 -->
		<div class="rounded-xl shadow p-6 bg-gray-100">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6 text-blue-300">
  			<path d="M10.5 3.75a6.75 6.75 0 1 0 0 13.5 6.75 6.75 0 0 0 0-13.5ZM2.25 10.5a8.25 8.25 0 1 1 14.59 5.28l4.69 4.69a.75.75 0 1 1-1.06 1.06l-4.69-4.69A8.25 8.25 0 0 1 2.25 10.5Z" clipRule="evenodd" />
			</svg>
			<h2 class="text-xl font-semibold mb-3 mt-4">
				Lost & Found
			</h2>
			<p class="text-gray-600">
				Report and search for lost items on campus and reunite with your
				belongings quickly and easily.
			</p>
		</div>

		<!-- Card 3 -->
		<div class="rounded-xl shadow p-6 bg-gray-100">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6 text-blue-300">
  			<path d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z" />
			</svg>


			<h2 class="text-xl font-semibold mb-3 mt-4">
				Prayer Requests
			</h2>
			<p class="text-gray-600">
				Share prayer needs and receive spiritual support from a caring
				student community.
			</p>
		</div>
	</div>
</div>



<div class="bg-gray-50 py-20 px-6">
	<div class="max-w-3xl mx-auto rounded-2xl bg-black/60 backdrop-blur-md p-10 text-center text-white">
		<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="size-10">
  		<path d="m20.893 13.393-1.135-1.135a2.252 2.252 0 0 1-.421-.585l-1.08-2.16a.414.414 0 0 0-.663-.107.827.827 0 0 1-.812.21l-1.273-.363a.89.89 0 0 0-.738 1.595l.587.39c.59.395.674 1.23.172 1.732l-.2.2c-.212.212-.33.498-.33.796v.41c0 .409-.11.809-.32 1.158l-1.315 2.191a2.11 2.11 0 0 1-1.81 1.025 1.055 1.055 0 0 1-1.055-1.055v-1.172c0-.92-.56-1.747-1.414-2.089l-.655-.261a2.25 2.25 0 0 1-1.383-2.46l.007-.042a2.25 2.25 0 0 1 .29-.787l.09-.15a2.25 2.25 0 0 1 2.37-1.048l1.178.236a1.125 1.125 0 0 0 1.302-.795l.208-.73a1.125 1.125 0 0 0-.578-1.315l-.665-.332-.091.091a2.25 2.25 0 0 1-1.591.659h-.18c-.249 0-.487.1-.662.274a.931.931 0 0 1-1.458-1.137l1.411-2.353a2.25 2.25 0 0 0 .286-.76m11.928 9.869A9 9 0 0 0 8.965 3.525m11.928 9.868A9 9 0 1 1 8.965 3.525" />
		</svg>
		<h1 class="text-3xl font-semibold mb-4">
			A Community That Cares
		</h1>

		<p class="text-gray-600 mb-6 text-white">
			UniCore is designed to make campus feel like home. Join a safe space
			where students support students, fostering connection and belonging.
		</p>

		<button
			class="px-6 py-3 rounded-lg bg-blue-300 text-white font-medium hover:bg-blue-700 transition"
		>
			Join the Community
		</button>
	</div>
</div>



<div class="py-8 px-6 font-light">
	<div class="flex items-center justify-between px-6">
		<div class="flex items-center gap-2">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 24 24"
				fill="currentColor"
				class="size-6 text-blue-300"
			>
				<path d="M11.7 2.805a.75.75 0 0 1 .6 0A60.65 60.65 0 0 1 22.83 8.72a.75.75 0 0 1-.231 1.337 49.948 49.948 0 0 0-9.902 3.912l-.003.002c-.114.06-.227.119-.34.18a.75.75 0 0 1-.707 0A50.88 50.88 0 0 0 7.5 12.173v-.224c0-.131.067-.248.172-.311a54.615 54.615 0 0 1 4.653-2.52.75.75 0 0 0-.65-1.352 56.123 56.123 0 0 0-4.78 2.589 1.858 1.858 0 0 0-.859 1.228 49.803 49.803 0 0 0-4.634-1.527.75.75 0 0 1-.231-1.337A60.653 60.653 0 0 1 11.7 2.805Z" />
				<path d="M13.06 15.473a48.45 48.45 0 0 1 7.666-3.282c.134 1.414.22 2.843.255 4.284a.75.75 0 0 1-.46.711 47.87 47.87 0 0 0-8.105 4.342.75.75 0 0 1-.832 0 47.87 47.87 0 0 0-8.104-4.342.75.75 0 0 1-.461-.71c.035-1.442.121-2.87.255-4.286.921.304 1.83.634 2.726.99v1.27a1.5 1.5 0 0 0-.14 2.508c-.09.38-.222.753-.397 1.11.452.213.901.434 1.346.66a6.727 6.727 0 0 0 .551-1.607 1.5 1.5 0 0 0 .14-2.67v-.645a48.549 48.549 0 0 1 3.44 1.667 2.25 2.25 0 0 0 2.12 0Z" />
				<path d="M4.462 19.462c.42-.419.753-.89 1-1.395.453.214.902.435 1.347.662a6.742 6.742 0 0 1-1.286 1.794.75.75 0 0 1-1.06-1.06Z" />
			</svg>

			<h1 class="text-lg font-light">UniCore</h1>
		</div>

		<!-- Right side -->
		<p class="text-sm text-gray-500 px-10">
			© 2024 UniCore. All rights reserved.
		</p>
	</div>
</div>


