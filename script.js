// Base URL of backend (Flask API)
const BASE_URL = "http://127.0.0.1:5000";

// Add Medicine
async function addMedicine() {
    const name = document.getElementById("name").value;
    const dosage = document.getElementById("dosage").value;
    const reminder_time = document.getElementById("reminder_time").value;
    const notes = document.getElementById("notes").value;

    if (!name || !dosage || !reminder_time) {
        alert("Please fill all required fields!");
        return;
    }

    const response = await fetch(`${BASE_URL}/add_medicine`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name,
            dosage,
            reminder_time,
            notes
        })
    });

    const result = await response.json();
    alert(result.message);

    document.getElementById("medicineForm").reset();
}

// View Medicines
async function loadMedicines() {
    const response = await fetch(`${BASE_URL}/view_medicines`);
    const medicines = await response.json();

    const tableBody = document.getElementById("medicineTableBody");
    tableBody.innerHTML = "";

    medicines.forEach(med => {
        const row = `
            <tr>
                <td>${med.id}</td>
                <td>${med.name}</td>
                <td>${med.dosage}</td>
                <td>${med.reminder_time}</td>
                <td>${med.notes}</td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });
}

// Check Reminder
async function checkReminder() {
    const response = await fetch(`${BASE_URL}/check_reminder`);
    const result = await response.json();

    if (result.reminder) {
        alert(`⏰ Time to take ${result.reminder}`);
    } else {
        alert("No reminders right now.");
    }
}

// Auto check every 60 seconds
setInterval(checkReminder, 60000);