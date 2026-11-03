const API_URL = "http://127.0.0.1:8000/api/auth/";

const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");

if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const message = document.getElementById("message");
        try {
            const response = await fetch(`${API_URL}token/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    username: document.getElementById("username").value,
                    password: document.getElementById("password").value
                })
            });
            const data = await response.json();
            if (!response.ok) {
                message.innerHTML = '<div class="alert alert-danger">Invalid username or password.</div>';
                return;
            }
            sessionStorage.setItem("access", data.access);
            sessionStorage.setItem("refresh", data.refresh);
            window.location.href = "dashboard.html";
        } catch (error) {
            message.innerHTML = '<div class="alert alert-danger">Unable to connect to the server.</div>';
        }
    });
}

if (registerForm) {
    registerForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const message = document.getElementById("message");
        try {
            const response = await fetch(`${API_URL}register/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    username: document.getElementById("username").value,
                    email: document.getElementById("email").value,
                    password: document.getElementById("password").value
                })
            });
            const data = await response.json();
            if (!response.ok) {
                message.innerHTML = `<div class="alert alert-danger">${Object.values(data).flat().join("<br>")}</div>`;
                return;
            }
            message.innerHTML = '<div class="alert alert-success">Registration successful! Redirecting to login...</div>';
            setTimeout(() => window.location.href = "login.html", 1000);
        } catch (error) {
            message.innerHTML = '<div class="alert alert-danger">Unable to connect to the server.</div>';
        }
    });
}