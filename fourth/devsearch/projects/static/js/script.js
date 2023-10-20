
    let searchForm = document.getElementById('search_query');
    let pageLink = document.querySelectorAll('.page-link');

if (searchForm){
    for (let i=0; pageLink.length > i; i++){
        pageLink[i].addEventListener('click', function(e){
            e.preventDefault()

            let page = this.dataset.page;

            searchForm.innerHTML += `<input values=${page} name="page" type="hidden">`

            searchForm.submit()
        })
    }
}

