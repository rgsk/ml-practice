# export ONLINE_JUDGE=true
 
import os
import sys
 
if os.getenv("ONLINE_JUDGE") is not None:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_directory, 'input.txt')
    try:
        sys.stdin = open(input_file_path, 'r')
    except Exception as e:
        sys.stdin = open(input_file_path, 'w')
    output_file_path = os.path.join(script_directory, 'output.txt')
    sys.stdout = open(output_file_path, 'w')
 
 

def main():
    n = int(input())
    for _ in range(n):
        def solve():
            nums = [int(v) for v in input()]
            zeroes_count = 0
            ones_count = 0
            for v in nums:
                if v == 1:
                    ones_count += 1
                else:
                    zeroes_count += 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    ones_count -= 1
                else:
                    zeroes_count -= 1
                if ones_count == -1 or zeroes_count == -1:
                    return len(nums) - i
            return 0
        print(solve())
 
main()