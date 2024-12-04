const kue = require('kue'), queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    return new Error('Jobs is not an array');
  }

  for (const data of jobs) {
    const job = queue.create('push_notification_code_3', data);
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    })
    .on('complete', (result) => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (errorMessage, doneAttempts) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    })
    .on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  }
}
module.exports = createPushNotificationsJobs;
