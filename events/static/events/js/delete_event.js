function deleteEvent(eventId) {
    // Confirms with the user before attempting to delete an event
    if (confirm("Are you sure you want to delete this event?")) {
        fetch(`/delete_event/${eventId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCsrfToken(), // Includes CSRF token for security
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                alert("Event deleted successfully!");
                location.reload(); // Refresh the page to reflect changes
            } else {
                alert("Failed to delete the event.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
}

function getCsrfToken() {
    // Extracts the CSRF token from cookies for secure requests
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, 'csrftoken'.length + 1) === ('csrftoken=')) {
                cookieValue = decodeURIComponent(cookie.substring('csrftoken'.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
