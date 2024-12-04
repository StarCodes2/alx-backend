const { expect } = require('chai');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', function() {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    kue.Job.rangeByType('push_notification_code_3', 'active', 0, 10, 'asc', function (err, jobs) {
      jobs.forEach(function (job) {
        job.remove();
      });
    });
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', function() {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue when jobs is an array', function() {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234' },
      { phoneNumber: '4153518781', message: 'This is the code 5678' }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('should log correct messages when jobs are created', function() {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];
    job.emit('complete');
    job.emit('failed', 'Something went wrong');
    job.emit('progress', 50, {});

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  });
});
