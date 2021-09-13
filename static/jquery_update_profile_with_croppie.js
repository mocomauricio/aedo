      const $form = document.querySelector('#editProfileForm');
      const $urlProfilePhoto = '/static/profile.jpg'

      var resize = $('#previewImg').croppie({
          enableExif: true,
          enableOrientation: true,    
          viewport: { // Default { width: 100, height: 100, type: 'square' } 
              width: 200,
              height: 200,
              type: 'square' //square
          },
          boundary: {
              width: 200,
              height: 200
          }
      });

      resize.croppie('bind', {
          url: '{{ user.photo.url }}',
      });

      $('#photo').on('change', function () { 
          var reader = new FileReader();
          reader.onload = function (e) {
              resize.croppie('bind',{
                  url: e.target.result
              }).then(function(){
                  console.log('jQuery bind complete');
              });
          }
          reader.readAsDataURL(this.files[0]);
      });

      $form.addEventListener('submit',(e) => {
          e.preventDefault();

          resize.croppie('result', {
              type: 'blob',
              size: 'viewport'
          }).then(function (img) {
              let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
              let formData = new FormData($form);

              if(formData.get('photo').name === "") { formData.delete('photo'); }
              else { formData.set('photo', img, 'imagen.jpg'); }

              fetch('/api/usuarios/{{user.id}}/',{
                  method:'PUT',
                  headers:{"X-CSRFToken": $crf_token},
                  body:formData
              })
              .then(data => {
                  $alert.innerHTML = `
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                      ¡Su perfil se actualizó con éxito!
                      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                  `
                  $('#editarPerfilModal').modal('hide');
                  console.log(data);
              }).catch(function(error) {
                  $alert.innerHTML = `
                    <div class="alert alert-danger alert-dismissible fade show" role="alert">
                      ¡Ocurrió un error! Su perfil no se actualizó
                      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                  `
                  alert('Apodo y email deben ser únicos');
                  $('#editarPerfilModal').modal('hide');
              });
          });
      });