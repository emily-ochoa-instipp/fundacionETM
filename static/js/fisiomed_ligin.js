// Asegúrate de que el DOM esté completamente cargado antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    // Solo procede si el formulario existe en la página
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            // Evita que el formulario se envíe de la manera tradicional
            event.preventDefault();

            const emailInput = document.getElementById('inputEmail');
            const passwordInput = document.getElementById('inputPassword');

            // Limpia los estados de validación anteriores (clases is-invalid)
            emailInput.classList.remove('is-invalid');
            passwordInput.classList.remove('is-invalid');

            let isValid = true; // Bandera para controlar la validez

            // Validar campo de Email
            if (emailInput.value.trim() === '') {
                emailInput.classList.add('is-invalid');
                alert('Por favor, ingresa tu correo electrónico.'); // Alerta simple
                isValid = false;
            }

            // Validar campo de Contraseña
            if (passwordInput.value.trim() === '') {
                passwordInput.classList.add('is-invalid');
                alert('Por favor, ingresa tu contraseña.'); // Alerta simple
                isValid = false;
            }

            // Si ambos campos son válidos, procede con la redirección
            if (isValid) {
                // Aquí usamos la variable global INDEX_URL que Django generó en el HTML
                window.location.href = INDEX_URL;
            }
        });

        // Event listeners para eliminar la clase 'is-invalid' cuando el usuario escribe
        document.getElementById('inputEmail').addEventListener('input', function() {
            this.classList.remove('is-invalid');
        });
        document.getElementById('inputPassword').addEventListener('input', function() {
            this.classList.remove('is-invalid');
        });
    }
});