<script lang="ts">
	import { navigate } from '../router.js';
	
	function handleGetStarted() {
		navigate('/register');
	}
	
	function handleLogin() {
		navigate('/login');
	}
</script>


<!-- Hero -->
<section class="relative min-h-[90vh] flex items-center overflow-hidden bg-white">
	<div class="absolute top-0 left-0 w-full h-1/2 bg-gradient-to-bl from-sky-200/50 to-transparent blur-3xl"></div>
	
	<div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32 w-full">
		<div class="grid lg:grid-cols-2 gap-12 items-center">
			<!-- Left  -->
			<div class="text-center lg:text-left">
				<div class="inline-flex items-center gap-2 px-4 py-1.5 bg-sky-100 text-sky-600 rounded-full text-sm font-medium mb-6">
					<span class="w-2 h-2 bg-sky-500 rounded-full"></span>
					NOW LIVE ON Taylor University Campus
				</div>
				
				<h1 class="text-5xl sm:text-6xl lg:text-7xl font-medium text-gray-900 mb-6">
					One place for
					<span class="text-sky-500">
						Taylor University Campus life
					</span>
				</h1>
				<p class="text-gray-600 mb-8 max-w-2xl mx-auto lg:mx-0 text-lg">
					Connect with roommates, find lost items, and share prayer requests. Build your community at university in a safe, trusted space.
				</p>
				<div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start mb-6">
					<button on:click={handleGetStarted} class="px-8 py-4 bg-sky-500 text-white text-lg font-semibold rounded-xl shadow-lg hover:bg-sky-600 hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-200">
						Sign Up 
					</button>
					<button on:click={handleLogin} class="px-8 py-4 bg-white text-gray-700 text-lg font-semibold rounded-xl shadow-md hover:shadow-lg border-2 border-gray-200 hover:border-sky-300 transform hover:-translate-y-0.5 transition-all duration-200">
						Log In
					</button>
				</div>
				
				<!-- Need to place student faces here -->
				<div class="flex items-center justify-center lg:justify-start gap-3">
					<div class="flex -space-x-2">
						<div class="w-10 h-10 rounded-full bg-gray-300 border-2 border-white"></div>
						<div class="w-10 h-10 rounded-full bg-gray-400 border-2 border-white"></div>
						<div class="w-10 h-10 rounded-full bg-gray-200 border-2 border-white"></div>
					</div>
					<p class="text-gray-600 text-sm">
						Joined by <span class="font-semibold text-gray-900">50+ students</span>
					</p>
				</div>
			</div>
			
			<!-- Right: Putting Taylor Image -->
			<div class="relative hidden lg:block">
				<div class="relative z-10">
					<div class="relative rounded-2xl overflow-hidden shadow-lg">
						<img src="../public/taylor.webp" alt="Taylor students" class="relative w-full h-auto object-cover rounded-2xl"/>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- Features -->
<section class="py-24 px-4 sm:px-6 lg:px-8 bg-white">
	<div class="max-w-7xl mx-auto">
		<div class="text-center mb-16">
			<h2 class="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
				Core Features
			</h2>
			<p class="text-xl text-gray-600 max-w-2xl mx-auto">
				Everything you need to navigate student life and feel at home.
			</p>
		</div>

		<div class="grid md:grid-cols-3 gap-8 lg:gap-12">
			<article class="bg-white rounded-2xl p-8 shadow-md hover:shadow-lg transition-all duration-300">
				<div class="w-16 h-16 bg-sky-100 rounded-xl flex items-center justify-center mb-6">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-sky-500">
						<path d="M8.25 6.75a3.75 3.75 0 1 1 7.5 0 3.75 3.75 0 0 1-7.5 0ZM15.75 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM2.25 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM6.31 15.117A6.745 6.745 0 0 1 12 12a6.745 6.745 0 0 1 6.709 7.498.75.75 0 0 1-.372.568A12.696 12.696 0 0 1 12 21.75c-2.305 0-4.47-.612-6.337-1.684a.75.75 0 0 1-.372-.568 6.787 6.787 0 0 1 1.019-4.38Z" clip-rule="evenodd" />
						<path d="M5.082 14.254a8.287 8.287 0 0 0-1.308 5.135 9.687 9.687 0 0 1-1.764-.44l-.115-.04a.563.563 0 0 1-.373-.487l-.01-.121a3.75 3.75 0 0 1 3.57-4.047ZM20.226 19.389a8.287 8.287 0 0 0-1.308-5.135 3.75 3.75 0 0 1 3.57 4.047l-.01.121a.563.563 0 0 1-.373.486l-.115.04c-.567.2-1.156.349-1.764.441Z" />
					</svg>
				</div>
				<h3 class="text-2xl font-bold text-gray-900 mb-3">
					Roommate Finder
				</h3>
				<p class="text-gray-600">
					Find compatible roommates based on shared values, study habits, and lifestyle preferences.
				</p>
			</article>

			<article class="bg-white rounded-2xl p-8 shadow-md hover:shadow-lg transition-all duration-300">
				<div class="w-16 h-16 bg-sky-100 rounded-xl flex items-center justify-center mb-6">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-sky-500">
						<path fill-rule="evenodd" d="M10.5 3.75a6.75 6.75 0 1 0 0 13.5 6.75 6.75 0 0 0 0-13.5ZM2.25 10.5a8.25 8.25 0 1 1 14.59 5.28l4.69 4.69a.75.75 0 1 1-1.06 1.06l-4.69-4.69A8.25 8.25 0 0 1 2.25 10.5Z" clip-rule="evenodd" />
					</svg>
				</div>
				<h3 class="text-2xl font-bold text-gray-900 mb-3">
					Lost & Found
				</h3>
				<p class="text-gray-600">
					Easily report lost items or search for found belongings across campus locations.
				</p>
			</article>

			<article class="bg-white rounded-2xl p-8 shadow-md hover:shadow-lg transition-all duration-300">
				<div class="w-16 h-16 bg-sky-100 rounded-xl flex items-center justify-center mb-6">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-sky-500">
						<path d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z" />
					</svg>
				</div>
				<h3 class="text-2xl font-bold text-gray-900 mb-3">
					Prayer Requests
				</h3>
				<p class="text-gray-600 leading-relaxed">
					A safe, supportive space to share prayer requests and uplift one another in community.
				</p>
			</article>
		</div>
	</div>
