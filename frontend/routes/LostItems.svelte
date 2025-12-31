<script lang="ts">
    import LostItemsList from "../src/lib/components/LostItemsList.svelte";

    async function addLostItem(event) {
        event.preventDefault();
        const form = event.target;
        const title = form.title.value;
        const description = form.description.value;
        const location = form.location.value;
        const contact_info = form.contact_info.value;
        const category = form.category.value;
        const image_url = form.image_url.value;

        const response = await fetch('http://localhost:8000/api/v1/lost-items/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title,
                description,
                location_found: location,
                contact: contact_info,
                category: category,
                image_url: image_url})

        });

        if (response.ok) {
            alert('Lost item added successfully!');
            form.reset();
            window.location.reload();
        } else {
            alert('Failed to add lost item.');
        }
        
    }
</script>
<div class="add-lost-item">
    <h2>Add Lost Item</h2>
    <form on:submit={addLostItem}>
        <label for="title">Name of Item:</label>
        <input type="text" id="title" name="title" required />
        <label for="description">Description:</label>
        <input type="text" id="description" name="description" required />
        <label for="category">Category:</label>
        <input type="text" id="category" name="category" required />
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url" required />
        <label for="location">Location:</label>
        <input type="text" id="location" name="location" required />
        <label for="contact_info">Contact Info:</label>
        <input type="text" id="contact_info" name="contact_info" required />
        <label for="date_found">Date Found:</label>
        <input type="date" id="date_found" name="date_found" required />
        <button type="submit">Add Lost Item</button>
    </form>
</div>

<div class="lost-items-list">
<LostItemsList />
</div>

