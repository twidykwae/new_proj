<script lang="ts">
  import { authStore } from '../src/stores/auth.svelte.js';
  import { navigate } from '../router.js';
  
  interface Token {
    access_token: string;
    token_type: string;
  }

  interface LoginError {
    detail: string;
  }

  let props = $props<{sendLogin?: any}>();
  let sendLogin = props.sendLogin;

  let username = $state('');
  let password = $state('');
  let loading = $state(false);
  let error = $state<string | null>(null);
  let token = $state<Token | null>(null);
  
  const API_URL = 'http://localhost:8000/api/v1';

  //async function forgotpassword

  async function handleSubmit(e: Event) {
    e.preventDefault();
    loading = true;
    error = null;
    token = null;

    try {
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
      
      await authStore.login(data.access_token);

      const savedUsername = username;
      username = '';
      password = '';

      if (savedUsername === 'admin@admin.com') {
        navigate('/admin');
      } else {
        navigate('/profile');
      }
    } catch (err) {
      error = err instanceof Error ? err.message : 'An error occurred';
    } finally {
      loading = false;
    }
  }
</script>

<div class="min-h-screen bg-gradient-to-bl from-sky-50 via-blue-50 to-sky-100 flex flex-col">

  <main class="flex-1 flex items-center justify-center px-4 py-8">
    {#if token}
      <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full text-center">
        <div class="w-16 h-16 bg-sky-100 rounded-full flex items-center justify-center mx-auto mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-sky-500">
            <path fill-rule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12Zm13.36-1.814a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z" clip-rule="evenodd" />
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-900 mb-2">Login Successful!</h2>
        <p class="text-gray-600">Redirecting...</p>
      </div>
    {:else}
      <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full">
        <div class="flex justify-center mb-6">
          <div class="w-16 h-16 bg-sky-100 rounded-full flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-sky-500">
              <path fill-rule="evenodd" d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25Zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5Z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>

        <h1 class="text-3xl font-bold text-gray-900 text-center mb-2">Welcome Back</h1>
        <p class="text-gray-600 text-center mb-8">Please enter your details to sign in.</p>

        {#if error}
          <div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
            <p class="text-red-600 text-sm">{error}</p>
          </div>
        {/if}

        <form on:submit={handleSubmit} class="space-y-6">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
              Email or Username
            </label>
            <input
              type="text"
              id="username"
              bind:value={username}
              placeholder="student@university.com/edu"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sky-500 focus:border-transparent outline-none transition-all"
            />
          </div>

          <div>
            <div class="flex items-center justify-between mb-2">
              <label for="password" class="block text-sm font-medium text-gray-700">
                Password
              </label>
              <button type="button" class="text-sm text-sky-600 hover:text-sky-700 font-medium">
                Forgot Password?
              </button>
            </div>
            <input
              type="password"
              id="password"
              bind:value={password}
              placeholder="••••••••"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-sky-500 focus:border-transparent outline-none transition-all"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            class="w-full bg-sky-500 hover:bg-sky-600 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {#if loading}
              <svg class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Logging in...
            {:else}
              Log In
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
                <path fill-rule="evenodd" d="M16.72 7.72a.75.75 0 0 1 1.06 0l4.5 4.5a.75.75 0 0 1 0 1.06l-4.5 4.5a.75.75 0 1 1-1.06-1.06l3.22-3.22H8.25a.75.75 0 0 1 0-1.5h11.69l-3.22-3.22a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd" />
              </svg>
            {/if}
          </button>

          <div class="text-center pt-4">
            <p class="text-gray-600 mb-4">New to Uni Core?</p>
            <a
              href="#/register"
              class="inline-block w-full border-2 border-gray-300 hover:border-sky-300 text-gray-700 hover:text-sky-600 font-semibold py-3 px-6 rounded-lg transition-colors duration-200"
            >
              Create an Account
            </a>
          </div>

        </form>
      </div>
    {/if}
  </main>

  <footer class="w-full px-6 py-6 flex flex-col sm:flex-row items-center justify-between text-sm text-gray-600">
    <p class="mb-4 sm:mb-0">© 2024 Uni Core. All rights reserved.</p>
  </footer>
</div>