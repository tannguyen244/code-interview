import itertools
from itertools import groupby, chain
from operator import itemgetter

def main():
    NATInstances = {
    "1": "us-west1-a",
    "2": "us-west1-b",
    "3": "us-west1-a",
    "4": "us-west1-c"
    }
    Subnets = {
    "1": "us-west1-a",
    "2": "us-west1-b",
    "3": "us-west1-b",
    "4": "us-west1-c",
    "5": "us-west1-c"
    }
    az_a_nat_instances = []
    az_a_subnets = []
    az_b_nat_instances = []
    az_b_subnets = []
    az_c_nat_instances = []
    az_c_subnets = []
    az_dic = {}
    for k, v in NATInstances.items():
        if v == 'us-west1-a':
            az_a_nat_instances.append(str(k + "-" + v))
        elif v == 'us-west1-b':
            az_b_nat_instances.append(str(k + "-" + v))
        elif v == 'us-west1-c':
            az_c_nat_instances.append(str(k + "-" + v))
    for k, v in Subnets.items():
        if v == 'us-west1-a':
            az_a_subnets.append(str(k + "-" + v))
        elif v == 'us-west1-b':
            az_b_subnets.append(str(k + "-" + v))
        elif v == 'us-west1-c':
            az_c_subnets.append(str(k + "-" + v))
    allocate_az_a = list(itertools.izip(itertools.cycle(az_a_nat_instances), az_a_subnets))
    allocate_az_b = list(itertools.izip(itertools.cycle(az_b_nat_instances), az_b_subnets))
    allocate_az_c = list(itertools.izip(itertools.cycle(az_c_nat_instances), az_c_subnets))
    az_dic['az_a'] = allocate_az_a
    az_dic['az_b'] = allocate_az_b
    az_dic['az_c'] = allocate_az_c
    for k, v in az_dic.items():
        if not v and k == "az_c" and az_c_subnets:
            az_a_b_nat_instances = az_a_nat_instances + az_b_nat_instances
            allocate_az_c = list(itertools.izip(itertools.cycle(az_a_b_nat_instances), az_c_subnets))
            az_dic['az_c'] = allocate_az_c
        if not v and k == "az_b" and az_b_subnets:
            az_a_c_nat_instances = az_a_nat_instances + az_c_nat_instances
            allocate_az_b = list(itertools.izip(itertools.cycle(az_a_c_nat_instances), az_b_subnets))
            az_dic['az_b'] = allocate_az_b
        if not v and k == "az_a" and az_a_subnets:
            az_b_c_nat_instances = az_b_nat_instances + az_c_nat_instances
            allocate_az_a = list(itertools.izip(itertools.cycle(az_b_c_nat_instances), az_a_subnets))
            az_dic['az_a'] = allocate_az_a
    lst_az_dic = [x for l in az_dic.values() for x in l]
    dic_allocate_result = {}
    for x, y in lst_az_dic:
        if x in dic_allocate_result:
            dic_allocate_result[x].append(y)
        else:
            dic_allocate_result[x] = [y]
    for k, v in dic_allocate_result.items():
        print("instance: %s ; subnet: %s" % (k, ', '.join(v)))
if __name__ == "__main__":
    main()