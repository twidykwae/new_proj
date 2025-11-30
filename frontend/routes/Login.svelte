<script lang="ts">
    import { on } from 'svelte/events';
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
    let isAdmin = $state(false);
    
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

      const savedUsername = username;
            
      // Clear form
      username = '';
      password = '';

      if (savedUsername === 'admin@admin.com') {
          window.location.href = '#/admin';
        } else {
          window.location.href = `#/profile`;
        }

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
    isAdmin = false;
  }

</script>

{#if token}
<div class="success-container">
  <p>Login successful! Redirecting...</p>
</div>
{:else}
<div class="auth-container">
  <form onsubmit={handleSubmit}>
    <h2>{isLogin ? 'Login' : 'Register'}</h2>
    {#if error}
      <p class="error">{error}</p>
    {/if}
    <div>
      <label for="username">Email:</label>
      <input type="text" id="username" bind:value={username} placeholder="Enter your email" required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" bind:value={password} placeholder="Enter your password" required />
    </div>
    <button type="submit" class="submit-button" onclick={handleSubmit}>
      {loading ? (isLogin ? 'Logging in...' : 'Registering...') : (isLogin ? 'Login' : 'Register')}
    </button>
    <div>
      <p>Don't have an account? <a href="#/register">Register here</a></p>
    </div>
  </form>
</div>
    
{/if}