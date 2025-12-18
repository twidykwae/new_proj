<script>
    import Sidebar from "../src/lib/components/sidebar.svelte";
    import UserList from "../src/lib/components/UserList.svelte";
    import LostItemsList from "../src/lib/components/LostItemsList.svelte";
    import PrayerRequests from "../src/lib/components/PrayerRequests.svelte";

    let activeSection = 'dashboard';

    function setPage(page) {
        activeSection = page;
    }
</script>

<div class="wrapper">
    <Sidebar {activeSection} {setPage} />

    <div class="content">
        <h1>Admin Dashboard</h1>

        {#if activeSection === 'dashboard'}
            <h2>Dashboard</h2>
            <p>Welcome to the admin dashboard.</p>

        {:else if activeSection === 'users'}
            <h2>User Management</h2>
            <UserList />

        {:else if activeSection === 'lostitems'}
            <h2>Lost and Found</h2>
            <LostItemsList />

        {:else if activeSection === 'prayerrequests'}
            <h2>Prayer Requests</h2>
            <PrayerRequests />
        {/if}
    </div>
</div>
