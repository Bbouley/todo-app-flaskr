$(document).on('ready', function() {
    // console.log('sanity check')
    $(document).on('click', '.delete', function(e) {
        var $db_id = $(this).parent().attr('id')
        var $this = $(this)
        $.ajax({
            url: '/delete/' + $db_id,
            method: 'GET',
            success: function(result) {
                if(result.status === 1) {
                    $this.parent().remove()
                }
            }
        });
    });

    $(document).on('click', '.edit', function() {
        var thisEl = $(this)
        var $db_id = thisEl.parent().attr('id')
        var element = '<input type="text" id="' + $db_id + '" required></input>'
        var buttonElement = '&lt;<button class="sendEdit">Edit</button>'
        thisEl.parent().append(element);
        thisEl.parent().append(buttonElement);
        thisEl.hide()
    });

    $(document).on('click', '.sendEdit', function() {
        var thisEl = $(this)
        var edit = {
            data: thisEl.prev().val()
        }
        var $db_id = thisEl.parent().attr('id')
        $.ajax({
            url: '/edit/' + $db_id,
            contentType: 'application/json',
            method: 'POST',
            data: JSON.stringify(edit),
            datatype: 'json',
            success: function(result) {
                window.location.reload();
            }
        });
    });

});
