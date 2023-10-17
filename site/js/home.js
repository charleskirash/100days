function toggleSidebar(){
	const sidebar = document.querySelector('.sidebar-toggle');
	let activeIndex;
	sidebar.addEventListener('click', toggleSidebar => {
		document.body.classList.toggle('collapsed', true)
	});
	sidebar.classList.toggle('collapsed');
}