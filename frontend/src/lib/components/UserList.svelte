<script lang="ts">
    import { onMount } from 'svelte';
    import User from './User.svelte';

    let loading = $state(false);
    let error = $state(null);

    let users: any[];

    onMount(() => {
        fetchUsers();
    });

    async function fetchUsers(){
        loading = true;
        error = null;

        try{
            const response = await fetch('http://127.0.0.1:8000/api/v1/users');
            if(!response.ok){
                throw new Error('Failed to fetch users');
            }
            users = await response.json();
        }catch(err){
            error = err.message;
        }finally{
            loading = false;
        }
    }
</script>

<h1>Users</h1>


{#if loading}
    <p>Loading users...</p>
{:else if error}
    <p class="error">Error: {error}</p>
{:else}
    <ul>
        {#each users as user}
            <li>{user.name} - {user.email}</li>
        {/each}
    </ul>
{/if}

<button onclick={fetchUsers}>Refresh Users</button>
