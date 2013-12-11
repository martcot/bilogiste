function columnsEqualHeight(className, eachX)
{
	var col = 1; var i = 1; var ic = 1;
	$('.'+className).each(function(){
		$(this).addClass(className+'-col-'+col);
		if(ic==eachX){ ic=1; col++; }
		else{ ic++; } i++;
	});
	for(i=1;i<=col;i++){ $("."+className+'-col-'+i).equalHeights(); }
}

var QueryParameters = (function()
{
    var result = {};

    if (window.location.search)
    {
        // split up the query string and store in an associative array
        var params = window.location.search.slice(1).split("&");
        for (var i = 0; i < params.length; i++)
        {
            var tmp = params[i].split("=");
            result[tmp[0]] = unescape(tmp[1]);
        }
    }

    return result;
}());