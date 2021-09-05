/*
  actualizar foto de perfil de usuario sin croppie 
  en vanilla javascript
*/

window.onload = () => {
    const $form = document.querySelector('#profileForm');
    const $image = document.querySelector('#previewImg');
    const $file = document.querySelector('#photo');
    const $csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    console.log($csrf_token);

    $file.addEventListener('change', () => {
        const formData = new FormData($form)
        const file = formData.get('photo');
        const image = URL.createObjectURL(file);
        $image.setAttribute('src',image);
    });

    $form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData($form);
        fetch('/api/usuarios/{{user.id}}/',{
            method:'PUT',
            headers: {
                "X-CSRFToken": $csrf_token
            },
            body:formData
        })
        .then(response => response.json())
        .then(response => console.log('Success:', response))
        .catch(error => console.error('Error:', error));
    });
}