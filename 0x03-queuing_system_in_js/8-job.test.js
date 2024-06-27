// Test for job creation
import kue from 'kue';

const queue = kue.createQueue();
const { expect } = require('chai');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter(true);
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should not throw an error if jobs is an array', () => {
    expect(() => createPushNotificationsJobs([], queue)).not.to.throw();
  });

  it('create two new jobs to the queue', () => {
    queue.createJob('myJob', { foo: 'bar' }).save();
    queue.createJob('anotherJob', { baz: 'bip' }).save();
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('myJob');
    expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
  });
});





