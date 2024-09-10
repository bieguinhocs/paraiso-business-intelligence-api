// dynamic_brand_line.js
document.addEventListener('DOMContentLoaded', function () {
    const brandSelect = document.getElementById('id_brand');
    const lineSelect = document.getElementById('id_line');

    // Escuchar el cambio en la selección de brand
    brandSelect.addEventListener('change', function () {
        const brandId = this.value;
        
        if (brandId) {
            // Realizar una solicitud AJAX para obtener las líneas relacionadas a la marca seleccionada
            $.ajax({
                url: '/api/products/ajax/load-lines/',  // URL de la vista que devuelve las líneas
                data: {
                    'brand': brandId  // Parámetro de marca seleccionado
                },
                success: function (data) {
                    // Limpiar las opciones actuales del selector de línea
                    lineSelect.innerHTML = '<option value="" selected></option>';

                    // Añadir las nuevas opciones obtenidas por AJAX
                    data.forEach(function (line) {
                        const option = document.createElement('option');
                        option.value = line.id;
                        option.textContent = line.name;
                        lineSelect.appendChild(option);
                    });
                },
                error: function (xhr, status, error) {
                    console.error('Error al cargar las líneas:', error);
                }
            });
        } else {
            // Si no hay ninguna marca seleccionada, reiniciar el selector de líneas
            lineSelect.innerHTML = '<option value="" selected></option>';
        }
    });
});
