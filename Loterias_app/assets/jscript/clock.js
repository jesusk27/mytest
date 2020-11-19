var udateTime = function() {
    let currentDate = new Date(),
        hours = currentDate.getHours(),
	ampm,
        minutes = currentDate.getMinutes(), 
        seconds = currentDate.getSeconds(),
        weekDay = currentDate.getDay(), 
        day = currentDate.getDay(), 
        month = currentDate.getMonth(), 
        year = currentDate.getFullYear();

    const weekDays = [
        'Dom.',
        'Lun.',
        'Mar.',
        'Mié.',
        'Jue.',
        'Vie.',
        'Sab.'
    ];

    document.getElementById('weekDay').textContent = weekDays[weekDay];
    document.getElementById('day').textContent = day;
    
    const months = [
        'Ene.',
        'Feb.',
        'Mar.',
        'Abr.',
        'May.',
        'Jun.',
        'Jul.',
        'Ago.',
        'Sep.',
        'Oct',
        'Nov.',
        'Dic.'
    ];

    document.getElementById('month').textContent = months[month];
    document.getElementById('year').textContent = year;
	
	if (hours >= 12){
           hours=hours-12; 
           ampm='PM';
        } else{
            ampm='AM';

        }

	if (hours == 0 ){
			hours = 12;
		}

    document.getElementById('hours').textContent = hours;
    document.getElementById('ampm').textContent = ampm;    



    if (minutes < 10) {
        minutes = "0" + minutes
    }

    if (seconds < 10) {
        seconds = "0" + seconds
    }

    document.getElementById('minutes').textContent = minutes;
    document.getElementById('seconds').textContent = seconds;
};

udateTime();

setInterval(udateTime, 1000);