
async function refapicall(){
    const resName= document.getElementById("resName").value;
    const mailid =document.getElementById("mailId").value;
    // const response = await fetch(`https://api.unpaywall.org/v2/${doi}?email=${mailid}`);
                                // {mode:"no-cors"}
    const url =`https://api.unpaywall.org/v2/search?query=${resName}&is_oa=true&email=${mailid}`;
    const response = await fetch(url);

    const jsonData = await response.json();
    console.log(`url = ${url} ${JSON.stringify(jsonData.results,null,2)}`);


    const arr = jsonData.results
    document.getElementById("add").innerText=JSON.stringify(jsonData.results.map(element => {
            return element.response.title;
    }),null,2   );
    const data = {
      //string
        // author:jsonData.results[0].z_authors[0].given,
        author:"dharti pr bojh",
        title:jsonData.results[0].response.title, 
        volume:jsonData.results[0].snippet,
        Doi:jsonData.results[0].response.doi,
        date:jsonData.results[0].response.published_date,
        page:'1'
      };
    const check = await fetch("/literatureSurvey", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      })
        
    console.log("check"+check+"data"+JSON.stringify(data,null,2));
}