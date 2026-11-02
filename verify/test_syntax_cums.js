const fs = require('fs');

['a', 'b', 'c', 'd', 'e'].forEach(c => {
  const code = fs.readFileSync(`content/cum_${c}.js`, 'utf8');
  try {
    eval(code);
    console.log(`content/cum_${c}.js syntax OK!`);
  } catch (err) {
    console.error(`content/cum_${c}.js syntax ERROR:`, err);
    process.exit(1);
  }
});
