
wk07_prob_below

## Purpose<br>목적
* The `main` module contains the `probability_below()` function, used to calculate the probability of a randomly selected value from a dataset being less than a specified bound.<br>`main` 모듈의 `probability_below()` 함수는 임의의 데이터 집합에서 임의로 선택된 값이 주어진 상한값보다 작을 확률을 계산함.

## Functionality<br>기능
### Input<br>입력
* `data` : A list-like containing numerical data<br>데이터 값을 담은 리스트 비슷한 자료형
* `bound` : A float value representing the upper limit.<br>`float`형 상한값

### Process<br>과정
1. Determin the total number of elements within the `data` list.<br>`data` 리스트 안의 전체 요소 갯수를 구하시오.
1. Count the number of elements in `data` that are less than `bound`.<br>`data` 안의 요소 가운데 `bound` 보다 작은 요소의 갯수를 세시오.
1. Divide the count from step 2 by the total number of elements from step 1.<br>2 단계에서 구한 갯수를 1 단계에서 구한 전체 갯수로 나누시오.

### Output<br>출력
* A `float` value representing the probability that a randomly selected element from `data` will be less than `bound`.<br>`data` 에서 무작위로 선택한 값이 `bound`보다 작을 `float`형 확률값

## Function Specification<br>함수 명세
``` python
def probability_below(data: Iterable[float], bound: float) -> float:
    pass
```

## Example Usage<br>예시
``` python
>>> data = (0, 1, 2, 3, 4)
>>> bound = 1.5
>>> print(probability_below(data, bound))
0.4
```

``From here is common to all assignments.``

## Notes

* This assignment was developed with the assistance of an AI language model for creative inspiration and guidance, demonstrating the potential of AI as a tool to enhance learning and problem-solving.  Students are encouraged to use AI responsibly and ethically, always prioritizing their own understanding and critical thinking.

## NOTICE REGARDING STUDENT SUBMISSIONS<br>제출 결과물에 대한 알림

* Your submissions for this assignment may be used for various educational purposes. These purposes may include developing and improving educational tools, research, creating test cases, and training datasets.<br>제출 결과물은 다양한 교육 목적으로 사용될 수 있을 밝혀둡니다. (교육 도구 개발 및 개선, 연구, 테스트 케이스 및 교육용 데이터셋 생성 등).

* The submissions will be anonymized and used solely for educational or research purposes. No personally identifiable information will be shared.<br>제출된 결과물은 익명화되어 교육 및 연구 목적으로만 사용되며, 개인 식별 정보는 공유되지 않을 것입니다.

* If you do not wish to have your submission used for any of these purposes, please inform the instructor before the assignment deadline.<br>위와 같은 목적으로 사용되기 원하지 않는 경우, 과제 마감일 전에 강사에게 알려주기 바랍니다.

``Until here is common to all assignments.``
