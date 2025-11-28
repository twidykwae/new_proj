<script lang="ts">
  import { authStore } from '../src/stores/auth.svelte.js';
  import { onMount } from 'svelte';
  let username = $state("");
  let email = $state("");

  function handleLogout() {
    authStore.logout();
    window.location.href = '/login';
  }

  async function fetchProfile() {
    if (authStore.isAuthenticated) {
      try {
        const token = authStore.getToken();
        const response = await fetch('http://localhost:8000/api/v1/users/me/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        if (!response.ok) {
          throw new Error('Failed to fetch profile');
        }

        const data = await response.json();
        username = data.name;
        email = data.email;

      } catch (error) {
        console.error('Error fetching profile:', error);
      }
    }
  }

  onMount(() => {
    fetchProfile();
  });
</script>

<p>Welcome {username}</p>
<p>Email: {email}</p>
<button onclick={handleLogout}>Logout</button>