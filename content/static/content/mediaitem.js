django.jQuery(function(){

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


    django.jQuery('#id_file').on('change', function () {
        var file_name = django.jQuery(this).val().replace(/^.*\\/, "");;
        django.jQuery('.vTextField').each(function(index){
            django.jQuery(this).val(URLify(file_name));
        })
    });
});
