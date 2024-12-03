from bisect import bisect_right


class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        prime_numbers = [True] * 1010
        prime_numbers[0] = prime_numbers[1] = False

        for i in range(2, len(prime_numbers)):
            if prime_numbers[i] and i ** 2 < len(prime_numbers):
                for j in range(i ** 2, len(prime_numbers), i):
                    prime_numbers[j] = False

        primes = []
        for i in range(len(prime_numbers)):
            if prime_numbers[i]:
                primes.append(i)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                nums[i] -= primes[bisect_right(primes, nums[i] - nums[i + 1])]

                if nums[i] <= 0:
                    return False
        return True