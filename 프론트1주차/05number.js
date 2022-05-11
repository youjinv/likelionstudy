let integer = 10; //10진수
//0~9
let hex = 0xa; //16진수
//0~9사용하고 남는 자리는 A~F까지 사용
let binary = 0b1010; //2진수
//0,1만 사용
//0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010...
let octal = 0o12 //8진수
//0~7까지만 사용(아마도 요일?)
//1234567->1011121314151617 

console.log(integer, hex, binary, octal);

let negative = -10; //음의 정수
let indices = 1.0e1; //지수
let double = 10.12; //소수

console.log(negative, double, indices);