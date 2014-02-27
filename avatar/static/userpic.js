var upload_to = upload_to;
var csrftoken = csrftoken;




// set option as default for all modals opened
//В случае закрытия модального окна возвращаем старый рисунок
$.modal({
	closeOnEsc: true,
	onClose: function(el, options) {
		//Заменяем рисунок		
		$("#userpic__preview").html("");
		//ms = new Date().getMilliseconds();
		//url = avatar_url + "?" + ms;
		//$(".userpic").css("background-image", 'url("' + url + '")');

	},
});



$('#userpic').fileapi({
	url: upload_to,
	accept: 'image/*',
	data: {"csrfmiddlewaretoken": csrftoken}, // дополнительный POST-параметры
	//name: 'avatar', // название POST-параметра загружаемого файла
	//imageSize: { minWidth: 200, minHeight: 200, maxWidth: 3840, maxHeight: 2160 },
	multiple: false,
	duplicate: true,
	
	elements: {
		active: { show: '.js-upload', hide: '.js-browse' },
		preview: {
			el: '.js-preview',
			width: 200,
			height: 200
		},
		progress: '.js-progress'
	},
	filterFn: function (file, info){ 
		//console.log(info.width);
		//console.log(info.height);
		
		if (info.width < 200 || info.height < 200) {
			alert("Выберите изображение размером не меньше 200x200");
			return false;
		}
		if (info.width > 3840 || info.height > 2160) {
			alert("Выберите изображение размером не больше 3840x2160");
			return false;
		}
		
		//return /^image/.test(file.type) && info.width > 320;
		return /^image/.test(file.type);
		
	},
	
	
	onSelect: function (evt, ui){
		var file = ui.files[0];
		

		if( file ){
			$('#popup').modal({
				closeOnEsc: true,
				closeOnOverlayClick: false,
				onOpen: function (overlay){
					$(overlay).on('click', '.js-upload', function (){
						$.modal().close();
						$('#userpic').fileapi('upload');
					});

					$('.js-img', overlay).cropper({
						file: file,
						bgColor: '#fff',
						size: '200px',
						maxSize: [$(window).width()-100, $(window).height()-100],
						minSize: [200, 200],
						//selection: '90%',
						aspectRatio: 1, //квадрат
						//setSelect:   [ 100, 100, 50, 50 ],
						onSelect: function (coords){
							$('#userpic').fileapi('crop', file, coords);
						}
					});
					

				},
			}).open();
			

		}
		
	},
	onComplete: function(evt, uiEvt){
	    var error = uiEvt.error;
	    var result = uiEvt.result; // server response

	    
	    if (result.status == "error") {
	    	alert(result.err_message);
	    }
	    else if(result.status == "success") {
			avatar_url = result.avatar_url;
			//Заменяем рисунок
			$("#userpic__preview").html("");
			ms = new Date().getMilliseconds();
			url = avatar_url + "?" + ms;
			$(".userpic").css("background-image", 'url("' + url + '")');
		}
		
	}
	
	
	
	
});



//Заменяем рисунок
//$("#userpic__preview").html("");
ms = new Date().getMilliseconds();
url = avatar_url + "?" + ms;
$(".userpic").css("background-image", 'url("' + url + '")');





