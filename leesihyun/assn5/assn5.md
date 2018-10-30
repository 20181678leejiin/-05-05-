소프트웨어프로젝트2 과제5 
===
20181664 이시현
----------
---- 
 - 과제를 해결하기 위해 고안했던 점
 if문의 반복을 없애기 위해 눌리는 버튼의 종류에 따라 종속적으로 그에 상응하는 기능을 인덱스의 참조 없이 수행하게하면 될거 같다는 생각을 하였습니다.
----

 - 코드의 구현
     - keypad2.py 안에  funtion이라는 딕셔너리를 만들어었습니다.
    <pre><code>
    function = {
        'pi': calcFunctions.Pi,
        '빛의 이동 속도 (m/s)': calcFunctions.Light_speed,
        '소리의 이동 속도 (m/s)':calcFunctions.Sound_speed,
        '태양과의 평균 거리 (km)':calcFunctions.Sun_dis,
        'factorial (!)':calcFunctions.factorial,
        '-> binary':calcFunctions.decToBin,
        'binary -> dec':calcFunctions.binToDec
    }
    </pre></code>

    - function 딕셔너리 안에 들어있는 함수들의 기능들을 구현하였습니다.
    <pre><code>
    def Pi(input):
        return input + '3.141592'
    
    def Light_speed(input):
        return input + '3E+8'
        
    def Sun_dis(input):
        return input + '1.5E+8'
        
    def Sound_speed(input):
        return input + '340'
    </pre></code>

    - buttonClicked()함수 안에 기존 elif문을 삭제,수정하여 눌린 버튼의 이름을 확인해 그에 맞는 기능을 딕셔너리를 통해 수행하도록 하였습니다.
    <pre><code>
     if key == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)
    elif key == 'C':
            self.display.clear()
    elif key in keypad2.function:
            temp = keypad2.function[key](self.display.text())
            self.display.setText(temp)
    else:
            self.display.setText(self.display.text() + key)
    </pre></code>
---
- 코드리뷰를 통해 배운 점
    - 저의 코드는 function 딕셔너리에 있는 key값들이 무조건 functionList안에 있는 원소들과 동일해야한다는 위험성이 있었습니다.
    - 버튼이 추가되었을 떄 수정해야하는 코드의 부분이 3군데나 되었습니다.
    - 계산기가 최대 15자리까지 표현하기 때문에 15자리 숫자보다 더 큰 숫자를 계산하면 이상한 값이 나오게 됩니다.

---
- 코드리뷰를 통해 개선한 부분
    - function딕셔너리를 없애고 새로 튜플을 원소로 갖는 두개의 리스트를 새로 만들었습니다.
    그리고 기존의 functionList와 constantList는 새로 만든 리스트의 첫 번째 원소와 완전히 동일함으로 그대로 대입시켜 만들어 주었습니다. 그리고 calcFunc모듈안에 만들었던 함수들은 없앴습니다.
    <pre><code>
    function = [
        ('factorial (!)',calcFunctions.factorial),
        ('-> binary',calcFunctions.decToBin),
        ('binary -> dec',calcFunctions.binToDec)
    ]
    constant = [
        ('pi','3.141592'),
        ('빛의 이동 속도 (m/s)','3E+8'),
        ('소리의 이동 속도 (m/s)','1.5E+8'),
        ('태양과의 평균 거리 (km)','340')
    ]

    functionList = [x[0] for x in function]
    constantList = [x[0] for x in constant]
    </pre></code>
    
    - buttonClicked메소드에서 기존의 elif문을 하나 더 늘려 수정하였습니다.
    <pre><code>
        if key == '=':
            try:
            result = str(eval(self.display.text()))
        except:
            result = 'Error!'
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()
        elif key in functionList:
            i = functionList.index(key)
            temp = keypad2.function[i][1](self.display.text())
            self.display.setText(temp)
        elif key in constantList:
            i = constantList.index(key)
            temp = self.display.text()+keypad2.constant[i][1]
            self.display.setText(temp)
        else:
            self.display.setText(self.display.text() + key)
    </pre></code>
---

