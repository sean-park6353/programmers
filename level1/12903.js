function solution(s) {
    var answer = '';
    var stringLength = s.length;
    var isStringLengthOdd = (stringLength % 2 == 1);
    var index = 0;

    if (isStringLengthOdd) {
        index = stringLength / 2 + 1;
        s = s.slice(index - 1, index);
        answer = s;

        return answer;
    } else {
        index = stringLength / 2;
        s = s.slice(index - 1, index + 1);
        answer = s;

        return answer;
    }

}