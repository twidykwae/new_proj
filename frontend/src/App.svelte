<script lang="ts">
  import Users from '../routes/Users.svelte';
  import { currentRoute } from '../router.js';
  import Home from '../routes/Home.svelte';
  import About from '../routes/About.svelte';
  import Admin from '../routes/Admin.svelte';
  import {authStore} from '../src/stores/auth.svelte.js';
  import Login from '../routes/Login.svelte';
  import Profile from '../routes/Profile.svelte';
  import LostItemsList from '../routes/LostItems.svelte';
  import PrayerRequestsRoute from '../routes/PrayerRequestsRoute.svelte';
  import Register from '../routes/Register.svelte';
  let route = $derived($currentRoute);

  function getComponent(path: string | null | undefined){
    if(!path || path === '/'){
      return Home;
    } 
    if(path === '/about'){
      return About;
    }
    if(path === '/users'){
      return Users;
    }
    if(path === '/admin'){
      return Admin;
    }
    if(path === '/login'){
      return Login;
    }
    if(path === '/profile'){
      return Profile;
    } 
    
    if(path === '/lostitems'){
      return LostItemsList;
    }
    if(path === '/prayer-requests'){
      return PrayerRequestsRoute;
    }
    if(path === '/register'){
      return Register;
    }
    return Home;
    }

  let CurrentComponent = $derived(getComponent(route));

  function isActive(path: string): boolean {
    if (path === '/' && (!route || route === '/')) return true;
    return route === path;
  }

  function handleLogout() {
    authStore.logout();
    window.location.href = '/login';
  }

  let mobileMenuOpen = $state(false);

  function toggleMobileMenu() {
    mobileMenuOpen = !mobileMenuOpen;
  }

  function closeMobileMenu() {
    mobileMenuOpen = false;
  }
</script>

<nav class="sticky top-0 z-50 w-full backdrop-blur-md bg-white/80 border-b border-gray-200/50 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex-shrink-0">
        <a href="#/" class="text-xl font-bold text-gray-900 hover:text-sky-600 transition-colors">
          UniCore
        </a>
      </div>

      <div class="hidden md:flex items-center justify-center flex-1 gap-8">
        <a 
          href="#/" 
          class="nav-link {isActive('/') || isActive('') ? 'active' : ''}"
        >
          Home
        </a>
        <a 
          href="#/about" 
          class="nav-link {isActive('/about') ? 'active' : ''}"
        >
          About
        </a>
        {#if authStore.isAuthenticated}
          <a 
            href="#/lostitems" 
            class="nav-link {isActive('/lostitems') ? 'active' : ''}"
          >
            Lost & Found
          </a>
          <a 
            href="#/prayer-requests" 
            class="nav-link {isActive('/prayer-requests') ? 'active' : ''}"
          >
            Prayer Requests
          </a>
        {/if}
        {#if authStore.isAdmin()}
          <a 
            href="#/admin" 
            class="nav-link {isActive('/admin') ? 'active' : ''}"
          >
            Admin
          </a>
        {/if}
      </div>

      <div class="flex items-center gap-4">
        {#if authStore.isAuthenticated}
          <a 
            href="#/profile" 
            class="hidden md:block nav-link {isActive('/profile') ? 'active' : ''}"
          >
            Profile
          </a>
          <button 
            onclick={handleLogout}
            class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900 bg-white hover:bg-gray-50 border border-gray-300 rounded-lg transition-colors"
          >
            Logout
          </button>
        {:else}
          <a 
            href="#/login" 
            class="nav-link {isActive('/login') ? 'active' : ''}"
          >
            Login
          </a>
        {/if}

        <button 
          type="button"
          onclick={toggleMobileMenu}
          class="md:hidden p-2 rounded-lg text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-colors"
          aria-label="Toggle menu"
          aria-expanded={mobileMenuOpen}
        >
          {#if mobileMenuOpen}
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          {:else}
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          {/if}
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    {#if mobileMenuOpen}
      <div class="md:hidden border-t border-gray-200/50 bg-white/95 backdrop-blur-md">
        <div class="px-4 pt-2 pb-4 space-y-1">
          <a 
            href="#/" 
            onclick={closeMobileMenu}
            class="mobile-nav-link block px-3 py-2 rounded-lg {isActive('/') || isActive('') ? 'active' : ''}"
          >
            Home
          </a>
          <a 
            href="#/about" 
            onclick={closeMobileMenu}
            class="mobile-nav-link block px-3 py-2 rounded-lg {isActive('/about') ? 'active' : ''}"
          >
            About
          </a>
          {#if authStore.isAuthenticated}
            <a 
              href="#/lostitems" 
              onclick={closeMobileMenu}
              class="mobile-nav-link block px-3 py-2 rounded-lg {isActive('/lostitems') ? 'active' : ''}"
            >
              Lost & Found
            </a>
            <a 
              href="#/prayer-requests" 
              onclick={closeMobileMenu}
              class="mobile-nav-link block px-3 py-2 rounded-lg {isActive('/prayer-requests') ? 'active' : ''}"
            >
              Prayer Requests
            </a>
            <a 
              href="#/profile" 
              onclick={closeMobileMenu}
              class="mobile-nav-link block px-3 py-2 rounded-lg {isActive('/profile') ? 'active' : ''}"
            >
              Profile
            </a>
          {/if}
          {#if authStore.isAdmin()}
            <a 
              href="#/admin" 
              onclick={closeMobileMenu}
              class="mobile-nav-link block px-3 py-2 rounded-lg {isActive('/admin') ? 'active' : ''}"
            >
              Admin
            </a>
          {/if}
          {#if !authStore.isAuthenticated}
            <a 
              href="#/login" 
              onclick={closeMobileMenu}
              class="mobile-nav-link block px-3 py-2 rounded-lg {isActive('/login') ? 'active' : ''}"
            >
              Login
            </a>
          {/if}
          {#if authStore.isAuthenticated}
            <button 
              onclick={() => { closeMobileMenu(); handleLogout(); }}
              class="w-full text-left px-3 py-2 rounded-lg text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-colors font-medium"
            >
              Logout
            </button>
          {/if}
        </div>
      </div>
    {/if}
  </div>
</nav>

<style>
  .nav-link {
    @apply relative text-gray-600 font-medium transition-colors duration-200;
    @apply hover:text-gray-900;
  }

  .nav-link::after {
    content: '';
    @apply absolute bottom-0 left-0 w-0 h-0.5 bg-sky-500 transition-all duration-300;
  }

  .nav-link:hover::after {
    @apply w-full;
  }

  .nav-link.active {
    @apply text-gray-900;
  }

  .nav-link.active::after {
    @apply w-full;
  }

  .mobile-nav-link {
    @apply text-gray-600 font-medium transition-colors duration-200;
    @apply hover:text-gray-900 hover:bg-gray-50;
  }

  .mobile-nav-link.active {
    @apply text-gray-900 bg-sky-50;
  }
</style>

{#if CurrentComponent}
  <CurrentComponent />
{:else}
  <p>404 - Not Found</p>
{/if}