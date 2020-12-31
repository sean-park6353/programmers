function solution(numbers) {
    var answer = [];

    for (var i = 0; i < numbers.length; i++) {
        for (var j = 0; j < i + 1; j++) {
            if (i !== j) {
                answer.push(numbers[i] + numbers[j]);
            }
        }
    }
    answer = Array.from(new Set(answer));

    answer.sort(function (a, b) {
        return a - b;
    });

    return answer;
}