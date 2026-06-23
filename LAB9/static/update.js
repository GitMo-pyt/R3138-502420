function addWork() {
    let Company = document.getElementById('company').value
    let term = document.getElementById('term').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'company': Company,
                             'term': term,
                             'in_stock': true})
    })
}