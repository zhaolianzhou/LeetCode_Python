import operator

def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    # WRITE YOUR CODE HERE

    sorted_foreAppList = sorted(foregroundAppList, key = operator.itemgetter(1))

    sorted_backAppList = sorted(backgroundAppList, key = operator.itemgetter(1))

    result_list = dict()
    max_memory = 0

    F_count = len(sorted_foreAppList)
    start_E = 0
    E_count = len(sorted_backAppList)

    for i in range(0, F_count)[::-1]:
        if sorted_foreAppList[i][1] < deviceCapacity:
            j = E_count
            while j >= start_E:
                j -= 1
                exe_memory = sorted_foreAppList[i][1] + sorted_backAppList[j][1]
                if exe_memory <= deviceCapacity:
                    start_E = j-1
                    if max_memory <= exe_memory:
                        max_memory = exe_memory
                        if exe_memory in result_list:
                            result_list[exe_memory].append([sorted_foreAppList[i][0], sorted_backAppList[j][0]])
                        else:
                            result_list[exe_memory] = [[sorted_foreAppList[i][0], sorted_backAppList[j][0]]]
                    break

    # for foreApp in reversed(sorted_foreAppList):
    #     if foreApp[1] < deviceCapacity:
    #         for backApp in reversed(sorted_backAppList):
    #             exe_memory = foreApp[1] + backApp[1]
    #             if exe_memory <= deviceCapacity:
    #                 if max_memory <= exe_memory:
    #                     max_memory = exe_memory
    #                     if exe_memory in result_list:
    #                         result_list[exe_memory].append([foreApp[0], backApp[0]])
    #                     else:
    #                         result_list[exe_memory] = [[foreApp[0], backApp[0]]]
    #                 break

    # for foreApp in foregroundAppList:
    #     if foreApp[1] < deviceCapacity:
    #         for backApp in backgroundAppList:
    #             exe_memory = foreApp[1] + backApp[1]
    #             if exe_memory <= deviceCapacity:
    #                 if max_memory <= exe_memory:
    #                     max_memory = exe_memory
    #                     if exe_memory in result_list:
    #                         result_list[exe_memory].append([foreApp[0], backApp[0]])
    #                     else:
    #                         result_list[exe_memory] = [[foreApp[0], backApp[0]]]


    return result_list[max_memory]




if __name__ == "__main__":
    str1 = [[1,8], [2,15],[3, 9], [4, 7]]
    str2 = [[1,8], [2, 11], [3, 12], [4, 13]]
    print(optimalUtilization(20, str1,  str2))