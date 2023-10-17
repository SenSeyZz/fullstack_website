var key;

export async function deleteMethod() {
    const formData = new FormData();
    formData.append('title', 'example data');
    formData.append('description', 'example description');
    if(document.getElementById("delete").value !== null){
        key = document.getElementById("delete").value
        console.log(key);
    } 

    try {
      const response = await fetch(`http://localhost:8000/api/${key}`, {
        method: 'DELETE',
        body: formData
      });
  
      if (response.ok) {
        const data = await response.json();
        console.log(data);
      } else {
        console.log('Error:', response.statusText);
      }
    } catch (error) {
      console.log('Error:', error.message);
    }
  }