const kue = require('kue'), queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '709-585-3900',
  message: 'Notify'
}).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', (result) => {
  console.log('Notification job completed');
});

job.on('failed', (errorMessage, doneAttempts) => {
  console.log('Notification job failed');
});
