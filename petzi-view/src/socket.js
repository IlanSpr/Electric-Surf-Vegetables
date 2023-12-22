import { reactive } from "vue";
import { io } from "socket.io-client";

export const state = reactive({
  connected: false,
  tickets: []
});

const URL = "http://webhook:5000/tickets";

export const socket = io(URL, { autoConnect: true });

socket.on("connect", () => {
  state.connected = true;
});

socket.on("disconnect", () => {
  state.connected = false;
});

socket.on("ticket_event", (ticket) => {
  state.tickets.push(ticket);
});
