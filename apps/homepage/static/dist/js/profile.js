$(window).on("load", function() {
    var Toast = Swal.mixin({
		toast: true,
		position: 'top-end',
		showConfirmButton: false,
		timer: 3000
    });

    /*************************************
     * 
     * javascript para cambiar contraseñas
     *
     ************************************/

    $("#changePasswordForm").submit( function(e) {
        e.preventDefault();

        const $form = $('#changePasswordForm');
        const $csrf_token = $('[name="csrfmiddlewaretoken"]').val();
        const old_password = $('#old_password').val();
        const new_password = $('#new_password').val();
        const confirm_password = $('#confirm_password').val();

        if (!(new_password === confirm_password)){
          Toast.fire({
            icon: 'error',
            title: 'Las contraseñas no coinciden'
          })
          return ;
        }

        $.ajax({
            url: '/api/change-password/',
            method:'PUT',
            headers:{
                "X-CSRFToken": $csrf_token
            },
            data: $form.serialize(),
        })
        .done(function(response){
          Toast.fire({
            icon: 'success',
            title: 'Su contraseña fue actualizada'
          })
          $('#ChangePasswordModal').modal('hide')
        })
        .fail(function(xhr, status, error) {
          Toast.fire({
            icon: 'error',
            title: 'La contraseña actual es incorrecta'
          })
        });
    });



    /*************************************
     * 
     * javascript para actualizar perfil
     *
     ************************************/
    
    var vanilla = new Croppie( document.querySelector('#previewImg'), {
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
        url: $('#user_profile_photo').attr('src')
    });

    $("#photo").change( function() {
        const form = document.querySelector('#editProfileForm');
        const formData = new FormData(form)
        const file = formData.get('photo');
        const image = URL.createObjectURL(file);
        //$image.setAttribute('src',image);

        vanilla.bind({
            url: image
        });

    });

    $("#editProfileForm").submit( function(e) {
        e.preventDefault();

        const $form = document.querySelector('#editProfileForm');
        const $image = document.querySelector('#previewImg');
        const $file = document.querySelector('#photo');
        const $csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
        const formData = new FormData($form);

        vanilla.result('blob')
        .then(function(img) {

            if(formData.get('photo').name === "") { formData.delete('photo'); }
            else { formData.set('photo', img, 'imagen.jpg'); }

            $.ajax({
                //url: '/api/users/{{user.id}}/',
                url: '/api/update-profile/',
                method:'PUT',
                headers:{
                    "X-CSRFToken": $csrf_token
                },
                data: formData,
                processData: false,
                contentType: false
            })
            .done(function(response){
              console.log(response);

              $('#user_profile_photo').attr('src', response.photo);
              $('#user_profile_name').text(response.short_name);

              Toast.fire({
                icon: 'success',
                title: 'Su perfil fue actualizado'
              })
              $('#EditProfileModal').modal('hide')
            })
            .fail(function(xhr, status, error) {
              Toast.fire({
                icon: 'error',
                title: 'Ya existe una cuenta con ese correo electrónico'
              })
            });

        });
    });
});