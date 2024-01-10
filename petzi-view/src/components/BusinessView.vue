<template>
  <div class="dashboard">
    <h1>Business Intelligence Dashboard</h1>
    <div v-if="!tickets.length">
      <p>No ticket data available yet.</p>
    </div>
    <div v-else>
      <div class="statistics">
        <div class="stat">
          <p>Total Tickets: {{ tickets.length }}</p>
        </div>
        <div class="stat">
          <p>Refund Rate: {{ refundRate }}%</p>
        </div>
        <div class="stat">
          <p>Canceled Events: {{ canceledEvents }}</p>
        </div>
        <div class="stat">
          <p>Average Price: ${{ averagePrice }}</p>
        </div>
      </div>
      <table class="tickets-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Type</th>
            <th>Category</th>
            <th>Refund Reason</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="ticketInfo in tickets" :key="ticketInfo.ticket.number">
            <td>{{ ticketInfo.ticket.title }}</td>
            <td>{{ ticketInfo.ticket.type }}</td>
            <td>{{ ticketInfo.ticket.category }}</td>
            <td>{{ ticketInfo.ticket.cancellationReason || 'N/A' }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { computed, onMounted, onBeforeUnmount, ref } from 'vue';

export default {
  name: "BusinessView",

  setup() {
    const tickets = ref([]);

    const initializeSSE = () => {
      const evtSource = new EventSource("http://localhost:8080/events");

      evtSource.onmessage = (e) => {
        const receivedData = JSON.parse(e.data);
        console.log('Parsed data:', receivedData);

        if (receivedData.message) {
          try {
            const jsonPart = receivedData.message.replace('Ticket Created: ', '');
            const ticketData = JSON.parse(jsonPart);
            tickets.value.push(ticketData);
          } catch (err) {
            console.error('Error parsing ticket data:', err);
          }
        }
      };

      onBeforeUnmount(() => {
        if (evtSource) {
          evtSource.close();
        }
      });
    };

    onMounted(initializeSSE);

    const refundRate = computed(() => {
      const refundCount = tickets.value.filter(ticket => ticket.cancellationReason).length;
      return ((refundCount / tickets.value.length) * 100).toFixed(2);
    });

    const canceledEvents = computed(() => {
      return tickets.value.filter(ticket => ticket.cancellationReason === 'event_cancellation').length;
    });

    const averagePrice = computed(() => {
      const totalAmount = tickets.value.reduce((sum, ticketInfo) => {
        return sum + (ticketInfo.price ? parseFloat(ticketInfo.price.amount) : 0);
      }, 0);
      return tickets.value.length > 0 ? (totalAmount / tickets.value.length).toFixed(2) : '0.00';
    });

    return {
      tickets,
      refundRate,
      canceledEvents,
      averagePrice
    };
  }
};
</script>


<style scoped>
.dashboard {
  max-width: 800px;
  margin: 0 auto;
  font-family: 'Arial', sans-serif;
}

h1 {
  text-align: center;
  color: #333;
}

.statistics {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.stat p {
  font-size: 1.2em;
  color: #555;
}

.tickets-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.tickets-table th, .tickets-table td {
  border: 1px solid #ddd;
  padding: 8px;
}

.tickets-table th {
  background-color: #f4f4f4;
  color: #333;
}


.tickets-table tr:nth-child(odd) {
  background-color: #333;
  color: #fff;
}

.tickets-table tr:nth-child(even) {
  background-color: #fff;
  color: #333;
}

</style>
