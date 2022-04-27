let student1 = {
    koreanScore:90, //국어 점수
    "englishScore":70, //영어 점수
    'mathScore':80, //수학 점수
    scienceScore:60 //과학 점수
    //문자열로 키 작성시 공백 가능
    //공백이 있는 키 값은 점 연산자로는 불가능
};

//대괄호 연산자
console.log(student1["englishScore"]);

//점(닷, 마침표) 연산자
console.log(student1.mathScore);