#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (!completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId] = 0;
        }
        completedTasksByUser[task.userId]++;
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
