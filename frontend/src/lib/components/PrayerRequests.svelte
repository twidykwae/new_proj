<script lang="ts">
    import { onMount } from "svelte";
    let loading = $state(false);
    let error = $state(null);
    let prayerRequests= $state<any[]>([]);
    let totalPrayerRequests = $state(0);
    let currentPage = $state(1);
    let selectedResults = $state("10");
    let perPageResults = $derived(parseInt(selectedResults));
    let totalPages = $derived(totalPrayerRequests > 0 ? Math.ceil(totalPrayerRequests / perPageResults) : 10);
    let prayerRequestSearchText = $state("");

    onMount(() => {
        fetchPrayerRequests();
    });

    async function fetchPrayerRequests(){
        loading = true;
        error = null;

        try{
            const response = await fetch(`http://127.0.0.1:8000/api/v1/prayer-requests?curPage=${currentPage}&pageSize=${perPageResults}&searchText=${prayerRequestSearchText}`);
            if(!response.ok){
                throw new Error('Failed to fetch prayer requests');
            }  
            const data = await response.json();
            totalPrayerRequests = data.total ? parseInt(data.total) : 0;
            prayerRequests = data.prayers;
        }catch(err){
            error = err.message;
        }finally{
            loading = false;
        }
    }

    async function deletePrayerRequest(request_id){
        if(confirm('Are you sure you want to delete this prayer request?')){
            try{
                const response = await fetch(`http://127.0.0.1:8000/api/v1/prayer-requests/${request_id}`, {
                    method: 'DELETE'
                });
                if(!response.ok){
                    throw new Error('Failed to delete prayer request');
                }
                await fetchPrayerRequests();
            }catch(err){
                error = err.message;
            }
        }
    }   
    async function goToPage(event: MouseEvent, page: number){
        event.preventDefault();
        currentPage = page;
        await fetchPrayerRequests();
    }
    async function prevPage(event: MouseEvent){
        event.preventDefault();
        if(currentPage > 1){
            currentPage -= 1;
            await fetchPrayerRequests();
        }
    }
    async function nextPage(event: MouseEvent){
        event.preventDefault();
        if(currentPage < totalPages){
            currentPage += 1;
            await fetchPrayerRequests();
        }
    }
    async function searchPrayerRequests(){
        currentPage = 1;
        await fetchPrayerRequests();
    }

</script>

<h1> Prayer Requests </h1>
{#if loading}
    <p>Loading prayer requests...</p>
{:else if error}
    <p class="error">Error: {error}</p>
{:else}
<div class="results-per-page">
        Results per page:
        <select bind:value={selectedResults} 
            onchange={() => {
                currentPage = 1;
                fetchPrayerRequests();
            }}>
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="25">25</option>
            <option value="50">50</option>
        </select>
    </div>
    <div>
        <input type="text" placeholder="Search Prayer Requests" bind:value={prayerRequestSearchText} />
        <button onclick={searchPrayerRequests}>Search</button>
    </div>
    <div class="request-list">
        <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Request</th>
                <th>Date Submitted</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {#each prayerRequests as request}
                <tr>
                    <td>{request.id}</td>
                    <td>{request.prayer_request}</td>
                    <td>{new Date(request.created_at).toLocaleDateString()}</td>
                    <td>
                        <button onclick={() => deletePrayerRequest(request.id)}>Delete</button>
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
    </div>

    <div class="pagination">
        <button onclick={prevPage} disabled={currentPage === 1}>Prev</button>
        <ul class="pagination-numbers">
            {#each Array(totalPages).fill(0) as _, i}
                <li>
                    <a href="#top" onclick={(e) => goToPage(e, i + 1)} class:selected={currentPage === i + 1}>{i + 1}</a>
                </li>
            {/each}
        </ul>
        <button onclick={nextPage} disabled={currentPage === totalPages}>Next</button>
    </div>
{/if}