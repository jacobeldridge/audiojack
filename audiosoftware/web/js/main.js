
eel.expose(prompt_alerts);
window.onload = effect();
var counter = 1
// async function check(){
//   let a = await eel.filescheck()();
//   console.log("iran")
//   if(a === false){
//     hide()
    
//   }
//   else{
    
//     //pass
//   }
  
// }
// setInterval(check, 1000);

function hide(){
  document.getElementById("hidebuttons").style.display = "block";
}
function playsound(){
  eel.play();
}
function nexttrack(){
  eel.crease(1);
  effect();
}
function prevtrack(){
  eel.crease(-1);
  effect();
}
function prompt_alerts(description) {
  alert(description);
}
async function effect(){
  let thename = await eel.effectpy()();
  document.getElementById("effect").innerHTML = thename;
}
async function loop(){
  
  
  loopelem = document.getElementById("loop")
  
  if(counter < 4 && counter != 0){
    loopelem.className = 'red';
    loopelem.innerHTML = "&#11119 "+counter;
    
    let x = await eel.loop(counter)();
    counter++
    
  }
  else if(counter === 0){
    loopelem.className = 'red';
    counter++
    loopelem.innerHTML = "&#11119 "+counter;
    let x = await eel.loop(counter)();
    
  }
  else{
    
    loopelem.className = 'loop';
    loopelem.innerHTML = "&#11119";
    counter = 0;
    let x = await eel.loop(counter)();
  }
  
}


