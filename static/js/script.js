$(document).ready(function() {
    $('.toggle-switch input').change(function() {
        var isChecked = $(this).prop('checked') ? true : false;
        
        var toggleId = $(this).attr('id');
        
        $.ajax({
            url: '/update_toggle',
            type: 'POST',
            data: { id: toggleId, status: isChecked },
            success: function(response) {
                console.log(response);
                for(i = 0; i < 8; i++) {
                $(`#displaytoggle${Number(i)}`).prop('checked', response[1][i]);
                }
                $(`#overbufferedtoggle`).prop('checked', response[0]);
            },
            error: function(xhr, status, error) {
                console.error('Request failed with status: ' + xhr.status);
            }
        });
    });
});