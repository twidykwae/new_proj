<script lang="ts">
    import { onMount } from 'svelte';
    import User from '../../../routes/Users.svelte';

    let loading = $state(false);
    let error = $state(null);

    let users: any[];
    let totalUsers = $state(0);
    let currentPage = $state(1);
    let selectedResults = $state("10");
    let perPageResults = $derived(parseInt(selectedResults));
    let totalPages = $derived(totalUsers > 0 ? Math.ceil(totalUsers / perPageResults) : 10);
    let userSearchText = $state("");

    onMount(() => {
        fetchUsers();
    });

    async function fetchUsers(){
        loading = true;
        error = null;

        try{
            const response = await fetch(`http://127.0.0.1:8000/api/v1/users?curPage=${currentPage}&pageSize=${perPageResults}&earch=${userSearchText}`);
            if(!response.ok){
                throw new Error('Failed to fetch users');
            }
            const data = await response.json();
            totalUsers = data.total ? parseInt(data.total) : 0;
            users = data.users;
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

    async function goToPage(event: MouseEvent, page: number){
        event.preventDefault();
        currentPage = page;
        await fetchUsers();

    }

    async function nextPage(event: MouseEvent){
        event.preventDefault();
        if(currentPage < totalPages){
            currentPage += 1;
            fetchUsers();
        }
    }

    async function prevPage(event: MouseEvent){
        event.preventDefault();
        if (currentPage > 1) {
            currentPage -= 1;
            fetchUsers();
        }
    }

    function search(){
        currentPage = 0;
        fetchUsers();
    }
</script>
<h1>Users</h1>

<div class="results-per-page">
    Results per page:
    <select bind:value={selectedResults} 
        onchange={() => { 
            currentPage = 1;
            fetchUsers();
    }}
    >
    <option value="5">5</option>
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="50">50</option>
</select>
</div>

<input type="text" placeholder="Search users..." bind:value={userSearchText} oninput={search}/>

<div class="pagination">
    <button onclick={prevPage} disabled={currentPage === 1}>Prev</button>
    <ul class="pagination-numbers">
    {#each Array(totalPages).fill(0) as _, i}
        <li>
            <a href="#top" onclick={(e) => goToPage(e, i + 1)} class:selected={currentPage === i + 1}>{i+1}</a>
        </li>
    {/each}
</ul>
    <button onclick={nextPage} disabled={currentPage === totalPages}>Next</button>

</div>

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
