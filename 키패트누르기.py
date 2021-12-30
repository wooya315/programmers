def solution(numbers, hand):
    answer = ''
    left_hand_current = "*"
    right_hand_current = "#"
    phone = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        "*": (3, 0), 0: (3, 1), "#": (3, 2)
    }
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left_hand_current = number
        elif number in [3, 6, 9]:
            answer += "R"
            right_hand_current = number
        else:
            left_finger_x_distance = abs(
                phone[number][0] - phone[left_hand_current][0])
            left_finger_y_distance = abs(
                phone[number][1] - phone[left_hand_current][1])
            left_finger_distance = left_finger_x_distance + left_finger_y_distance
            right_finger_x_distance = abs(
                phone[number][0] - phone[right_hand_current][0])
            right_finger_y_distance = abs(
                phone[number][1] - phone[right_hand_current][1])
            right_finger_distance = right_finger_x_distance + right_finger_y_distance
            if left_finger_distance > right_finger_distance:
                answer += "R"
                right_hand_current = number
            elif left_finger_distance < right_finger_distance:
                answer += "L"
                left_hand_current = number
            else:
                if hand == "right":
                    answer += "R"
                    right_hand_current = number
                elif hand == "left":
                    answer += "L"
                    left_hand_current = number
    return answer
