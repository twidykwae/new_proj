<script lang="ts">
    import {onMount} from 'svelte';
    let loading = $state(false);
    let error = $state(null);
    let lostItems = $state<any[]>([]);
    let totalLostItems = $state(0);
    let currentPage = $state(1);
    let selectedResults = $state("10");
    let perPageResults = $derived(parseInt(selectedResults));
    let totalPages = $derived(totalLostItems > 0 ? Math.ceil(totalLostItems / perPageResults) : 10);
    let lostItemSearchText = $state("");

    onMount(() => {
        fetchLostItems();
    });

    async function fetchLostItems(){
        loading = true;
        error = null;

        try{
            const response = await fetch(`http://127.0.0.1:8000/api/v1/lost-items?curPage=${currentPage}&pageSize=${perPageResults}&searchText=${lostItemSearchText}`);
            if(!response.ok){
                throw new Error('Failed to fetch lost items');
            }
            const data = await response.json();
            totalLostItems = data.total ? parseInt(data.total) : 0;
            lostItems = data.items;
        }catch(err){
            error = err.message;
        }finally{
            loading = false;
        }
    }

    async function goToPage(event: MouseEvent, page: number){
        event.preventDefault();
        currentPage = page;
        await fetchLostItems();
    }

    async function deleteLostItem(item_id){
        if(confirm('Are you sure you want to delete this lost item?')){
            try{
                const response = await fetch(`http://127.0.0.1:8000/api/v1/lost-items/${item_id}`, {
                    method: 'DELETE'
                });
                if(!response.ok){
                    throw new Error('Failed to delete lost item');
                }
            }catch(error: unknown){
                error = (error as Error).message;
            }finally{
                fetchLostItems();
            }
        }
    }

    async function searchLostItems(){
        currentPage = 1;
        await fetchLostItems();
    }

    async function nextPage(event: MouseEvent){
        event.preventDefault();
        if(currentPage < totalPages){
            currentPage += 1;
            await fetchLostItems();
        }
    }

    async function prevPage(event: MouseEvent){
        event.preventDefault();
        if (currentPage > 1) {
            currentPage -= 1;
            await fetchLostItems();
        }
    }

</script>

<h1>Lost Items</h1>
{#if error}
    <p class="error">{error}</p>
{:else}
    <div class="controls">
        <label for="resultsPerPage">Results per page:</label>
        <select id="resultsPerPage" bind:value={selectedResults} onchange={fetchLostItems}>
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="25">25</option>
            <option value="50">50</option>
        </select>

        <input type="text" placeholder="Search lost items..." bind:value={lostItemSearchText} />
        <button onclick={searchLostItems}>Search</button>
    </div>

    {#if loading}
        <p>Loading lost items...</p>
    {:else}
    <div class="lost-items-list">
        {#if lostItems.length === 0}
            <p>No lost items found.</p>
        {:else}
        <table>
            <thead>
                <tr>
                    <th>Name of Item</th>
                    <th>Description</th>
                    <th>Location</th>
                    <th>Contact</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {#each lostItems as item}
                    <tr>
                        <td>{item.title}</td>
                        <td>{item.description}</td>
                        <td>{item.location_found}</td>
                        <td>{item.contact}</td>
                        <td>
                            <button onclick={() => deleteLostItem(item.id)}>Delete</button>
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
        {/if}
    </div>

        <div class="pagination">
            <button onclick={prevPage} disabled={currentPage === 1}>Previous</button>
            <span>Page {currentPage} of {totalPages}</span>
            <button onclick={nextPage} disabled={currentPage === totalPages}>Next</button>
        </div>
    {/if}
{/if}