//@ts-check : enable more type checks for editor
//@handler  : Расчет расстояний до маячков
//@author   : Iprofi-254187039

/**
 * Makes the sum of two numbers
 * @author `iprofi-254187039`
 * @param {object} data 
 */
function process(data) {
  function distance(beac_coords,current_coords){
    let dist = Math.sqrt(Math.pow((beac_coords.x -current_coords.x),2)+Math.pow((beac_coords.y - current_coords.y),2)+
                          +Math.pow((beac_coords.z -current_coords.z),2));
    return Number(dist).toFixed(2);
  }
  
  // экспортировал данные по расположению маяков с раздела со схемой
  var beacons_from_scheme = {
  "beacons": [
    {
      "name": "98:12",
      "x": 10,
      "y": 25,
      "z": -27
    },
    {
      "name": "0a:35",
      "x": 90,
      "y": 5,
      "z": -27
    },
    {
      "name": "29:39",
      "x": 10,
      "y": 5,
      "z": -27
    },
    {
      "name": "d3:96",
      "x": 90,
      "y": 25,
      "z": -27
    },
    {
      "name": "f7:41",
      "x": 37,
      "y": 25,
      "z": -27
    },
    {
      "name": "01:dd",
      "x": 64,
      "y": 25,
      "z": -27
    },
    {
      "name": "08:cd",
      "x": 37,
      "y": 5,
      "z": -27
    },
    {
      "name": "0e:60",
      "x": 64,
      "y": 5,
      "z": -27
    }
  ]
} 
  if(!data){return {};}

  let current_coords = data;
  let x_coord = current_coords.x;
  let y_coord = current_coords.y;
  let z_coord = current_coords.z;

  let distance_to_98_12 = distance(beacons_from_scheme.beacons[0],current_coords);
  let distance_to_0a_35 = distance(beacons_from_scheme.beacons[1],current_coords);
  let distance_to_29_39 = distance(beacons_from_scheme.beacons[2],current_coords);
  let distance_to_d3_96 = distance(beacons_from_scheme.beacons[3],current_coords);
  let distance_to_f7_41 = distance(beacons_from_scheme.beacons[4],current_coords);
  let distance_to_01_dd = distance(beacons_from_scheme.beacons[5],current_coords);
  let distance_to_08_cd = distance(beacons_from_scheme.beacons[6],current_coords);
  let distance_to_0e_60 = distance(beacons_from_scheme.beacons[7],current_coords);  

  return {x_coord,
          y_coord,
          z_coord,
          distance_to_98_12,
          distance_to_0a_35,
          distance_to_29_39,
          distance_to_d3_96,
          distance_to_f7_41,
          distance_to_01_dd,
          distance_to_08_cd,
          distance_to_0e_60};

}

/* ↑ here ends original handler code  */
/* ↓ here goes generated debug  code  */

/* 01. define test values */
const config = {};
const packet = {
  "data": null
};

/* 02. run handler code */
const result = process(
  packet["data"]
);

/* 03. log handler results */
console.log({
  "x_coord": result["x_coord"],
  "y_coord": result["y_coord"],
  "z_coord": result["z_coord"],
  "distance_to_98_12": result["distance_to_98_12"],
  "distance_to_0a_35": result["distance_to_0a_35"],
  "distance_to_29_39": result["distance_to_29_39"],
  "distance_to_d3_96": result["distance_to_d3_96"],
  "distance_to_f7_41": result["distance_to_f7_41"],
  "distance_to_01_dd": result["distance_to_01_dd"],
  "distance_to_08_cd": result["distance_to_08_cd"],
  "distance_to_0e_60": result["distance_to_0e_60"]
});

