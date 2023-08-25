

const time_el = document.querySelector('.watch .time');
const start_btn = document.getElementById('start');
const stop_btn = document.getElementById('stop');
const reset_btn = document.getElementById('reset');

let seconds = 0;
let interval = null;

let hrs;
let mins;
let secs;

start_btn.addEventListener('click', start);
stop_btn.addEventListener('click', stop);
reset_btn.addEventListener('click', reset);

function timer(){
  seconds++;

  hrs = Math.floor(seconds / 3600);
  mins = Math.floor((seconds - (hrs * 3600)) / 60);
  secs = seconds % 60;

  if (secs < 10) secs = '0' + secs;
	if (mins < 10) mins = "0" + mins;
	if (hrs < 10) hrs = "0" + hrs;

  time_el.innerText =  `${hrs}:${mins}:${secs}`;
}


function start () {
	if (interval) {
		return
	}

	interval = setInterval(timer, 1000);
}

function stop () {
	clearInterval(interval);
	interval = null;

}

function reset () {
	stop();
	seconds = 0;
	time_el.innerText = '00:00:00';
}

$('#start').click(function(){
  console.log('Startbtn')
  $.ajax({
    type:'GET',
    url:'/start',
    success:function(){
      console.log('data has been stored')
    },
    error:function(){
      console.log('data did not saved');
    }
  })
})


$('#stop').click(function(){
  console.log('Stopbtn')
  $.ajax({
    type:'GET',
    url:'/stop',
    success:function(){
      console.log('stop data has been stored')
    },
    error:function(){
      console.log('stop data not been stored');
    }
  })
})

$('#stop').click(function(){
  console.log('Startbtn')
  $.ajax({
    type:'GET',
    url:'/createtimesheet/',
    success:function(){
      console.log('data has been stored')
    },
    error:function(){
      console.log('data did not saved');
    }
  })
})