from django.test import TestCase

from tabom.models import User


# Create your tests here.
class TestAutoNow(TestCase):
    """
    django 의 TestCase 클래스를 상속하는 클래스를 만든다.
    class 의 이름은 Test 로 시작해야 합니다. (pytest 에서는 무조건적인 규칙인데, unit test 에서는 강제는 아닙니다.)

    - unit test -> 파이썬 언어 자체에 내장된 테스트 프레임워크
    - pytest -> 써드파티 라이브러리 (poetry add 로 추가해야 됩니다.) 사실상 파이썬 표준.
    """

    def test_auto_now_field_is_set_when_save(self) -> None:
        """
        모든 테스트 함수는 None 을 리턴합니다.

        테스트 함수는 3가지 단계로 이루어집니다.

        given (주어진)
        테스트의 대상이 되는 재료를 만듭니다.
        e.g.) 좋아요를 하려면 좋아요를 하는 유저와, 대상이되는 게시글이 필요. 이 둘을 생성합니다.
        when
        실제로 검증해야 하는 동작을 수행합니다.
        e.g.) 좋아요를 하는 함수를 호출합니다.
        then
        정상적으로 수행이 됬는지 검증합니다.
        e.g.) 좋아요 row 가 데이터베이스에 insert 되었는지 확인합니다.
        """
        # given
        user = User(name="test")

        # when
        user.save()

        # then
        # 상속에 의해서 assertXXX 메소드들을 물려받았습니다.
        self.assertIsNotNone(user.updated_at)
        self.assertIsNotNone(user.created_at)

    def test_sample(self) -> None:
        print("none")


"""
## 테스트 함수가 실패와 성공을 판가름 하는 방법
- 테스트 함수는 아무런 exception 이 발생하지 않고 종료되었을때 성공합니다.
- 반대로, 어떤 Exception 이든 exception 이 발생했다면 실패입니다.
- 검증을 하되, 검증 실패시 에러가 일어나도록 하고 싶다면 `assert` 를 사용합니다.
e.g.) `assert 1 + 1 == 2`
"""

"""
- 디버깅을 비정상종료 할 경우 쟝고가 테스트 데이터베이스를 삭제하지 못합니다. 그 다음번에 테스트를 실행하면 "데이터베이스를 삭제하고 새로 만들어도 되나요?" 라고
django 가 물어보는데, 이 때는 yes 하면 됩니다.
"""
