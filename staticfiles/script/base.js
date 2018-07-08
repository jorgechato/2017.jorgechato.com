document.onreadystatechange = () => {
	var searchBtn = document.getElementById('btn-search')
	var searchForm = document.querySelector('.form-search')

	searchForm.style.height = searchForm.clientHeight + 'px';
	searchForm.classList.add('hidden');
	searchBtn.onclick = () => {
		searchForm.classList.toggle('hidden');
	}
}
