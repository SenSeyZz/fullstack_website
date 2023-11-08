// Import necessary dependencies and modules
import React, { useEffect, useState, useRef } from 'react';

import axios from "axios"; // Import Axios for HTTP requests

// Create an empty array for filter values
export var i = [];

// Function to render the components

// SOOOo I put everything in the home function and now the filters don twork anymore maybe just take them out. 

const Home = () => {
  var j = [] // Initialize an empty array for selected filter options
  var k; // Initialize a variable for filter count
  var uniqueTitle = [] // Initialize an array for unique filter titles
  var uniqueNb = [] // Initialize an array for unique filter numbers

  // Define available filter options
  var options = [
    { value: 'CAPM', label: 'CAPM' },
    { value: 'Beta', label: 'Beta' },
    { value: 'Volatility', label: 'Volatility' }
  ];

  // Function to send filters and values to the API
  async function postMethod() {
    const formData = new FormData();
    formData.append('title', `${uniqueTitle}` );
    formData.append('description', `${i}`);
    
    try {
      const response = await fetch('http://localhost:8000/api/', {
        method: 'POST',
        body: formData
      })

      if (response.ok) {
        const data = await response.json();
        const xValue = data.x;
        console.log('Value of x:', xValue); 
      } else {
        console.log('Error:', response.statusText);
      }
    } catch (error) {
      console.log('Error:', error.message);
    }
  }

  // Function to fetch and list items from the API
  async function fetchTodoList() {
    try {
      const response = await fetch('http://localhost:8000/api/back');
      const data = await response.json();
      console.log(data);
      setAnswer(data[0]);
      
      if (data.length > 0) {
        let idToDelete = data[data.length - 1].id;
        
        // Send a DELETE request using Axios
        axios.delete(`http://localhost:8000/api/back/delete/${idToDelete}/`)
        .then(response => {
          console.log('Delete successful:', response.data);
        })
        .catch(error => {
          console.error('Error:', error);
        });
      };

      return answer;
    } catch (error) {
      console.log('Error:', error.message);
    }
  }

  // Function to post filters and fetch items from the API
  async function postGet() {
    await postMethod();
    await fetchTodoList();
  }

  // Component for rendering a dropdown menu for filter selection
  function DropdownMenu({ inputId }) {
    const [selectedValue, setSelectedValue] = useState('Select an option');
    const inputValueRef = useRef('');

    if (selectedValue !== 'Select an option') {
      j.push(selectedValue);
      uniqueTitle = Array.from(new Set(j));
    }

    // Remove the selected filter option from available options
    options = options.filter(option => option.value !== selectedValue);

    return (
      <div>
        <select
          value={selectedValue}
          onChange={(e) => setSelectedValue(e.target.value)}
        >
          <option>{selectedValue}</option>
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        <input
          type="number"
          id={inputId}
          min="0"
          max="100"
          step="1"
          ref={inputValueRef}
        />
      </div>
    );
  }

  // State variables
  const [filterCount, setFilterCount] = useState(0);
  const [todos, setTodos] = useState([]);
  const [answer, setAnswer] = useState(null);

  // Function to add filter menus
  const handleAddFiltersClick = () => {
    setFilterCount((prevCount) => prevCount + 1);
    k = filterCount;
  };

  
  // Function to collect filter values
const handleLogValues = () => {
  for (let index = 0; index < filterCount; index++) {
    const inputValue = document.getElementById(`myNumberInput-${index}`).value;
    i.push(inputValue);
    uniqueNb = Array.from(new Set(i));
  }
};

  // Render the UI elements
  return (
    <div>
      <h1>Malkiel investment</h1>
      <h2>Filters:</h2>
      <button onClick={handleAddFiltersClick}>Add Filters</button>
      {Array.from({ length: filterCount }, (_, index) => (
        <DropdownMenu key={index} inputId={`myNumberInput-${index}`} />
      ))}
      
      <button onClick={() => {handleLogValues(); postGet()}}>Submit</button>
      
      <div>
        {todos.map((item) => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
      {answer && (
        <div>
          <p>Average value: {answer.number}</p>
          <p>Stock name: {answer.description}</p>
        </div>
      )}
    </div>
  );
};

export default Home;
