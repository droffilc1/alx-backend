// Seat
import express from 'express';
import { promisify } from 'util';
import redis from 'redis';
import kue from 'kue';

// Redis client
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

async function reserveSeat(number) {
  const setAsync = promisify(client.set).bind(client);
  return setAsync('available_seats', number);
}

reserveSeat(50);
let reservationEnabled = true;
const queue = kue.createQueue();

async function getCurrentAvailableSeats() {
  const getAsync = promisify(client.get).bind(client);
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats) : 0;
}

// Set up express server
const app = express();
const port = 1245;

// GET /available_seats
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats()
  res.json({ numberOfAvailableSeats: seats });
})

// GET /reserve_seat
app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
    res.send({ "status": "Reservation are blocked" });
  } else {
    const seatsReserved = queue.create('reserve_seat').save((err) => {
      if (!err) {
        res.json({ status: 'Reservation in process' });
      } else {
        res.json({ status: 'Reservation failed' });
      }
    });
    seatsReserved.on('complete', () => {
      console.log(`Seat reservation job ${seatsReserved.id} completed`);
    }).on('failed', (err) => {
      console.log(`Seat reservation job ${seatsReserved.id} failed: ${err.message}`);
    });
  }
});

// GET /process
app.get('/process', (req, res) => {
  res.json({ "status": "Queue processing" });
  queue.process('reserve_seat', async (job, done) => {
    const count = await getCurrentAvailableSeats();
    console.log(`Current available seats: ${count}`);
    if (count === 0) {
      reservationEnabled = false;
      done();
    } else if (count > 0) {
      await reserveSeat(count - 1);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  })
})

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
})
