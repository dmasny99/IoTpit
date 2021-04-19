//@ts-check : enable more type checks for editor
//@handler  : Парсинг данных согласно протоколу
//@author   : Iprofi-254187039

/**
 * Makes the sum of two numbers
 * @author `iprofi-254187039`
 * @param {string} beacons
 */

function process(beacons) {
  if(!beacons){
    return{};
  }
  var mac_98_12 = null;
  var mac_0a_35 = null;
  var mac_29_39 = null;
  var mac_d3_96 = null;
  var mac_f7_41 = null;
  var mac_01_dd = null;
  var mac_08_cd = null;
  var mac_0e_60 =null;
  var offset = 0;
  function bit_inverse(st){
    let result = String(st.split('').map(bit => (1-bit).toString()).join(''));
    return result;
  }
  function get_ble_data(num){
    if(num !=0){
      let tmp = (num - 1).toString(2);
      var tmp2 = -1*parseInt(bit_inverse(tmp),2);
    }
    else{tmp2 = 0;}
    return tmp2;
  }
  const buff =ric.base64.decode(beacons);
  let lat_beac = buff.getFloat32(offset).toFixed(2);
  offset += 4;
  let lon_beac = buff.getFloat32(offset).toFixed(2);
  offset += 4;
  let alt_beac = buff.getFloat32(offset).toFixed(2);
  offset += 4;
  let ev_time = buff.getInt32(offset)*1000;
  offset += 4;
  var visible_count = buff.getUint8(offset);
  offset += 1;
  
  for(let i = 0;i < visible_count; i++){
    switch("0x"+buff.getUint16(offset).toString(16).padStart(4,"0")) {
      case "0x9812":
        offset +=2;
        mac_98_12 = get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
      case "0x0a35":
        offset +=2;
        mac_0a_35 = get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
      case "0x2939":
        offset +=2;
        mac_29_39 = get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
      case "0xd396":
        offset +=2;
        mac_d3_96 =get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
      case "0xf741":
        offset +=2;
        mac_f7_41 = get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
      case "0x01dd":
        offset +=2;
        mac_01_dd = get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
      case "0x08cd":
        offset +=2;
        mac_08_cd = get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
      case "0x0e60":
        offset +=2;
        mac_0e_60 = get_ble_data(buff.getUint8(offset));
        offset +=1;
        break;
    }
  }
  return {lat_beac,
          lon_beac,
          alt_beac,
          ev_time,
          visible_count,
          mac_98_12,
          mac_0a_35,
          mac_29_39,
          mac_d3_96,
          mac_f7_41,
          mac_01_dd,
          mac_08_cd,
          mac_0e_60};

}

/* ↑ here ends original handler code  */
/* ↓ here goes generated debug  code  */

/* 01. define test values */
const config = {};
const packet = {
  "beacons": "string"
};

/* 02. run handler code */
const result = process(
  packet["beacons"]
);

/* 03. log handler results */
console.log({
  "lat_beac": result["lat_beac"],
  "lon_beac": result["lon_beac"],
  "alt_beac": result["alt_beac"],
  "ev_time": result["ev_time"],
  "visible_count": result["visible_count"],
  "mac_98_12": result["mac_98_12"],
  "mac_0a_35": result["mac_0a_35"],
  "mac_29_39": result["mac_29_39"],
  "mac_d3_96": result["mac_d3_96"],
  "mac_f7_41": result["mac_f7_41"],
  "mac_01_dd": result["mac_01_dd"],
  "mac_08_cd": result["mac_08_cd"],
  "mac_0e_60": result["mac_0e_60"]
});

