window.onload = () => {
    update();
    var esteSelectata = false;

    function fade() {
        let buline = document.getElementsByClassName("bulina");
        if (buline !== null) {
            for (let bul of buline) {

            }
        }
    }

    function selectata() {
        if (esteSelectata === false) {
            esteSelectata = true;
            this.style.border = "red solid 3px";
        }
    }

    function dimensiuneRandom() {
        let dim = Math.floor(Math.random() * 151);
        while (true) {
            if (dim < 30 || dim > 150) {
                dim = Math.floor(Math.random() * 151);
            } else break;
        }
        return dim;
    }

    function update() {
        let dots = sessionStorage.getItem('dots');
        let noDots = document.getElementById('noDots');
        if (!noDots) {
            noDots = document.createElement('div');
            noDots.style.textAlign = "right";
            noDots.setAttribute('id', 'noDots');
            document.body.appendChild(noDots);
        }
        noDots.textContent = dots ? dots : 0;
    }


    document.addEventListener("click", () => {
        if (esteSelectata === true) {
            let buline = document.getElementsByClassName("bulina");
            for (let bul of buline) {
                bul.style.removeProperty("border"); // nu se actualizeaza pe site
                console.log(bul.style.border.toString());
                esteSelectata = false;
                return true;

            }
        } else {
            const div = document.createElement('div');
            div.classList.add("bulina");
            div.onclick = selectata;
            div.style.backgroundColor = "rgb(255, 255, 255)";
            document.body.appendChild(div);
            let dim = dimensiuneRandom();
            div.style.width = `${dim}px`;
            div.style.height = `${dim}px`;
            div.style.borderRadius = '50%';
            div.style.position = 'absolute';
            let dots = sessionStorage.getItem('dots');
            if (dots) {
                dots = JSON.parse(dots) + 1;
            } else {
                dots = 1;
            }
            // console.log(dots);
            sessionStorage.setItem('dots', JSON.stringify(dots));
            div.style.top = `${Math.random() * window.innerHeight}px`;
            div.style.left = `${Math.random() * window.innerWidth}px`;
            update();
        }
    })
}