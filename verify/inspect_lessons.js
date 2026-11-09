const { ALL_LESSONS } = require('../content/lessons_all.js');

console.log('Total lessons:', ALL_LESSONS.length);
let totalSteps = 0;
let totalExs = 0;
let totalTraps = 0;
let totalQuiz = 0;

ALL_LESSONS.forEach(l => {
  const steps = l.steps ? l.steps.length : 0;
  const exs = l.examples ? l.examples.length : 0;
  const traps = l.pitfalls ? l.pitfalls.length : 0;
  const quiz = l.quizzes ? l.quizzes.length : (l.quiz ? (l.quiz.questions ? l.quiz.questions.length : 1) : 0);
  totalSteps += steps;
  totalExs += exs;
  totalTraps += traps;
  totalQuiz += quiz;
  const r = l.ref ? `${l.ref.slide_file} (${l.ref.pages || 'p.' + l.ref.page_start})` : 'No ref';
  console.log(`[${l.id}] ${l.title} | Steps: ${steps} | Exs: ${exs} | Traps: ${traps} | Quiz: ${quiz} | Ref: ${r}`);
});

console.log('---');
console.log(`SUMMARY: Total Steps=${totalSteps}, Total Examples=${totalExs}, Total Traps=${totalTraps}, Total Quiz Questions=${totalQuiz}`);
