def hillClimb(arr, start_index):

    if start_index < 0 or start_index >= len(arr):
        return None

    current_index = start_index


    while True:

        left = current_index - 1 if current_index > 0 else current_index
        right = current_index + 1 if current_index < len(arr) - 1 else current_index

        # Check to see if code is already at peak
        if arr[left] < arr[current_index] and arr[right] < arr[current_index]:
            return current_index, arr[current_index]

        # Shoulder Checks --------------------------------------
        # Shoulder check right
        while right < len(arr) and arr[right] == arr[current_index]:
            current_index = right
            right += 1

        # Shoulder check left
        while left > 0 and arr[left] == arr[current_index]:
            current_index = left
            left -= 1
        # Highest hill code ----------------------------------
        # Choose the higher path
        if right < len(arr) and left > 0 and arr[right] > arr[current_index] and arr[left] > arr[current_index]:
            if arr[right] > arr[left]:
                current_index = right
            else:
                current_index = left

        # check if in pit
        elif right < len(arr) and arr[right] > arr[current_index]:
            current_index = right

        elif left > 0 and arr[left] > arr[current_index]:
            current_index = left
        else:
            return current_index, arr[current_index]
