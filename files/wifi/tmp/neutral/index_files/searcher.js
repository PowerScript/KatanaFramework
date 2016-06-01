(function($){
  $.fn.searcher=function(options){
    var defaults = {
			fieldText : 'Buscar...',
      fieldSelector : 'input.text',
      msgResults : 'Resultados encontrados',
      msgCategories : 'Buscar categorias',
      msgNoResults : 'No se encontraron resultados',
      msgMoreResults : 'Mas resultados',
      url : 'index.php?option=com_search&tmpl=raw&type=json&ordering=&searchphrase=all'
		};
		var options = $.extend(defaults, options);
    var container=$(this);
    
    var resultados=null;
    var loader=container.find('img.loader');
    loader.css('display','none');
    var icon=container.find('img.buscador');
    
    var field = container.find(options.fieldSelector);
    field.val(options.fieldText);

    var sections = new Array();
    var focussed = false;
    var selection = false;
    var ajax=null;
    $(document).on('click',function(e){
    	var target=$(e.target);
    	if(!target.parents().hasClass('resultados')){
    		if(resultados && resultados.css('display')=='block')clearSearch();
    	}
    });
    field.attr('autocomplete', 'off');
    field.on('keyup',function(){
      if(field.val().length<3) return;
      else processSearch();
    });
    function showLoader(display){
    	loader.css('display',display?'block':'none');
    	icon.css('display',display?'none':'block');
		}
		function clearSearch() {
			if(field.val()=='') field.val(options.fieldText);
			try{
				resultados.fadeOut(200,function(){
					resultados.empty();
				});
			}catch(E){}
		}
    function processSearch() {
			if (field.val()) {
				var url = options.url;
        try{ajax.abort();}catch(e){}
        showLoader(true);
				ajax=$.ajax(url, {
					type: 'post',
					data: 'searchword=' + field.val(),
					success : function(data){
            processResults(data);
          }
				});
			}
		}
    function processResults(data) {
    	showLoader(false);
			if (data) {
        if(!$('#resultados').length){
        	resultados=$('<div id="resultados" class="resultados" />');
        	container.append(resultados);
        	resultados.css({'opacity':0});
        }
        resultados.empty();
        resultados.html(data);
        resultados.fadeTo(300,1);
        resultados.find('a').on('click',clearSearch);
			}
		}
  };
})(jQuery);