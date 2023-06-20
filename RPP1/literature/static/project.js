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
async function createPro(){

    const proName= document.getElementById('ProjectName').value;
    console.log(proName);
        const csrfToken = getCookie('csrftoken'); // Get the CSRF token

    const resp = await fetch('',{

        method:'POST',

        headers: {
            'Content-Type':'application/json',
                      "X-CSRFToken": csrfToken // Include the CSRF token in the headers
        },
        body: JSON.stringify(proName)
    }
    )
    console.log(resp);
}