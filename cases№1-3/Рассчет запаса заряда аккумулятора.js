//@ts-check : enable more type checks for editor
//@handler  : Рассчет запаса заряда аккумулятора
//@author   : Iprofi-254187039

/**
 * Makes the sum of two numbers
 * @author `iprofi-254187039`
 * @param {number} charge charge of the costume
 * @param {number} battery_capacity b_c of the costume 
 * @param {number} power_in_hour KWt/hour
 */
function process(charge,battery_capacity,power_in_hour) {
    if(power_in_hour < 0 || battery_capacity < 0 || charge < 0 || charge > 100 || charge == null){
      return{};
    }
    else{
    let minutes_reserve = Math.round((0.01*charge*battery_capacity / power_in_hour) *60);
    return{minutes_reserve};
    }
}

/* ↑ here ends original handler code  */
/* ↓ here goes generated debug  code  */

/* 01. define test values */
const config = {};
const packet = {
  "charge": 37,
  "battery_capacity": 84,
  "power_in_hour": 69
};

/* 02. run handler code */
const result = process(
  packet["charge"],
  packet["battery_capacity"],
  packet["power_in_hour"]
);

/* 03. log handler results */
console.log({
  "minutes_reserve": result["minutes_reserve"]
});

