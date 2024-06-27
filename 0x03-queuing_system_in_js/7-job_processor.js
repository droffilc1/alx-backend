// Track progress and errors with Kue: Create the Job processor
import kue from 'kue';

const blacklist = [4153518780, 4153518781];

const sendNotification = (phoneNumber, message, job, done) => {
  const progress = job.on('progress', (progress) => {
    console.log(`${progress}%`);
  });
  if (phoneNumber in blacklist) {
    job.on('failed', () => {
      throw new Error(`Phone number ${phoneNumber} is blacklisted`);
    });
  } else if (progress <= 50) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, function (job, done) {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
