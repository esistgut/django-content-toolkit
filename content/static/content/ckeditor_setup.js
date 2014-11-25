django.jQuery(function(){
    config = {
        toolbar: [
            [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ], [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
            [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
            '/',
            [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ],
            [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'language' ],
            [ 'Link', 'Unlink', 'Anchor' ], [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            [ 'Styles', 'Format', 'FontSize' ], [ 'TextColor', 'BGColor' ], [ 'Maximize', 'ShowBlocks' ], [ '-' ],
        ],


        'filebrowserBrowseUrl': '/admin/content/mediaitem/?_popup=1',
        'width': 758,
        'height': 400,
        allowedContent: true
    };

    django.jQuery('textarea').each(function(index){
        CKEDITOR.replace((this), config);
    })
    
    
    function getUrlParam( paramName ) {
        var reParam = new RegExp( '(?:[\?&]|&)' + paramName + '=([^&]+)', 'i' ) ;
        var match = window.location.search.match(reParam) ;

        return ( match && match.length > 1 ) ? match[ 1 ] : null ;
    }

    if (getUrlParam( 'CKEditorFuncNum' )) {
        document.cookie='CKEditorFuncNum=' + getUrlParam( 'CKEditorFuncNum' );
    }
    
    django.jQuery('.cklink').on('click', function () {
        var funcNum = getUrlParam( 'CKEditorFuncNum' );
        var fileUrl = django.jQuery(this).attr('href');
        window.opener.CKEDITOR.tools.callFunction( funcNum, fileUrl );
        window.close()
    });

});


