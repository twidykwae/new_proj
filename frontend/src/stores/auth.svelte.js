export function createAuthStore() {
    let isAuthenticated = $state(false);
    let user = $state(null);
    let email = $state(null);
    let isAdmin = $state(false);

    function init(){
        const token = localStorage.getItem('access_token');
        const userData = localStorage.getItem('user');

        if (token && userData){
            isAuthenticated = true;
            user = userData ? JSON.parse(userData) : null; 
            isAdmin = user.is_admin; 
        }
    }

    async function login(token) {
        localStorage.setItem('access_token', token);
        isAuthenticated = true;

        // ⬇ Fetch user data from /users/me
        const response = await fetch('http://localhost:8000/api/v1/users/me', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        const userData = await response.json();
        localStorage.setItem('user', JSON.stringify(userData));
        user = userData;
        isAdmin = userData.is_admin;
}
    

    function logout() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('user');
        isAuthenticated = false;
        user = null;
        }

    function getToken() {
        return localStorage.getItem('access_token');
    }

    init();
    return {
        get isAuthenticated() { return isAuthenticated; },
        get user() { return user; },
        get accessToken() { return localStorage.getItem('access_token'); }
    , login, logout, getToken, isAdmin: () => isAdmin
    
    }
}

export const authStore = createAuthStore();