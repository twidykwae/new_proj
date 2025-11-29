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

  let route = $derived($currentRoute);

  function getComponent(path){
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
    return Home;
    }

  let CurrentComponent = $derived(getComponent(route));
</script>

<nav>
  <a href="#/">Home</a>
  <a href="#/about">About</a>
  <a href="#/users">Users</a>
  <a href="#/admin">Admin</a>
  <a href="#/lostitems">Lost and Found</a>
  <a href="#/prayer-requests">Prayer Requests</a>
  {#if authStore.isAuthenticated}
    <a href="#/profile">Profile</a>
    <button onclick={() => { authStore.logout(); window.location.href = '/login'; }} class="btn-logout">
      Logout
    </button>
  {:else}
    <a href="#/login">Login</a>
  {/if}
</nav>

{#if CurrentComponent}
  <CurrentComponent />
{:else}
  <p>404 - Not Found</p>
{/if}