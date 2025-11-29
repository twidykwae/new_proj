<script lang="ts">
    import PrayerRequests from "../src/lib/components/PrayerRequests.svelte";

    async function addPrayerRequest(event) {
        event.preventDefault();
        const form = event.target;
        const title = form.title.value;
        const prayer_request = form.request.value;
        const posted_by = form.name.value;

        const response = await fetch('http://localhost:8000/api/v1/prayer-requests/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title,
                prayer_request,
                posted_by
            })
        });

        if (response.ok) {
            alert('Prayer request added successfully!');
            form.reset();
            window.location.reload();
        } else {
            alert('Failed to add prayer request.');
        }
        
    }
</script>
<div class="add-prayer-request">
    <h2>Add Prayer Request</h2>
    <form on:submit={addPrayerRequest}>
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required />
        <label for="request">Prayer Request:</label>
        <input type="text" id="request" name="request" required />
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required />
        <button type="submit">Add Prayer Request</button>
    </form>
</div>
<PrayerRequests />