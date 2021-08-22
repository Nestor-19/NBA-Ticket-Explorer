const httpGet = (theUrl) =>{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

Imagesdata = JSON.parse(httpGet('http://'+window.location.host+'/static/CrawledData/logos.json'))

for (const teamName in Imagesdata) {
    // console.log(`${property}: ${object[property]}`);
    document.querySelector('#card-container').innerHTML += `
            <div  class = "col-md-4 my-col">
                <div class="card-container">
                    <div class="card">
                        <div class="imgBx">
                            <img src="`+Imagesdata[teamName]+`">
                        </div>
                        <div class="contentBx">
                            <h2>`+teamName+`</h2>
                            <a href="{% url 'gameTickets:tkt' team_name=`+teamName+` %}">Get Tickets</a>
                        </div>
                    </div>
                </div>
            </div>`
}
