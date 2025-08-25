import axios from "axios";

const BASE_URL = "http://localhost:8000";

export async function getExchangeRates() {
  const res = await axios.get(`${BASE_URL}/changes/exchange`);
  return res.data.exchange_rate; // ⚡ accede al objeto interno
}

export async function getInterestRates() {
  const res = await axios.get(`${BASE_URL}/rates/interest`);
  return res.data.interest_rate; // ⚡ accede al objeto interno
}