</section>

<!-- CTA Section -->
<section class="py-24 px-4 sm:px-6 lg:px-8 bg-gray-900 relative overflow-hidden">
	<div class="absolute inset-0 bg-gradient-to-br from-sky-500/20 via-transparent to-transparent"></div>
	<div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-sky-400/30 rounded-full blur-3xl"></div>
	
	<div class="relative z-10 max-w-4xl mx-auto text-center">
		<div class="inline-block mb-6">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-16 h-16 text-sky-400">
				<path d="M8.25 6.75a3.75 3.75 0 1 1 7.5 0 3.75 3.75 0 0 1-7.5 0ZM15.75 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM2.25 9.75a3 3 0 1 1 6 0 3 3 0 0 1-6 0ZM6.31 15.117A6.745 6.745 0 0 1 12 12a6.745 6.745 0 0 1 6.709 7.498.75.75 0 0 1-.372.568A12.696 12.696 0 0 1 12 21.75c-2.305 0-4.47-.612-6.337-1.684a.75.75 0 0 1-.372-.568 6.787 6.787 0 0 1 1.019-4.38Z" clip-rule="evenodd" />
				<path d="M5.082 14.254a8.287 8.287 0 0 0-1.308 5.135 9.687 9.687 0 0 1-1.764-.44l-.115-.04a.563.563 0 0 1-.373-.487l-.01-.121a3.75 3.75 0 0 1 3.57-4.047ZM20.226 19.389a8.287 8.287 0 0 0-1.308-5.135 3.75 3.75 0 0 1 3.57 4.047l-.01.121a.563.563 0 0 1-.373.486l-.115.04c-.567.2-1.156.349-1.764.441Z" />
			</svg>
		</div>
		<h2 class="text-4xl sm:text-5xl font-bold text-white mb-6">
			A Community That Cares
		</h2>
		<p class="text-xl text-gray-300 mb-8 max-w-2xl mx-auto leading-relaxed">
			Uni Core is designed to make campus feel like home. Join a safe space where students support students, fostering connection and belonging.
		</p>
		<button
			on:click={handleGetStarted}
			class="px-8 py-4 bg-sky-500 text-white text-lg font-semibold rounded-xl shadow-xl hover:bg-sky-600 hover:shadow-2xl transform hover:-translate-y-0.5 transition-all duration-200"
		>
			Join the Community
		</button>
	</div>
</section>

<footer class="bg-white border-t border-gray-200 py-12 px-4 sm:px-6 lg:px-8">
	<div class="max-w-7xl mx-auto">
		<div class="flex flex-col md:flex-row items-center justify-between gap-4">
			<div class="flex items-center gap-2">
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6 text-sky-500">
					<path d="M11.7 2.805a.75.75 0 0 1 .6 0A60.65 60.65 0 0 1 22.83 8.72a.75.75 0 0 1-.231 1.337 49.948 49.948 0 0 0-9.902 3.912l-.003.002c-.114.06-.227.119-.34.18a.75.75 0 0 1-.707 0A50.88 50.88 0 0 0 7.5 12.173v-.224c0-.131.067-.248.172-.311a54.615 54.615 0 0 1 4.653-2.52.75.75 0 0 0-.65-1.352 56.123 56.123 0 0 0-4.78 2.589 1.858 1.858 0 0 0-.859 1.228 49.803 49.803 0 0 0-4.634-1.527.75.75 0 0 1-.231-1.337A60.653 60.653 0 0 1 11.7 2.805Z" />
					<path d="M13.06 15.473a48.45 48.45 0 0 1 7.666-3.282c.134 1.414.22 2.843.255 4.284a.75.75 0 0 1-.46.711 47.87 47.87 0 0 0-8.105 4.342.75.75 0 0 1-.832 0 47.87 47.87 0 0 0-8.104-4.342.75.75 0 0 1-.461-.71c.035-1.442.121-2.87.255-4.286.921.304 1.83.634 2.726.99v1.27a1.5 1.5 0 0 0-.14 2.508c-.09.38-.222.753-.397 1.11.452.213.901.434 1.346.66a6.727 6.727 0 0 0 .551-1.607 1.5 1.5 0 0 0 .14-2.67v-.645a48.549 48.549 0 0 1 3.44 1.667 2.25 2.25 0 0 0 2.12 0Z" />
					<path d="M4.462 19.462c.42-.419.753-.89 1-1.395.453.214.902.435 1.347.662a6.742 6.742 0 0 1-1.286 1.794.75.75 0 0 1-1.06-1.06Z" />
				</svg>
				<span class="text-lg font-semibold text-gray-900">Uni Core</span>
			</div>
			
				<p class="text-sm text-gray-500">
				©2024 Uni Core. All rights reserved.
			</p>
		</div>
	</div>
</footer>