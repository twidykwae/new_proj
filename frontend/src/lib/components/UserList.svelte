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
        }catch(error: unknown){
            error = (error as Error).message;
        }finally{
            loading = false;
        }
    }


    async function deleteUser(user_id){
        if(confirm('Are you sure you want to delete this user?')){
            try{
                const response = await fetch(`http://127.0.0.1:8000/api/v1/users/${user_id}`, {
                    method: 'DELETE'
                });
                if(!response.ok){
                    throw new Error('Failed to delete user');
                }
            }catch(error: unknown){
                error = (error as Error).message;
            }finally{
                fetchUsers();
            }
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
            <h1>{user.name}</h1>
            <li>ID - {user.id}, Email:{user.email}</li>
            <button onclick={() => deleteUser(user.id)}>Delete User</button>
        {/each}
    </ul>
{/if}
<button onclick={fetchUsers}>Refresh Users</button>
