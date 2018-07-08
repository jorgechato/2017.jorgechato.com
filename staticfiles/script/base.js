document.onreadystatechange = () => {
	var searchBtnOpen = document.getElementById('btn-search-open')
	var searchForm = document.getElementById('form-search')
	var searchBtnClose = document.getElementById('btn-search-close')

	searchBtnOpen.onclick = () => {
		searchForm.style.display = "block";
	}

	searchBtnClose.onclick = () => {
		searchForm.style.display = "none";
	}
}
