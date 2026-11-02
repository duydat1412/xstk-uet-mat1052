const { ALL_LESSONS } = require('../content/lessons_all.js');
console.log('Total ALL_LESSONS:', ALL_LESSONS.length);
let refCount = 0;
ALL_LESSONS.forEach(l => {
  if (l.ref && l.ref.slide_file && l.ref.pages && l.ref.section && l.ref.remind) {
    refCount++;
  }
});
console.log('Lessons with valid complete ref:', refCount);
