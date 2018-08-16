console.log("0");

// 변수
// 파이썬 a = 1
// javascript
var a = 1  // 변수
const b = 1  // 상수(값이 변경x)
// let c = 2  //  나중에 이해~

// 함수
function sum(x , y){
    return x+y
}

console.log( sum(1,2) )

// 무명(익명)함수 >> 1회성 or 변수로 받기
var c = function(x , y){
    return x+y
}
console.log(c(5,6))

// 애로우(화살표) 함수 (방법들 .. 축약형!!)
var d = (x , y) =>  x+y

var e = (x , y) =>  {
    return x+y
}

// 콜백함수 : 익명함수의 클로저 사용
function test( name , cb ){
    cb( name + "1" );
}

test( '멀티' , function( msg ){
    console.log( '>>' , msg);
} );