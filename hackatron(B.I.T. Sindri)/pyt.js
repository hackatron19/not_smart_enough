var {PythonShell}=require('python-shell');
let options = {
    mode: 'text',
    pythonPath: 'C:/python/python.exe',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: './',
    //args: ['value1', 'value2', 'value3']
  };
  var tes=new PythonShell('./randomgen.py',options)
  tes.on('message',function(message)
  {
      console.log(message)
  })
  tes.end(function (err,code,signal) {
    if (err) throw err;
    console.log('The exit code was: ' + code);
    console.log('The exit signal was: ' + signal);
    console.log('finished');
    console.log('finished');
  });