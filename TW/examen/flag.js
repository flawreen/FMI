window.onload = () => {
    let coduri;
    let fisier = fetch("flag.json");
        fisier.then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }
            return response.text();
        })
        .then((text) => {
            coduri = JSON.parse(text);
        })
        .catch(function(err){
            alert(err);});

    console.log(coduri);

    document.addEventListener("keydown", (e) => {
        const key = e.key;
        switch (key) {
            case "A":

        }
    })
}