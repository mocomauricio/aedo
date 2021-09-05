/*
    actualizar foto de perfil de usuario sin croppie 
    en jquery
*/

$(window).on("load", function() {
    const $form = $('#profileForm');
    const $image = $('#previewImg');
    const $csrf_token = $('[name="csrfmiddlewaretoken"]').val();

    console.log($csrf_token);

    $("#photo").change( function() {
        const formData = new FormData( $form[0] )
        const file = formData.get('photo');
        const image = URL.createObjectURL(file);
        $image.attr('src', image);
    });
    
    $("#profileForm").submit( function(e) {
        e.preventDefault();
        const formData = new FormData( $form[0] )
        $.ajax({
            url: '/api/usuarios/{{user.id}}/',
            method:'PUT',
            headers:{
                "X-CSRFToken": $csrf_token
            },
            data: formData,
            processData: false,
            contentType: false
        })
        .done(function(response){
            console.log('Success:', response);
        })
        .fail(function(xhr, status, error) {
            console.error('Error:', error);
        });

    });
});