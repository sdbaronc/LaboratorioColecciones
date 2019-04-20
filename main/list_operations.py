def list_sum(list):
    sum=0

    for j in range(0,12):
        sum = sum+ list[j]

def lis_average(list):

    sum_list=list_sum(list)
    len_list=len(list)
    prom=sum_list/len_list
    return prom
def lis_max(list):
    max_element=list[0]
    pos_element=0
    cont=0
    for item in list:
        if item>max_element:
            max_element= item
            pos_element=cont
        cont+=1
    return max_element