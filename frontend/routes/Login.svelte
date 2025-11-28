<script lang="ts">
    import { authStore } from '../src/stores/auth.svelte.js';
    interface Token{
        access_token: string;
        token_type: string;
    }

    interface LoginError{
        detail: string;
    }

    let {sendLogin} = $props();

    let isLoggedIn = $state(false);
    let username = $state('');
    let password = $state('');
    let loading = $state(false);
    let error = $state<string | null>(null);
    let token = $state<Token | null>(null);
    let isLogin = $state(true);
    let full_name = $state("");
    let email = $state("");
    
    const API_URL = 'http://localhost:8000/api/v1';

    $effect(() => {
    isLoggedIn = localStorage.getItem('access_token') != "" ? true : false;
  });

  async function handleSubmit(e: Event) {
    e.preventDefault();
    loading = true;
    error = null;
    token = null;

    try {
      // Create FormData for OAuth2PasswordRequestForm
      const formData = new FormData();
      formData.append('grant_type', "password");
      formData.append('username', username);
      formData.append('password', password);

      const response = await fetch(`${API_URL}/users/token`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData: LoginError = await response.json();
        throw new Error(errorData.detail || 'Login failed');
      }

      const data: Token = await response.json();
      token = data;
      
      // Store token in authstore for future requests
      authStore.login(data.access_token, null);
      
      // Clear form
      username = '';
      password = '';

      // Redirect to profile after successful login
      window.location.href = `/profile/${username}`;

    } catch (err) {
      error = err instanceof Error ? err.message : 'An error occurred';
    } finally {
      loading = false;
    }
  }

  function logout() {
    token = null;
    authStore.logout();
    window.location.href = '/login';
  }

  function toggleMode() {
    isLogin = !isLogin;
    error = '';
  }
</script>

{#if token}
  <p>Login successful! Access Token: {token.access_token}</p>
  <button onclick={logout}>Logout</button>
{:else}
  <form onsubmit={handleSubmit}>
    <h2>{isLogin ? 'Login' : 'Register'}</h2>
    {#if error}
      <p class="error">{error}</p>
    {/if}
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" bind:value={username} required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" bind:value={password} required />
    </div>
    <button type="submit" disabled={loading}>
      {loading ? (isLogin ? 'Logging in...' : 'Registering...') : (isLogin ? 'Login' : 'Register')}
    </button>
  </form>
    
{/if}