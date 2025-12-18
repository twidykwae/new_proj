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

<div class="hero-container">
	<h1>Core features</h1>
	<p>
		Eveything you need to navigate student life and feel at home
	</p>
	<button class="mt-2 px-4 py-2 bg-indigo-600 text-white rounded">
    View
  </button>
	
</div>
