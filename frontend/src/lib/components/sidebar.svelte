<script lang="ts">
    export let activeSection;
    export let setPage;
</script>

<style>
    .sidebar {
        width: 240px;
        background: #1e293b;
        color: white;
        min-height: 100vh;
        padding: 20px;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    button {
        background: transparent;
        border: none;
        color: #e2e8f0;
        text-align: left;
        padding: 10px;
        font-size: 1rem;
        cursor: pointer;
        border-radius: 6px;
    }

    button:hover,
    button.active {
        background: #334155;
        color: white;
    }
</style>

<div class="sidebar">
    <button
        class:active={activeSection === 'dashboard'}
        on:click={() => setPage('dashboard')}
    >Dashboard</button>

    <button
        class:active={activeSection === 'users'}
        on:click={() => setPage('users')}
    >User Management</button>

    <button
        class:active={activeSection === 'lostitems'}
        on:click={() => setPage('lostitems')}
    >Lost & Found</button>

    <button
        class:active={activeSection === 'prayerrequests'}
        on:click={() => setPage('prayerrequests')}
    >Prayer Requests</button>
</div>
