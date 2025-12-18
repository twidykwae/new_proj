<script lang="ts">
    async function registerUser(event) {
        event.preventDefault();
        const form = event.target;
        const username = form.username.value;
        const password = form.password.value;
        const email = form.email.value;
        const major = form.major.value;
        const graduation_year = form.graduation_year.value;

        const response = await fetch('http://localhost:8000/api/v1/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: username,
                password: password,
                email: email,
                major: major,
                graduation_year: graduation_year
            })
        });

        if (response.ok) {
            alert('Registration successful! Please log in.');
            window.location.href = '#/login';
        } else {
            alert('Failed to register user.');
        }
        
    }
</script>
<div class="register-form">
<h2>Register</h2>
<form on:submit={registerUser}>
    <div>
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required />
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required />
    </div>
        <div>
        <label for="major">Major:</label>
        <input type="text" id="major" name="major" required />
    </div>
        <div>
        <label for="graduation_year">Graduation Year:</label>
        <input type="text" id="graduation_year" name="graduation_year" required />
    </div>
        <div>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required />
    </div>
    <button type="submit" class="submit-button">Sign Up</button>
    <p>Already have an account? <a href="#/login">Log in</a></p>
</form>
</div>