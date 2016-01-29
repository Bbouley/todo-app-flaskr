$(document).on('ready', function() {
    // console.log('sanity check')
    $(document).on('click', '.delete', function(e) {
        e.preventDefault()
        var $db_id = $(this).parent().attr('class')
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

    $(document).on('click', '.edit', function(e) {
        e.preventDefault();
        var thisEl = $(this)
        var $db_id = thisEl.parent().attr('class')
        var element = '<input type="text" id="' + $db_id + '" required>&nbsp;'
        var buttonElement = '<button class="sendEdit" id="send'+ $db_id +'">Edit</button>'
        thisEl.parent().append(element);
        thisEl.parent().append(buttonElement);
        thisEl.hide()
    });

    $(document).on('click', '.sendEdit', function(e) {
        e.preventDefault();
        var thisEl = $(this)
        var formVal = thisEl.prev().val()
        if (formVal.length === 0) {
            thisEl.addClass('warning');
        } else {
            var edit = {
                data: thisEl.prev().val()
            }
            var $db_id = thisEl.parent().attr('class')
            console.log($db_id)
            $.ajax({
                url: '/edit/' + $db_id,
                contentType: 'application/json',
                method: 'POST',
                data: JSON.stringify(edit),
                datatype: 'json',
                success: function(result) {
                    if (result.status === 1) {
                        $('#send' + $db_id + '').hide();
                        $('#' + $db_id + '').hide();
                        $('.edit').show();
                        window.location.replace("/");
                    } else {
                        //error handler
                    }
                }
            });
        }
    });

});
