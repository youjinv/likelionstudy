function sum(number1, number2){
    return number1 + number2;
}

const sum_result_1 = sum(10, 20); //30반환
const sum_result_2 = sum(20, 30); //50반환

const sum_result = sum_result_1 + sum_result_2; //30 + 50

console.log('총 합은 ' + sum_result + "입니다.");
