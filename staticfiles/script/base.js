document.onreadystatechange = () => {
	let sp = document.querySelector('.search-open');
	let searchbar = document.querySelector('.search-inline');
	let shclose = document.querySelector('.search-close');

	function changeClass() {
		searchbar.classList.add('search-visible');
	}

	function closesearch() {
		searchbar.classList.remove('search-visible');
	}

	sp.addEventListener('click', changeClass);
	shclose.addEventListener('click', closesearch);
}
