$.validator.setDefaults({
	submitHandler: function() { alert("submitted!"); }
});

$().ready(function() {
	
	$('.btn-add-rules-row').live("click", null, addRule);
	$('.btn-rm-rules-row').live("click", null, rmRule);
		
	/* Handle rule list + and - buttons */
	function addRule(event) {
		$('.rules-list').append($($('.rules-list .rule')[0]).clone());
		return false;
	};
	function rmRule(event) {
		if ($('.rules-list').children().length > 1) {
			$(event.target.parentNode).remove()
		}
		return false;
	};



});