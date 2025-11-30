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

<style>
	h1 {
		font-size: 3rem;
		font-weight: 700;
		letter-spacing: 1px;
		margin-bottom: 1rem;
	}

	p {
		font-size: 1.2rem;
		max-width: 600px;
		line-height: 1.6;
		opacity: 0.8;
	}

	.btn-container {
		margin-top: 2rem;
		display: flex;
		gap: 1.5rem;
	}

	a {
		text-decoration: none;
		color: white;
		border: 1px solid white;
		padding: 0.75rem 1.5rem;
		border-radius: 8px;
		font-size: 1rem;
		transition: 0.3s;
	}

	a:hover {
		background: #fff;
		color: #000;
	}
</style>

<div class="home-container">
	<h1>Campus Connect</h1>
	<p>
		A simple, all-in-one platform for students.  
		Find lost items, discover roommates, and share prayer requests —  
		all in one safe community.
	</p>

    {#if token}
        <div class="btn-container">
            <a href="#/lostitems">Lost & Found</a>
            <a href="#/roommates">Roommate Finder</a>
            <a href="#/prayer-requests">Prayer Requests</a>
        </div>
    {:else}
        <p style="margin-top: 2rem; opacity: 0.7;">
			Please log in to access Campus Connect features.
		</p>
		<div class="btn-container">
			<a href="#/login">Login</a>
		</div>
    {/if}
	
</div>
