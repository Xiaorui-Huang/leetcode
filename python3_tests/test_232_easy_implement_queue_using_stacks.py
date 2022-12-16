import pytest
from lc_232_easy_implement_queue_using_stacks import MyQueue


@pytest.fixture
def queue() -> MyQueue:
    return MyQueue()


def test_queue_empty(queue: MyQueue) -> None:
    assert queue.empty() == True
    with pytest.raises(Exception):
        queue.peek()
    with pytest.raises(Exception):
        queue.pop()

    queue.push(1)
    queue.push(2)
    assert len(queue) == 2
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() == False
    assert queue.pop() == 2
    assert queue.empty() == True
    with pytest.raises(Exception):
        queue.pop()
    with pytest.raises(Exception):
        queue.peek()


def test_queue_pushes_and_pops(queue: MyQueue) -> None:
    for i in range(1, 4 + 1):
        queue.push(i)

    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.pop() == 2
    queue.push(5)
    queue.push(6)
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.peek() == 6
    assert queue.empty() == False
    assert queue.pop() == 6
    assert queue.empty() == True
    with pytest.raises(Exception):
        queue.pop()

    with pytest.raises(Exception):
        queue.peek()
