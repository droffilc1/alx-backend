// Node Redis client and async operations
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

promisify(setNewSchool);
async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value, (err, reply) => {
    if (err) throw err;
    redis.print(`Reply: ${reply}`);
  });
}

promisify(displaySchoolValue);
async function displaySchoolValue(schoolName) {
  await client.get(schoolName, (err, reply) => {
    if (err) throw err;
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
