import robots from './data.js';

let wrapper = document.querySelector(".wrapper");

function createRobot(robot) {
    let element = document.createElement('div');
    element.classList.add('robot');

    element.style.gridColumnStart = robot.p[0];
    element.style.gridRowStart = robot.p[1];

    return element;
}

robots.forEach(robot => wrapper.appendChild(createRobot(robot)));

let slider = document.querySelector(".slider");
let box = document.querySelector(".box");


function updateRobots(time) {
    const robotElements = document.getElementsByClassName("robot");

    for(let i = 0; i < robots.length; i++) {
        const robotEl = robotElements[i];
        const robot = robots[i];

        const posx = (robot.p[0] + time * robot.v[0]) % 101;
        const posy = (robot.p[1] + time * robot.v[1]) % 103;

        robotEl.style.gridColumnStart = posx;
        robotEl.style.gridRowStart = posy;
    }
}

function handleSliderChange(event) {
    const time = event.target.value;
    updateRobots(time);

    box.value = time;

}

function handleBoxChange(event) {
    const time = event.target.value;
    updateRobots(time);

    slider.value = time;

}

slider.addEventListener('change', handleSliderChange);
box.addEventListener('change', handleBoxChange);




// {robots.map(robot => {
//     let posx = ((robot.p[0] + (77+101*(76+103*time)) * robot.v[0]) % 101)
//     let posy = ((robot.p[1] + (77+101*(76+103*time)) * robot.v[1]) % 103)
    
//     return (
//       <div className="robot" style={{
//         gridColumnStart: posx,
//         gridRowStart: posy,
//       }}></div>
//     );
//   })}