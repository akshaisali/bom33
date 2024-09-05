
document.addEventListener('DOMContentLoaded', function () {
    function updateComponentLabels(selectedBOM) {
        const componentLabels = {
            washing: {
                'washing_80':  ['Front Door 80', 'Tank 80', 'Rear Conveyor 80'],
                'washing_100': ['Front Door 100', 'Tank 100', 'Rear Conveyor 100'],
                'washing_120': ['Front Door 120', 'Tank 120', 'Rear Conveyor 120']
            },
            furnace: {
                'furnace_80': ['Component 1A', 'Component 2A', 'Component 3A'],
                'furnace_100': ['Component 1B', 'Component 2B', 'Component 3B'],
                'furnace_120': ['Component 1C', 'Component 2C', 'Component 3C']
            },
            tempering: {
                'tempering_80': ['Front Conveyor 80', 'Furnace 80', 'Rear Conveyor 80'],
                'tempering_100': ['Front Conveyor 100', 'Furnace 100', 'Rear Conveyor 100'],
                'tempering_120': ['Front Conveyor 120', 'Furnace 120', 'Rear Conveyor 120']
            },
            conveyor: {
                'conveyor_80': ['Component 1P', 'Component 2P', 'Component 3P'],
                'conveyor_100': ['Component 1Q', 'Component 2Q', 'Component 3Q'],
                'conveyor_120': ['Component 1R', 'Component 2R', 'Component 3R']
            },
            preheating: {
                'preheating_80': ['Component 1PH80', 'Component 2PH80', 'Component 3PH80'],
                'preheating_100': ['Component 1PH100', 'Component 2PH100', 'Component 3PH100'],
                'preheating_120': ['Component 1PH120', 'Component 2PH120', 'Component 3PH120']
            },
            front_door: {
                'front_door_80': ['Component FD80A', 'Component FD80B', 'Component FD80C'],
                'front_door_100': ['Component FD100A', 'Component FD100B', 'Component FD100C'],
                'front_door_120': ['Component FD120A', 'Component FD120B', 'Component FD120C']
            },
            rear_door: {
                'rear_door_80': ['Component RD80A', 'Component RD80B', 'Component RD80C'],
                'rear_door_100': ['Component RD100A', 'Component RD100B', 'Component RD100C'],
                'rear_door_120': ['Component RD120A', 'Component RD120B', 'Component RD120C']
            },
            double_door: {
                'double_door_80': ['Component DD80A', 'Component DD80B', 'Component DD80C'],
                'double_door_100': ['Component DD100A', 'Component DD100B', 'Component DD100C'],
                'double_door_120': ['Component DD120A', 'Component DD120B', 'Component DD120C']
            }
        };

        const selectedCategory = selectedBOM.split('_')[0];
        const selectedLabels = componentLabels[selectedCategory][selectedBOM] || [];

        document.querySelectorAll(`#component-section-${selectedCategory} input[type="checkbox"]`).forEach((checkbox, index) => {
            checkbox.nextElementSibling.textContent = selectedLabels[index] || '';
        });
    }

    function toggleComponents() {
        const bomSelect = document.getElementById('bom').value;
        const modelSelect = document.getElementById('model').value;
        const componentSections = ['washing', 'furnace', 'tempering', 'conveyor', 'preheating', 'front_door', 'rear_door', 'double_door'];

        componentSections.forEach(section => {
            document.getElementById(`component-section-${section}`).style.display = 'none';
        });

        if (bomSelect) {
            const selectedSection = bomSelect.split('_')[0];
            document.getElementById(`component-section-${selectedSection}`).style.display = 'block';
            updateComponentLabels(bomSelect);

            if (selectedSection === 'furnace') {
                fetchFurnaceData(bomSelect);
            } else {
                fetchEquipmentData(bomSelect, modelSelect);
            }
        }
    } 

    function getCsrfToken() {
        return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    }

    function fetchEquipmentData(bom, model) {
        fetch('/get-equipment-data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({ bom, model })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('data-container').innerHTML = data.html;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('data-container').innerHTML = `<p>Error fetching data: ${error.message}</p>`;
        });
    }

    function fetchFurnaceData(bom) {
        // Extract the furnace size from the BOM (e.g., 'furnace_80' -> '80')
        const size = bom.split('_')[1];

        fetch('/get-furnace-data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({ size })
        })
        .then(response => response.json())
        .then(data => {
            let tableHTML = `
                <h3>Furnace Data (${size}):</h3>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Equipment BOM</th>
                            <th>Model</th>
                            <th>Specification</th>
                            <th>Make</th>
                            <th>Purpose</th>
                            <th>Quality</th>
                            <th>Price</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            data.forEach(entry => {
                tableHTML += `
                    <tr>
                        <td>${entry.type}</td>
                        <td>${entry.model}</td>
                        <td>${entry.specification}</td>
                        <td>${entry.make}</td>
                        <td>${entry.purpose}</td>
                        <td>${entry.quality}</td>
                        <td>${entry.price}</td>
                        <td>${entry.total}</td>
                    </tr>
                `;
            });

            tableHTML += `
                    </tbody>
                </table>
            `;

            document.getElementById('data-container').innerHTML = tableHTML;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('data-container').innerHTML = `<p>Error fetching furnace data: ${error.message}</p>`;
        });
    }

    document.getElementById('bom').addEventListener('change', toggleComponents);
    document.getElementById('model').addEventListener('change', toggleComponents);
});

document.addEventListener('DOMContentLoaded', function() {
    const furnaceCheckbox = document.getElementById('component2_tempering');
    const furnaceDataDiv = document.getElementById('furnace-data');

    // Hide furnace data div initially
    furnaceDataDiv.style.display = 'none';

    furnaceCheckbox.addEventListener('change', function() {
        if (this.checked) {
            fetchFurnaceData();
        } else {
            furnaceDataDiv.style.display = 'none';
        }
    });

    function fetchFurnaceData() {
        fetch('/get_furnace_data/')
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    // Handle empty data case
                    furnaceDataDiv.innerHTML = '<p>No Furnace data available.</p>';
                } else {
                    displayFurnaceData(data);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                furnaceDataDiv.innerHTML = '<p>Error fetching data. Please try again later.</p>';
                furnaceDataDiv.style.display = 'block';
            });
    }
    function displayFurnaceData(data) {
        // Create the table headers
        let tableHTML = `
            <h3>Furnace Data:</h3>
            <table class="table">
                <thead>
                    <tr>
                        <th>Equipment BOM</th>
                        <th>Model</th>
                        <th>Specification</th>
                        <th>Make</th>
                        <th>Purpose</th>
                        <th>Quality</th>
                        <th>Price</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
        `;

        // Add each entry as a row in the table
        data.forEach(entry => {
            tableHTML += `
                <tr>
                    <td>${entry.type}</td>
                    <td>${entry.model}</td>
                    <td>${entry.specification}</td>
                    <td>${entry.make}</td>
                    <td>${entry.purpose}</td>
                    <td>${entry.quality}</td>
                    <td>${entry.price}</td>
                    <td>${entry.total}</td>
                </tr>
            `;
        });

        // Close the table tags
        tableHTML += `
                </tbody>
            </table>
        `;

        // Update the inner HTML of the div to include the table
        furnaceDataDiv.innerHTML = tableHTML;
        furnaceDataDiv.style.display = 'block';
    }
});

function fetchRearConveyorData() {
    fetch('/get_rear_conveyor_data/')
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                rearConveyorDataDiv.innerHTML = '<p>No Rear Conveyor data available.</p>';
            } else {
                displayRearConveyorData(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            rearConveyorDataDiv.innerHTML = '<p>Error fetching data. Please try again later.</p>';
            rearConveyorDataDiv.style.display = 'block';
        });
}
document.addEventListener('DOMContentLoaded', function() {
    const rearConveyorCheckbox = document.getElementById('component3_tempering'); // Adjust ID based on your actual checkbox
    const rearConveyorDataDiv = document.getElementById('rearconveyor-data');

    rearConveyorCheckbox.addEventListener('change', function() {
        if (this.checked) {
            fetchRearConveyorData();
        } else {
            rearConveyorDataDiv.style.display = 'none';
        }
    });

    function fetchRearConveyorData() {
        fetch('/get_rear_conveyor_data/')
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    rearConveyorDataDiv.innerHTML = '<p>No Rear Conveyor data available.</p>';
                } else {
                    displayRearConveyorData(data);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                rearConveyorDataDiv.innerHTML = '<p>Error fetching data. Please try again later.</p>';
                rearConveyorDataDiv.style.display = 'block';
            });
    }

    function displayRearConveyorData(data) {
        let tableHTML = `
            <h3>Rear Conveyor Data:</h3>
            <table class="table">
                <thead>
                    <tr>
                        <th>Equipment BOM</th>
                        <th>Model</th>
                        <th>Specification</th>
                        <th>Make</th>
                        <th>Purpose</th>
                        <th>Quality</th>
                        <th>Price</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
        `;

        data.forEach(entry => {
            tableHTML += `
                <tr>
                    <td>${entry.type}</td>
                    <td>${entry.model}</td>
                    <td>${entry.specification}</td>
                    <td>${entry.make}</td>
                    <td>${entry.purpose}</td>
                    <td>${entry.quality}</td>
                    <td>${entry.price}</td>
                    <td>${entry.total}</td>
                </tr>
            `;
        });

        tableHTML += `
                </tbody>
            </table>
        `;

        rearConveyorDataDiv.innerHTML = tableHTML;
        rearConveyorDataDiv.style.display = 'block';
    }
});
document.addEventListener('DOMContentLoaded', function () {
    const frontConveyorCheckbox = document.getElementById('component1_tempering'); // Adjust ID based on your actual checkbox
    const frontConveyorDataDiv = document.getElementById('frontconveyor-data');

    // Hide the data div initially
    frontConveyorDataDiv.style.display = 'none';

    // Add event listener for the checkbox
    frontConveyorCheckbox.addEventListener('change', function () {
        if (this.checked) {
            fetchFrontConveyorData();
        } else {
            frontConveyorDataDiv.style.display = 'none';
        }
    });

    function fetchFrontConveyorData() {
        fetch('/get_front_conveyor_data/')
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                frontConveyorDataDiv.innerHTML = '<p>No Rear Conveyor data available.</p>';
            } else {
                displayFrontConveyorData(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            frontConveyorDataDiv.innerHTML = '<p>Error fetching data. Please try again later.</p>';
            frontConveyorDataDiv.style.display = 'block';
        });
    }

    function displayFrontConveyorData(data) {
        let tableHTML = `
        
            <h3>Front Conveyor Data:</h3>
            <table class="table">
                <thead>
                    <tr>
                        <th>Equipment BOM</th>
                        <th>Model</th>
                        <th>Specification</th>
                        <th>Make</th>
                        <th>Purpose</th>
                        <th>Quality</th>
                        <th>Price</th>
                        <th>Total</th>
                        
                    </tr>
                </thead>
                <tbody>
        `;
    
        data.forEach(entry => {
            tableHTML += `
                <tr>
                    <td>${entry.type}</td>
                    <td>${entry.model}</td>
                    <td>${entry.specification}</td>
                    <td>${entry.make}</td>
                    <td>${entry.purpose}</td>
                    <td>${entry.quality}</td>
                    <td>${entry.price}</td>
                    <td>${entry.total}</td>
                    <td>
                       
                    </td>
                </tr>
            `;
            
        });

        tableHTML += `
                </tbody>
            </table>
        `;
    
        frontConveyorDataDiv.innerHTML = tableHTML;
        frontConveyorDataDiv.style.display = 'block';
        
    
        // Add event listeners after the table is updated
        document.querySelectorAll('.edit-button').forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const id = this.getAttribute('data-id');
                editEntry(id);
            });
        });
    
        document.querySelectorAll('.delete-button').forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const id = this.getAttribute('data-id');
                deleteEntry(id);
            });
        });
    }
    
    
    function editEntry(id) {
        // Implement the logic for editing an entry
        // This could involve displaying a form with the current data and allowing the user to make changes
        console.log('Edit entry with ID:', id);
    }
    
    function getCsrfToken() {
        let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        return csrfToken;
    }
    
    function deleteEntry(id) {
        if (confirm('Are you sure you want to delete this item?')) {
            fetch(`/delete-equipment/${id}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken()
                }
            })
            .then(response => {
                if (response.ok) {
                    alert('Item deleted successfully.');
                    fetchFrontConveyorData(); // Refresh the data
                } else {
                    alert('Failed to delete the item.');
                }
            })
            .catch(error => console.error('Error:', error));
        }
    }
    
    
    
});

