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
          <tr v-for="ticket in tickets" :key="ticket.number">
            <td>{{ ticket.title }}</td>
            <td>{{ ticket.type }}</td>
            <td>{{ ticket.category }}</td>
            <td>{{ ticket.cancellationReason || 'N/A' }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { state } from '../socket.js';

export default {
  name: "BusinessView",

  computed: {
    tickets() {
      return state.tickets;
    },
    refundRate() {
      const refundCount = this.tickets.filter(ticket => ticket.cancellationReason).length;
      return ((refundCount / this.tickets.length) * 100).toFixed(2);
    },
    canceledEvents() {
      return this.tickets.filter(ticket => ticket.cancellationReason === 'event_cancellation').length;
    },
    averagePrice() {
      const totalAmount = this.tickets.reduce((sum, ticket) => sum + parseFloat(ticket.price.amount), 0);
      return (totalAmount / this.tickets.length).toFixed(2);
    },
  },
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

.tickets-table tr:nth-child(even) {
  background-color: #f9f9f9;
}
</style>
