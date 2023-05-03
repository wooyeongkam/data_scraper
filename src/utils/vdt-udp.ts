import dgram from "dgram";
import fs from "fs";

const PORT = 6501;
const server = dgram.createSocket("udp4");

server.on("listening", () => {
  const address = server.address();
  console.log(`server listening on ${address.address}:${address.port}`);
});

server.on("message", (message, remote) => {
  const data = message.toString().trim();
  fs.appendFile("vdr_data.log", `${data}\n`, (error) => {
    if (error) throw error;
    console.log("Data saved to file");
  });
});

server.bind(PORT);
