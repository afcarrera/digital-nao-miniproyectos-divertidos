document.addEventListener('DOMContentLoaded', () => { 
	const DATE_TARGET = new Date();
	DATE_TARGET.setFullYear(DATE_TARGET.getFullYear()+1);
	DATE_TARGET.setMonth(0);
	DATE_TARGET.setDate(1);
	DATE_TARGET.setHours(0);
	DATE_TARGET.setMinutes(0);
	DATE_TARGET.setSeconds(0);
	DATE_TARGET.setMilliseconds(0);
	const SPAN_DAYS = document.querySelector('span#days');
	const SPAN_HOURS = document.querySelector('span#hours');
	const SPAN_MINUTES = document.querySelector('span#minutes');
	const SPAN_SECONDS = document.querySelector('span#seconds');
	const MILLISECONDS_OF_A_SECOND = 1000;
	const MILLISECONDS_OF_A_MINUTE = MILLISECONDS_OF_A_SECOND * 60;
	const MILLISECONDS_OF_A_HOUR = MILLISECONDS_OF_A_MINUTE * 60;
	const MILLISECONDS_OF_A_DAY = MILLISECONDS_OF_A_HOUR * 24
	function updateCountdown() {
		const NOW = new Date()
		const DURATION = DATE_TARGET - NOW;
		const REMAINING_DAYS = Math.floor(DURATION / MILLISECONDS_OF_A_DAY);
		const REMAINING_HOURS = Math.floor((DURATION % MILLISECONDS_OF_A_DAY) / MILLISECONDS_OF_A_HOUR);
		const REMAINING_MINUTES = Math.floor((DURATION % MILLISECONDS_OF_A_HOUR) / MILLISECONDS_OF_A_MINUTE);
		const REMAINING_SECONDS = Math.floor((DURATION % MILLISECONDS_OF_A_MINUTE) / MILLISECONDS_OF_A_SECOND);
		SPAN_DAYS.textContent = Math.max(0,REMAINING_DAYS);
		SPAN_HOURS.textContent = Math.max(0,REMAINING_HOURS);
		SPAN_MINUTES.textContent = Math.max(0,REMAINING_MINUTES);
		SPAN_SECONDS.textContent = Math.max(0,REMAINING_SECONDS);
	}
	updateCountdown();
	setInterval(updateCountdown, MILLISECONDS_OF_A_SECOND);
});