//// Change these as needed ////

const name = 'Michael';

const format_12hour = true;
const tempUnit = 'F';  // Change to 'C' for Celsius

// https://www.latlong.net/
const latitude = 41.829639;
const longitude = -86.252541;
const key = '16a924c654ff0e555f921a43d62a31d5';  // https://openweathermap.org/

// Here you can change your greetings
const gree1 = 'Good evening, ';
const gree2 = 'Good morning, ';
const gree3 = 'Good afternoon, ';

////////////////////////////////

// greeting();
displayClock();

// getWeather();

function greeting() {
    const today = new Date();
    const hour = today.getHours();

    // Define the hours of the greetings
    if (hour >= 17 || hour < 6) {
        document.getElementById('greetings').innerText = gree1 + name;
    } else if (hour >= 6 && hour < 12) {
        document.getElementById('greetings').innerText = gree2 + name;
    } else {
        document.getElementById('greetings').innerText = gree3 + name;
    }
}

function displayClock() {
    const monthNames = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ];

    const dayNames = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ];

    const date = new Date();
    const year = String(date.getFullYear());
    const month = monthNames[date.getMonth()];
    const day = String(date.getDate());
    const dayOfWeek = dayNames[date.getDay()];
    const minute = ('0' + date.getMinutes()).slice(-2);
    let hour = String(date.getHours());
    let ampm = '';
    let daySuffix = "th";

    if (format_12hour) {
        ampm = hour >= 12 ? ' pm' : ' am';
        hour = hour % 12;
        hour = hour ? hour : 12; //show mod 0 as 12
    }

    if (date.getDate() < 4 || date.getDate() > 20) {
        switch (date.getDate() % 10) {
            case 1:
                daySuffix = "st";
                break;
            case 2:
                daySuffix = "nd";
                break;
            case 3:
                daySuffix = "rd";
                break;
            default:
                daySuffix = "th";
        }
    }

    document.getElementById('time').innerText = `${hour}:${minute}${ampm}`
    document.getElementById('date').innerText = `${dayOfWeek} ${month} ${day}${daySuffix}, ${year}`
    setTimeout(displayClock, 1000);
}

// const iconElement = document.querySelector('.weather-icon');
const tempElement = document.querySelector('#temperature-value p');
const descElement = document.querySelector('#temperature-desc p');

// App data
const weather = {};
weather.temperature = {
    unit: 'celsius',
};

// Get the Weather data
function getWeather() {
    let api = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${key}`;
    const KELVIN = 273.15;

    fetch(api)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            let celsius = Math.floor(data.main.temp - KELVIN);
            weather.temperature.value = (tempUnit === 'C') ? celsius : (celsius * 9 / 5) + 32;
            weather.description = data.weather[0].description;
            // weather.iconId = data.weather[0].icon;
        })
        .then(function () {
            document.getElementById('weather-value').innerText = `${weather.temperature.value}°${tempUnit}`;
            document.getElementById('weather-desc').innerText = weather.description;

        });
}