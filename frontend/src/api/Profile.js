import axios from "axios";
const baseURL = "http://localhost:5600";

const api = axios.create({
  baseURL: baseURL,
  headers: {
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
  },
});

export default async function getProfile(url, method='scrape') {
    console.log(url)
  return api.get("/profile", {
    params: {
      profile: url,
      method: method
    },
  });
}
