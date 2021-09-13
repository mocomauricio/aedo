window.onload = () => {
    const $form = document.querySelector('#profileForm');
    const $image = document.querySelector('#previewImg');
    const $file = document.querySelector('#photo');
    const $csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    console.log($csrf_token);
    
    var vanilla = new Croppie($image, {
        enableExif: true,
        enableOrientation: true,

        viewport: { 
          width: 200, 
          height: 200 
        },

        boundary: { 
          width: 200, 
          height: 200 
        }
    });

    vanilla.bind({
        url: '{{ user.photo.url }}'
    });

    $file.addEventListener('change', () => {
        const formData = new FormData($form)
        const file = formData.get('photo');
        const image = URL.createObjectURL(file);
        //$image.setAttribute('src',image);

        vanilla.bind({
            url: image
        });

    });

    $form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData($form);

        vanilla.result('blob')
        .then(function(img) {

            if(formData.get('photo').name === "") { formData.delete('photo'); }
            else { formData.set('photo', img, 'imagen.jpg'); }

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
    });
}