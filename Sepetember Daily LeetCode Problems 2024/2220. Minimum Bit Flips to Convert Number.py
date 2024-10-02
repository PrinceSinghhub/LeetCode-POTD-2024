class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        # print(len(start_bin), len(goal_bin))
        count = 0
        if len(start_bin) == len(goal_bin):
            for i in range(len(start_bin)):
                if start_bin[i] == goal_bin[i]:
                    continue
                else:
                    count += 1

        else:
            if len(start_bin) > len(goal_bin):
                x = len(start_bin) - len(goal_bin)
                # print(x)
                start_bin = list(start_bin)
                goal_bin = list(goal_bin)
                goal_bin_2 = ['0'] * x
                goal_bin_2.extend(goal_bin)
                # print(start_bin, goal_bin_2)
                # print(start_bin, goal_bin)
                for i in range(len(start_bin)):
                    if start_bin[i] == goal_bin_2[i]:
                        continue
                    else:
                        count += 1

            else:
                if len(start_bin) < len(goal_bin):
                    x = len(goal_bin) - len(start_bin)
                    # print(x)
                    goal_bin = list(goal_bin)
                    start_bin = list(start_bin)
                    start_bin_2 = ['0'] * x
                    start_bin_2.extend(start_bin)
                    # print(start_bin, goal_bin_2)
                    # print(start_bin, goal_bin)
                    for i in range(len(start_bin_2)):
                        if start_bin_2[i] == goal_bin[i]:
                            continue
                        else:
                            count += 1

        return (count)
