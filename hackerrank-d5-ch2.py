from dataclasses import dataclass, field


@dataclass
class Queue(object):
    """[summary]

    Args:
        object ([type]): [description]

    Returns:
        [type]: [description]
    """

    _stack_1: list = field(default_factory=list)
    _stack_2: list = field(default_factory=list)

    def __enqueue(self, value: int) -> None:
        """[summary]

        Args:
            value (int): [description]
        """
        self._stack_1.append(value)

    def __dequeue(self) -> list:
        """[summary]

        Returns:
            list: [description]
        """
        if len(self._stack_2) == 0 and len(self._stack_1) > 0:
            while len(self._stack_1):
                self._stack_2.append(self._stack_1.pop())
        return self._stack_2.pop()

    def __front(self) -> str:
        """[summary]

        Returns:
            str: [description]
        """
        if len(self._stack_2) == 0 and len(self._stack_1) > 0:
            while len(self._stack_1):
                self._stack_2.append(self._stack_1.pop())
        print(self._stack_2[0])


if __name__ == "__main__":
    temp = Queue()
    temp._Queue__enqueue(42)
    temp._Queue__dequeue()
    temp._Queue__enqueue(14)
    temp._Queue__front()
    temp._Queue__enqueue(28)
    temp._Queue__front()
    temp._Queue__enqueue(60)
    temp._Queue__enqueue(78)
    temp._Queue__dequeue()
    temp._Queue__dequeue()
