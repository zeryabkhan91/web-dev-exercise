
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.cards').forEach((column) => {
      new Sortable(column, {
          group: 'shared',
          animation: 150,
          onEnd: (event) => {
              let newRank = 1000;
              let tickets = event.to.getElementsByClassName('card');

              let ticketId = event.item.dataset.ticketId;
              let newColumnId = event.to.dataset.columnId; 

              for (ticket in tickets) {
                if (tickets[ticket].dataset.ticketId === ticketId) {
                  if (ticket > 0) {
                    let aboveTicketRank = parseInt(tickets[ticket - 1].dataset.ticketRank);
                    newRank = aboveTicketRank - 1;
                  }
                  break;
                }
              } 

              updateTicket(ticketId, newColumnId, newRank)
          }
      });
  });
});

const updateTicket = (ticketId, newColumnId, newRank) => {
  fetch(`/helpdesk/ticket/${ticketId}/`, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({
      column_id: newColumnId,
      rank: newRank
    })
  })
    .then(async response => {
      const result = await response.json()
      if(result.status == "success" && result.data) {
        const elementWithSpecificTicketId = document.querySelector(`[data-ticket-id="${ticketId}"]`);
        elementWithSpecificTicketId.outerHTML = result.data.html
      }
    })
    .catch(error => {
      console.error(error)
    });
}