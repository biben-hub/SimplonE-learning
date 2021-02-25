const api_url = "http://127.0.0.1:5000/apivideo";





function displayData(data) {
    let pythonVids = document.querySelector('#python-vids');

    data.forEach(element => {
        // console.log(element.content)
        let author = element.author
        console.log(author)
        let categ = element.categorie
        console.log(categ)
        let description = element.description
        let anneeVideo = element.anne_video

        if (categ === "Python"){

        }

        // let image = element.image
        // let date = element.date
        // let title = element.title


        // let tbody = document.querySelector('tbody');
        // let tr = document.createElement("tr");
        // let colonne1 = tr.insertCell(0);
        //     colonne1.innerHTML += title ;
        // let colonne2 = tr.insertCell(1);
        //     colonne2.innerHTML += date;
        // let colonne3 = tr.insertCell(2);
        //     colonne3.innerHTML += `<img src="${image}" style="width:300px"></img>`;
        // let colonne4 = tr.insertCell(3);
        //     colonne4.innerHTML += content;
        // tbody.appendChild(tr);
    });
}


async function getData(url) {
    const response = await fetch(url);
    let data = await response.json();
    // console.log(data);
    displayData(data);
    return data
}
getData(api_url)

// INSERT INTO videos(titre, author,lien,anne_video,description,categorie) VALUES('descriptionvideoadlane','autueuradlane','https://www.youtube.com/watch?v=m6chqKlhpPo', '2020',"description adlane",'adlanelangage');