document.addEventListener('DOMContentLoaded', function () {
    const availableTypes = ['80', '100', '120'];
    
    function fetchComponentData(component, type) {
        const url = `/get_${component.toLowerCase().replace(' ', '_')}_data/?type=${type}`;

        return fetch(url)
            .then(response => response.json())
            .then(data => {
                return { component, type, data }; // Return an object with component, type, and data
            })
            .catch(error => {
                console.error(`Error fetching ${component} ${type} data:`, error);
                return { component, type, data: [], error: true }; // Indicate an error occurred
            });
    }

    function displayComponentData(allData) {
        allData.forEach(({ component, type, data }) => {
            let tableHTML = '';
            if (data.length === 0) {
                tableHTML += `<p>${component} ${type} data not available.</p>`;
            } else {
                tableHTML += `
                    <h3>${component} ${type}:</h3>
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Equipment BOM</th>
                                <th>Model</th>
                                <th>Specification</th>
                                <th>Make</th>
                                <th>Purpose</th>
                                <th>Quality</th>
                                <th>Price</th>
                                <th>Total</th>
                            </tr>
                        </thead>
                        <tbody>
                `;

                data.forEach(entry => {
                    tableHTML += `
                        <tr>
                            <td>${entry.type}</td>
                            <td>${entry.model}</td>
                            <td>${entry.specification}</td>
                            <td>${entry.make}</td>
                            <td>${entry.purpose}</td>
                            <td>${entry.quality}</td>
                            <td>${entry.price}</td>
                            <td>${entry.total}</td>
                        </tr>
                    `;
                });

                tableHTML += `
                        </tbody>
                    </table>
                `;
            }

            const componentDivId = `${component.toLowerCase().replace(' ', '')}-data`; // Generate div ID from component name
            const componentDataDiv = document.getElementById(componentDivId);
            if (componentDataDiv) {
                componentDataDiv.innerHTML = tableHTML;
                componentDataDiv.style.display = 'block';
            }
        });
    }

    function handleCheckboxChange() {
        const checkedComponents = Array.from(document.querySelectorAll('input[name="components"]:checked')).map(cb => cb.value);
        const selectedType = prompt("Enter the type (80, 100, 120) to fetch data:", "80,100,120");

        if (availableTypes.includes(selectedType)) {
            const fetchPromises = checkedComponents.map(component => fetchComponentData(component, selectedType));

            Promise.all(fetchPromises)
                .then(allData => displayComponentData(allData));
        } else {
            alert("Invalid type selected. Please enter 80, 100, or 120.");
        }
    }

    document.querySelectorAll('input[name="components"]').forEach(checkbox => {
        checkbox.addEventListener('change', handleCheckboxChange);
    });
});
