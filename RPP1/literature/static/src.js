
 // Retrieve the CSRF token from the cookie
 function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Extract the CSRF token
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
async function refapicall(){
    const resName= document.getElementById("resName").value;
    const mailid =document.getElementById("mailId").value;
    // const response = await fetch(`https://api.unpaywall.org/v2/${doi}?email=${mailid}`);
                                // {mode:"no-cors"}
    const url =`https://api.unpaywall.org/v2/search?query=${resName}&is_oa=true&email=${mailid}`;
    const csrfToken = getCookie('csrftoken'); // Get the CSRF token

    const response = await fetch(url);

    const jsonData = await response.json();
    console.log(`url = ${url} ${JSON.stringify(jsonData.results,null,2)}`);


    const arr = jsonData.results;
    document.getElementById("add").innerText=JSON.stringify(jsonData.results.map(element => {
            return element.response.title ;
    }),null,2   );
    const title =jsonData.results.map(element => {
      return element.response.title ;
})
const doiNo =jsonData.results.map(element => {
  return element.response.doi ;
})
    const data = {
      //string
        // author:jsonData.results[0].z_authors[0].given,
        // author:"dharti pr bojh",
        title:title, 
        // volume:jsonData.results[0].snippet,
        Doi:doiNo,
        // date:jsonData.results[0].response.published_date,
        // page:'1'
      };
    const check = await fetch("/literature/reference/my_model/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",             
          "X-CSRFToken": csrfToken // Include the CSRF token in the headers


        },
        body: JSON.stringify(data)
      })
        
    console.log("check"+check+"data"+JSON.stringify(data,null,2));
}