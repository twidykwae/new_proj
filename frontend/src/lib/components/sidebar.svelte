<script lang="ts">
    export let activeSection;
    export let setPage;
</script>

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
