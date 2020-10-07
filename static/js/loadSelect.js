console.log("funciona")

$(document).on('ready', function(){
    $('#items_0_marca').on('change', function(){
        $.ajax({
            url: '/',
            type: $(this).attr('GET'),
            data: $(this).serialize(),
            succes: function(data){
                console.log("aca",data);
            }
        });
    });
    return false
});

// axios.post('/ventas/venta/add', {
//     imtems_0_marca: 1,
//     })
//   .then(function (response) {
//     // Acá cambias el select y lo rellenas con lo que te vino del back
//     console.log(response)
//   })
//   .catch(function (error) {
//     // acá salió todo mal asi que no sé como queres manejarlo
//   });

//hacer llamada ajax y pasar valor del primer select cuando hace onchange

//views hacer que devuelva un json y cuando termine el ajax, limpiar el select segundo y agregar opciones que me da el json