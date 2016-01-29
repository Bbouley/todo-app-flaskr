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

});
